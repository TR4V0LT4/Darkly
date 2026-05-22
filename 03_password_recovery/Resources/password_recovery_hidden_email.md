For the password recovery breach, the idea is usually not to “guess the reset code.” It is to notice that the reset form trusts a value controlled by the client.

Approach

Open the password recovery page and inspect the HTML source or DevTools. You should find a form with a hidden field, something like:

<input type="hidden" name="mail" value="webmaster@borntosec.com">
or another email value.

That hidden input is the weak point. Even though the browser does not show it normally, it is still sent in the HTTP request, and the user can modify it.

Why It Is Vulnerable

The application uses the email from the client-side form to decide where to send/reset the password.

That means the server is trusting this:

mail=webmaster@borntosec.com
But an attacker can change it to something else before submitting:

mail=attacker@example.com
So the server-side recovery logic is controlled by the attacker.
