# Password Recovery Hidden Email


This breach is located in the password recovery page of the Darkly web application.
The vulnerability is that the application trusts an email value sent by the client during the password recovery process.
Because the server accepts the modified value, the password recovery logic is controlled by the attacker.

## How I Discovered It

I opened the password recovery page and inspected the HTML source / browser DevTools.

The form contained a hidden input field similar to:

```html
<input type="hidden" name="mail" value="webmaster@borntosec.com">
```

Even though this field is hidden from the normal page view, it is still part of the HTML and is still sent in the HTTP request.

Hidden fields are not secure. A user can modify them with browser DevTools, an intercepting proxy, or a manual HTTP request.

## Exploitation Approach

The normal request sends:

```txt
mail=webmaster@borntosec.com
```

I changed the value to another email address:

```txt
mail=attacker@example.com
```

Then I submitted the form again.

This showed that the backend was trusting the email address provided by the client instead of choosing the recovery email from trusted server-side data.

## Example Request

```bash
curl -i -X POST "http://192.168.56.101/index.php?page=recover" \
  -d "mail=attacker@example.com&Submit=Submit"
```

The exact parameter names may vary depending on the form source, but the important part is the modified `mail` value.

## Result

After changing the email value and submitting the request, the application accepted the modified recovery target and revealed the flag.

```txt
Flag: df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3
```

## Why This Is Vulnerable

The application makes a security decision based on client-controlled data.

The server should not trust this:

```txt
mail=webmaster@borntosec.com
```

because the attacker controls the request and can change it to:

```txt
mail=attacker@example.com
```

The mistake is assuming that a hidden HTML input is protected. Hidden inputs only hide data from the visual interface. They do not prevent modification.

## Impact

In a real application, this kind of vulnerability could allow an attacker to redirect password recovery actions to an email address they control.

Depending on the implementation, this could lead to account takeover.

## How To Prevent It

The password recovery process must be controlled server-side.

Recommended fixes:

- Do not store trusted recovery email addresses in hidden form fields.
- Do not let the client decide the recovery destination.
- The server should retrieve the account email from the database.
- Use secure, random, single-use password reset tokens.
- Expire reset tokens after a short time.
- Store reset tokens hashed server-side.
- Do not reveal whether an email exists in the system.
- Rate-limit password recovery requests.
- Log and alert on suspicious recovery attempts.
