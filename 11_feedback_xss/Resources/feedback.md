<b>test</b>

<script>alert(1)</script>

The flag is : 0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e

feedback input -> stored in page -> rendered without escaping -> browser treats it as HTML/JS

Prevention:

Escape user output with htmlspecialchars / HTML entity encoding.
Validate input server-side.
Use a CSP.
Never render feedback content as raw HTML.