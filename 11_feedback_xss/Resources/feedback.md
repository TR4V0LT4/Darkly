# Feedback Stored XSS

## Summary

This breach is located in the feedback page.

The vulnerability is that the application stores user feedback and renders it back into the page without escaping HTML special characters.

Because the feedback input is rendered as raw HTML, an attacker can inject JavaScript.

Final flag:

```txt
0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e
```

## How I Discovered It

I first noticed that the message I submitted appeared back on the feedback page.

That means the input was either reflected or stored and then rendered into the HTML response.

To test whether HTML was escaped, I submitted:

```html
<b>test</b>
```

If the word `test` appears in bold, it means the application is interpreting the input as HTML instead of displaying it safely as text.

After confirming that HTML tags were interpreted, I submitted a JavaScript payload:

```html
<script>alert(1)</script>
```

The browser executed the script, proving that the page is vulnerable to XSS.

The application then displayed the flag:

```txt
The flag is : 0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e
```

## Vulnerable Flow

The vulnerable flow is:

```txt
feedback input -> stored in page -> rendered without escaping -> browser treats it as HTML/JS
```

The application should treat feedback as text, but instead it allows the browser to parse the submitted content as HTML.

## Why This Is Vulnerable

User-controlled input is inserted into the page without output encoding.

For example, if the user submits:

```html
<script>alert(1)</script>
```

the page should display it safely as text:

```html
&lt;script&gt;alert(1)&lt;/script&gt;
```

Instead, the browser receives the real `<script>` tag and executes it.

This is a stored XSS vulnerability because the payload is saved and displayed later from the feedback page.

## Impact

An attacker could inject JavaScript that runs in the browser of anyone who views the feedback page.

In a real application, this could allow:

- stealing session cookies if they are not protected
- performing actions as another user
- changing page content
- redirecting users to malicious pages
- phishing users inside the trusted site

## How To Prevent It

Recommended fixes:

- Escape user output with `htmlspecialchars` or equivalent HTML entity encoding.
- Validate input server-side.
- Never render feedback content as raw HTML.
- Use a Content Security Policy to reduce XSS impact.
- Mark cookies as `HttpOnly`, `Secure`, and `SameSite`.

Example safe PHP output:

```php
echo htmlspecialchars($feedback, ENT_QUOTES, "UTF-8");
```

With this fix, this payload:

```html
<script>alert(1)</script>
```

would be displayed as text instead of being executed by the browser.

The main lesson is:

```txt
Stored user input must be escaped before being rendered into HTML.
```
