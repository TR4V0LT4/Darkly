The application stores an authorization value in a client-side cookie:
```
I_am_admin=68934a3e9455fa72420237eb05902327
```

At first, the value looks random, but it is actually an MD5 hash.

When decoded/cracked:

```
68934a3e9455fa72420237eb05902327 => false
```

This means the server is using the cookie to decide whether the user is admin:

```
I_am_admin = false
```

The problem is that cookies are controlled by the client. If the server trusts this cookie directly, an attacker can modify it.

So we generate the MD5 hash of:
```
true
```

Result:

```
b326b5062b2f0e69046810717534cb09
```

Then we replace the cookie value:

```
I_am_admin=b326b5062b2f0e69046810717534cb09
```

After reloading the page, the application accepts the modified cookie and displays:

```
Good job! Flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3
```

Why This Is Vulnerable

The application trusts a client-side cookie for authorization.

Even though the value is hashed with MD5, this does not protect it. MD5 is fast, weak, and easy to crack for simple words like:

```
false
true
```

Also, hashing is not the same as signing. The server has no way to know whether the cookie was created by the application or modified by the user.

Impact

An attacker can escalate privileges from a normal user to admin by changing the cookie value.

How To Prevent It

- Never trust client-side cookies for authorization decisions.
- Store admin/session state server-side.
- Use secure session IDs instead of role values in cookies.
- If cookie data must contain state, sign it with an HMAC.
- Use strong cryptographic algorithms, not MD5.
- Mark cookies HttpOnly, Secure, and SameSite.
