/robots.txt :

User-agent: *
Disallow: /whatever
Disallow: /.hidden

/whatever : htpasswd

root:437394baff5aa33daa618be47b75cb49
root:qwerty123@ reversed by md5

/.hidden : 

Demande à ton voisin de gauche  
Non ce n'est toujours pas bon ...
Demande à ton voisin du dessous 
Demande à ton voisin du dessus  
Demande à ton voisin de gauche  

Tu veux de l'aide ? Moi aussi !  

That's a maze of nested directories each subfolder likely contains more subdirectories and eventually a README with the flag.
Crawling manually would take forever. Use this script:

Downloading data:
wget -r -np http://192.168.56.101/.hidden/