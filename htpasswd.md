/robots.txt :

User-agent: *
Disallow: /whatever
Disallow: /.hidden

/whatever : htpasswd

root:437394baff5aa33daa618be47b75cb49
root:qwerty123@ reversed by md5

/admin : 

The flag is : d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

/.hidden : 

Demande à ton voisin de gauche  
Non ce n'est toujours pas bon ...
Demande à ton voisin du dessous 
Demande à ton voisin du dessus  
Demande à ton voisin de gauche  
Tu veux de l'aide ? Moi aussi ! 
...

That's a maze of nested directories each subfolder likely contains more subdirectories and eventually a README with the flag.
Crawling manually would take forever. Use crawler.py script :

> python3 crawler.py > result.txt

> grep "flag" result.txt 

Content: Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466

