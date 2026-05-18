# Media `src` Data URI Injection

This flag was found through an XSS vulnerability in the media handler of the Darkly web application.

The vulnerable URL was:

```txt
http://192.168.56.101/index.php?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
```

The payload is a Base64-encoded HTML document containing:

```html
<script>alert(1)</script>
```

When the payload was passed through the `src` parameter, the browser executed the JavaScript. This showed that the application was taking user-controlled input from `src` and placing it into an HTML `<object>` resource context without proper validation.

## How We Discovered It

Testing XSS in normal input fields using a classic payload:

```html
<script>alert(document.cookie)</script>
```

That payload worked and revealed:

```txt
I_am_admin=68934a3e9455fa72420237eb05902327
```

However, that cookie was already related to a previously solved flag, so it did not count as a new XSS flag. It only confirmed that the application had XSS-prone areas.

After that, we looked for a different XSS context. The important clue was the presence of URL parameters that control content loaded by the page. In Darkly, one of those parameters is:

```txt
page=media&src=...
```

When we opened the normal media page, the source confirmed how the handler renders media:

```html
<object data="http://192.168.56.101/images/nsa_prism.jpg"></object>
```

This is the exact sink. The page places a media path inside the `data` attribute of an `<object>` tag.

The reasoning process was:

1. The URL used `page=media`.
2. The URL accepted a `src` parameter.
3. The page source showed an `<object data="..."></object>` tag.
4. A `data:text/html;base64,...` payload was passed into `src`.
5. The browser executed JavaScript from that payload.
6. Therefore, the application was allowing attacker-controlled content to reach the `<object data>` resource attribute.

The vulnerable pattern is:

```html
<object data="USER_CONTROLLED_VALUE"></object>
```

The page should only load approved media resources, but it accepts a value that can become an inline HTML document through a `data:` URI.

## Payload Explanation

The working payload was:

```txt
data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
```

This is a `data:` URI.

A `data:` URI allows content to be embedded directly inside a URL. In this case, the content type is:

```txt
text/html
```

The Base64 part is:

```txt
PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
```

Decoded, it becomes:

```html
<script>alert(1)</script>
```

So the full meaning is:

```txt
Load this inline HTML document, then execute its script.
```

Because the application placed this value inside a media source context, the browser treated it as active content.


## Vulnerability Type

This is a form of Cross-Site Scripting through unsafe resource embedding.

More specifically:

```txt
User-controlled src parameter -> embedded into HTML -> browser executes attacker-controlled content
```

The root issue is insufficient validation of a URL-like parameter.

## Impact

An attacker could use this kind of vulnerability to execute JavaScript in the victim's browser.

Depending on the application, this could allow:

- stealing cookies or session tokens if they are not protected
- performing actions as the victim
- redirecting the victim to malicious pages
- modifying the page content
- phishing users inside the trusted application
- bypassing weak client-side protections

In this lab, the impact is demonstrated by triggering JavaScript execution and receiving the flag.

## How to Prevent It

The main rule is:

```txt
Never trust user-controlled input as a resource URL without strict validation.
```

Good protections include:

### 1. Use an Allowlist

Only allow known safe media identifiers instead of accepting arbitrary URLs.

Bad design:

```txt
?page=media&src=anything
```

Better design:

```txt
?page=media&id=nsa
```

Then the server maps `id=nsa` to a known safe file:

```php
$allowed = [
    "nsa" => "/images/nsa.jpg",
    "logo" => "/images/logo.png"
];
```

The user controls only the key, not the final resource path.

### 2. Block Dangerous Schemes

If URLs must be accepted, reject dangerous schemes such as:

```txt
javascript:
data:
vbscript:
file:
```

Only allow schemes such as:

```txt
https:
```

or local paths that are known to be safe.

### 3. Validate Content Type

If the field is supposed to load an image, only allow real image files and image MIME types:

```txt
image/png
image/jpeg
image/gif
```

Do not allow:

```txt
text/html
image/svg+xml
application/javascript
```

SVG can contain JavaScript, so it should be handled carefully.

### 4. Escape Output Based on Context

Escaping must match where the value is inserted.

For example, HTML text, HTML attributes, JavaScript strings, and URLs all need different escaping rules.

For URL attributes, encode and validate the URL before rendering it.

### 5. Add a Strong Content Security Policy

A Content Security Policy can reduce the damage of XSS.

For example, a safer policy may block inline scripts and `data:` documents:

```http
Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self'
```

Depending on the application, also avoid allowing:

```txt
data:
unsafe-inline
*
``

in sensitive directives.


