1. SQL Injection but check other forms too (login, member search)
2. XSS (Cross-Site Scripting)
3. File Upload — if there's an upload form, try uploading a .php file disguised as an image.
4. CSRF — look for forms without tokens.
5. Insecure Direct Object Reference — tamper with IDs, cookies, hidden fields.
6. Sensitive data exposure — check robots.txt, .htpasswd, page source comments.


Tools to learn alongside (manual first!)
Since sqlmap is forbidden, learn the manual approach then use these for understanding:

Burp Suite Community — intercept and modify requests, the most important tool
curl — craft raw HTTP requests
gobuster/dirb — discover hidden directories

bashdirb http://172.16.60.128/


5 XSS on feedback formtry <script>alert(1)</script>
6 XSS on image searchsame idea different field
7 File inclusion / path traversallook for ?page= in URLs
8 File upload exploitupload a PHP as image
9 Open redirecttamper with redirect URLs
10 CSRFforms without tokens 
12 Admin panel exposuretry /admin /administrator
13 Sensitive data in sourcecheck page source comments
14 HTTP header manipulationcheck Referer, User-Agent