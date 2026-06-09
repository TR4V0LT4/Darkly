Good Job Here is the flag : b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3# Unvalidated Redirect

## Summary

This breach is located in the social media footer links.

The application uses a redirect endpoint:

```txt
index.php?page=redirect&site=facebook
index.php?page=redirect&site=twitter
index.php?page=redirect&site=instagram
```

The vulnerability is that the `site` parameter can be modified by the user.

If the backend trusts this parameter without validation, an attacker can control where the application redirects the victim.

Final flag:

```txt
Flag: PUT_THE_FLAG_HERE
```

## How I Discovered It

In the page footer, the social media icons used links like:

```html
<a href="index.php?page=redirect&site=facebook" class="icon fa-facebook"></a>
<a href="index.php?page=redirect&site=twitter" class="icon fa-twitter"></a>
<a href="index.php?page=redirect&site=instagram" class="icon fa-instagram"></a>
```

The interesting part is:

```txt
page=redirect&site=facebook
```

This suggests that the application has a redirect handler and uses the `site` parameter to decide the destination.

Since `site` is controlled by the client, I tested changing it to an unexpected value.

## Exploitation Approach

Original URL:

```txt
http://192.168.56.101/index.php?page=redirect&site=facebook
```

Modified URL:

```txt
http://192.168.56.101/index.php?page=redirect&site=evil
```

or:

```txt
http://192.168.56.101/index.php?page=redirect&site=https://example.com
```

In Darkly, changing the `site` parameter to an unauthorized value triggers the breach and reveals the flag.

## Why This Is Vulnerable

The application allows the user to influence a redirect destination.

A vulnerable backend may do something like:

```php
$site = $_GET["site"];
header("Location: " . $site);
```

or map known values weakly without rejecting unknown values.

The problem is that the server trusts a client-controlled parameter to decide where the user should be redirected.

## Impact

Unvalidated redirects can be used for phishing and social engineering.

For example, an attacker can send a victim a link that starts with the trusted domain:

```txt
http://trusted-site.com/index.php?page=redirect&site=https://evil.example
```

The victim sees the trusted domain first, clicks it, and is redirected to the attacker's site.

This can be used to:

- steal credentials
- bypass user trust checks
- hide malicious URLs behind a trusted domain
- support phishing campaigns
- chain with other vulnerabilities

## How To Prevent It

Recommended fixes:

- Do not allow arbitrary redirect URLs from user input.
- Use an allowlist of known destinations.
- Store redirect targets server-side.
- Reject unknown `site` values.
- Prefer internal route names instead of full URLs.
- If external redirects are required, show an interstitial warning page.

Safer design:

```php
$allowedSites = [
    "facebook" => "https://www.facebook.com/borntosec",
    "twitter" => "https://twitter.com/borntosec",
    "instagram" => "https://www.instagram.com/borntosec",
];

$site = $_GET["site"] ?? "";

if (!array_key_exists($site, $allowedSites)) {
    http_response_code(400);
    exit("Invalid redirect target");
}

header("Location: " . $allowedSites[$site]);
exit;
```

The main lesson is:

```txt
Redirect destinations must be validated server-side. A trusted domain should not redirect users to attacker-controlled locations.
```
