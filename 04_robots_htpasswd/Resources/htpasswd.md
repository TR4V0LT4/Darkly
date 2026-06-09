# Robots.txt and Exposed htpasswd

Using Gobuster, I found several directories and files on the web server, including:

```txt
/robots.txt
/whatever
/admin
```

The `robots.txt` file disclosed a hidden directory:

```txt
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

The `/whatever` directory contained an `htpasswd` file with a username and password hash:

```txt
root:437394baff5aa33daa618be47b75cb49
```

The hash was an MD5 hash. After cracking it, the password was:

```txt
qwerty123@
```

Using these credentials on the `/admin` page revealed the flag:

```txt
Flag: d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff
```

## How I Discovered It

I started by enumerating directories and files on the web server with Gobuster:

```sh
sudo apt install gobuster
sudo snap install seclists
gobuster dir -u http://192.168.56.101/ \
  -w /usr/share/dirb/wordlists/common.txt \
  --exclude-length 975 \
  -x php,html,txt
```

```sh
===============================================================
[+] Url:                     http://192.168.56.101/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] Exclude Length:          975
[+] User Agent:              gobuster/3.6
[+] Extensions:              php,html,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/admin                (Status: 301) [Size: 193] [--> http://192.168.56.101/admin/]
/audio                (Status: 301) [Size: 193] [--> http://192.168.56.101/audio/]
/css                  (Status: 301) [Size: 193] [--> http://192.168.56.101/css/]
/errors               (Status: 301) [Size: 193] [--> http://192.168.56.101/errors/]
/favicon.ico          (Status: 200) [Size: 1406]
/fonts                (Status: 301) [Size: 193] [--> http://192.168.56.101/fonts/]
/images               (Status: 301) [Size: 193] [--> http://192.168.56.101/images/]
/includes             (Status: 301) [Size: 193] [--> http://192.168.56.101/includes/]
/index.php            (Status: 200) [Size: 6892]
/index.php            (Status: 200) [Size: 6892]
/js                   (Status: 301) [Size: 193] [--> http://192.168.56.101/js/]
/robots.txt           (Status: 200) [Size: 53]
/robots.txt           (Status: 200) [Size: 53]
/whatever             (Status: 301) [Size: 193] [--> http://192.168.56.101/whatever/]
Progress: 18456 / 18460 (99.98%)
===============================================================
Finished
===============================================================
```

```

Interesting results included:

```txt
/admin      (Status: 301)
/robots.txt (Status: 200)
/whatever   (Status: 301)
```

The `robots.txt` file is used to give crawling instructions to search engines, but it is public. It should not be used to hide sensitive paths.

Opening it showed:

```txt
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

The `/whatever` path was then visited manually.

## Exploitation Approach

Inside `/whatever`, I found an `htpasswd` file.

The file contained:

```txt
root:437394baff5aa33daa618be47b75cb49
```

This format means:

```txt
username: root
password hash: 437394baff5aa33daa618be47b75cb49
```

The hash is an MD5 hash.

After cracking the hash, the plaintext password was:

```txt
qwerty123@
```

So the recovered credentials were:

```txt
username: root
password: qwerty123@
```

These credentials were then used on:

```txt
http://192.168.56.101/admin
```

The application accepted the login and displayed the flag.

## Why This Is Vulnerable

There are multiple security problems in this breach:

1. A sensitive path was disclosed in `robots.txt`.
2. The `/whatever` directory was publicly accessible.
3. A password file was exposed to unauthenticated users.
4. The password hash used MD5, which is weak and easy to crack.
5. The password itself was weak.

The main issue is not Gobuster. Gobuster only helped discover what the server was already exposing.

The real vulnerability is sensitive information disclosure.

## Impact

An attacker can retrieve password hashes from the exposed file.

If the hash is weak or the password is common, the attacker can recover valid credentials and access restricted areas such as the admin page.

In this case, the exposed hash led directly to admin access.

## How To Prevent It

Recommended fixes:

- Never expose `.htpasswd`, password files, backups, or configuration files in the web root.
- Do not rely on `robots.txt` to hide sensitive paths.
- Disable directory listing.
- Restrict access to sensitive directories with server-side rules.
- Store secrets outside the public web directory.
- Use strong password hashing algorithms such as bcrypt, Argon2, or scrypt.
- Use strong, unique passwords.
- Monitor and alert on access to sensitive paths.
