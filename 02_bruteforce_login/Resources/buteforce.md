# Bruteforce Login

This breach is located in the login page of the Darkly web application.

The vulnerability is that the application allows many login attempts without rate limiting, account lockout, delay, CAPTCHA, or any other protection against bruteforce attacks.

By testing common passwords against the `admin` account, the correct credentials were found.

```txt
username: admin
password: shadow
```

After logging in with these credentials, the application displayed the flag.

## How I Discovered It

The login page accepts a username and password. Since this is a common attack surface, I tested whether the application had protections against repeated failed login attempts.

The first manual tests showed that wrong credentials simply returned a failure page, but the application did not block or slow down the requests.

That means an attacker can keep trying passwords until one works.

## Exploitation Approach

The idea was:

1. Use a known or likely username, such as `admin` or `user` .
2. Read passwords from a wordlist.
3. Send one login request per password.
4. Compare the server response.
5. Stop when the response is different from the normal failed login response.

The script does not exploit a technical parsing bug like SQL injection. It exploits weak authentication protection.

During failed login attempts, the application returns a response containing the failure marker. When the credentials are valid, the response changes, so the script can detect that the password was found.

## Result

The valid credentials were:

```txt
admin:shadow
```

Using these credentials on the login page gave access and revealed the flag.

## Why This Is Vulnerable

The application allows unlimited authentication attempts.

There is no:

- rate limiting
- account lockout
- exponential backoff
- CAPTCHA
- IP-based blocking
- alerting on repeated failed attempts
- strong password policy

The password is also weak because it appears in common wordlists.

## Impact

An attacker can discover valid credentials by trying many passwords.

If the targeted account is privileged, such as `admin`, the attacker can gain access to restricted functionality or sensitive information.

## How To Prevent It

The server should protect authentication endpoints against repeated guessing.

Recommended fixes:

- Add rate limiting per IP address and per account.
- Add temporary account lockout after too many failed attempts.
- Add exponential delay after repeated failures.
- Require strong passwords.
- Use multi-factor authentication for admin accounts.
- Log failed login attempts.
- Alert administrators about suspicious login behavior.
- Return generic login errors.

The main lesson is:

```txt
Authentication must be protected server-side. A login form that accepts unlimited guesses can be bruteforced.
```