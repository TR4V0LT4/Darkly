# Survey Tampering

## Summary

This breach is located in the survey page.

The application displays a survey form where the user can choose a value from a limited list.

The vulnerability is that the server trusts the value submitted by the client. By modifying the request manually, an attacker can send a value outside the allowed range and trigger the flag.

Final flag:

```txt
Flag: PUT_THE_FLAG_HERE
```

## How I Discovered It

The survey page contains form controls such as dropdowns or selectable values.

In the browser, the user can only select values provided by the HTML, for example:

```txt
1
2
3
4
5
6
7
8
9
10
```

However, these limits exist only in the frontend.

The browser sends a normal HTTP request to the server, and the attacker can modify that request before it reaches the backend.

## Exploitation Approach

The normal form sends a value such as:

```txt
sujet=2&valeur=10
```

Instead of submitting only allowed values, I changed the submitted value to something outside the expected range:

```txt
sujet=2&valeur=999999
```

Example request:

```bash
curl -i -X POST "http://192.168.56.101/index.php?page=survey" \
  -d "sujet=2&valeur=999999&submit=Submit"
```

The exact parameter names can be confirmed from the survey form source.

The important part is that the value sent to the server is modified manually instead of selected through the normal UI.

## DevTools Method

The same test can be done in the browser:

1. Open the survey page.
2. Right click the dropdown and inspect it.
3. Find an option such as:

```html
<option value="10">10</option>
```

4. Change the value to something invalid:

```html
<option value="999999">10</option>
```

5. Submit the form.

The displayed text may still look normal, but the submitted value is now attacker-controlled.

## Why This Is Vulnerable

The application relies on client-side restrictions to enforce valid survey values.

This is not secure because the client controls the request.

The server should not assume that a submitted value is valid just because the HTML page only showed valid choices.

Vulnerable logic:

```txt
Browser dropdown limits values to 1-10.
Server accepts whatever value is submitted.
Attacker sends 999999 manually.
```

Secure logic:

```txt
Browser dropdown limits values for usability.
Server validates that the submitted value is actually allowed.
```

## Impact

An attacker can manipulate survey results by submitting values that normal users cannot choose.

In a real application, this could affect:

- ratings
- votes
- scores
- prices
- quantities
- permissions
- any workflow that trusts client-side values

This is an example of broken server-side validation.

## How To Prevent It

Recommended fixes:

- Validate all submitted values on the server.
- Enforce allowed ranges server-side.
- Reject values outside the expected list.
- Do not trust hidden inputs, dropdowns, radio buttons, or disabled fields.
- Use server-side business rules for important decisions.
- Log suspicious values that are impossible through the normal UI.

Example validation:

```php
$allowedValues = range(1, 10);
$value = intval($_POST["valeur"] ?? 0);

if (!in_array($value, $allowedValues, true)) {
    http_response_code(400);
    exit("Invalid survey value");
}
```

The main lesson is:

```txt
Client-side controls are for user experience, not security. The server must validate every submitted value.
```
