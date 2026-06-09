# Darkly

Darkly is a web security project focused on finding and explaining vulnerabilities in a deliberately vulnerable web application.

The goal is not only to get the flags, but to understand each breach, explain the exploitation path, and describe how the issue should be fixed.

## Project Structure

Each breach is stored in its own folder:

```txt
{breach_name}/
├── flag
└── Resources/
    └── README.md
```

The `flag` file contains the final flag for that breach.

The `Resources/README.md` file explains:

- where the vulnerability is located
- how it was discovered
- the payload or request used
- why the vulnerability works
- the impact
- how to prevent it

## Breaches

```txt
01_admin_cookie
02_bruteforce_login
03_header_spoofing
04_unvalidated_redirect
05_survey_tampering
06_password_recovery_hidden_email
07_file_upload_mime_bypass
08_media_xss_data_uri
09_feedback_stored_xss
10_member_sql_injection
11_image_sql_injection
12_path_traversal
13_robots_htpasswd
14_hidden_directory_file_discovery
```

## Main Topics Covered

- Cookie tampering
- Bruteforce protection bypass
- HTTP header spoofing
- Unvalidated redirects
- Client-side value tampering
- Password recovery logic flaws
- File upload validation bypass
- Cross-site scripting
- SQL injection
- Path traversal
- Sensitive file exposure
- Directory discovery

## Notes

No automated exploitation tools such as `sqlmap` were used.

When scripts are included, they are small, custom, and used only to demonstrate or reproduce a specific manual finding.

The important part of the project is being able to explain each vulnerability clearly during evaluation.

## Security Lessons

User input must never be trusted directly.

Security decisions must be enforced server-side.

Client-side controls, hidden fields, cookies, headers, MIME types, and URL parameters can all be modified by an attacker.

Proper fixes include prepared statements, strict server-side validation, output escaping, secure session handling, allowlists, safe file upload handling, and least-privilege access.
