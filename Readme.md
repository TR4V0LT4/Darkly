# INSPECTING IP USING GO BUSTER:
sudo apt install gobuster
sudo snap install seclists

> gobuster dir -u http://192.168.56.101/ -w /usr/share/dirb/wordlists/common.txt --exclude-length 975 -x php,html,txt

```sh
===============================================================
[+] Url:                     http://192.168.56.101/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] Exclude Length:          975
[+] User Agent:              gobuster/3.6
[+] Extensions:              php,html,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/admin                (Status: 301) [Size: 193] [--> http://192.168.56.101/admin/]
/audio                (Status: 301) [Size: 193] [--> http://192.168.56.101/audio/]
/css                  (Status: 301) [Size: 193] [--> http://192.168.56.101/css/]
/errors               (Status: 301) [Size: 193] [--> http://192.168.56.101/errors/]
/favicon.ico          (Status: 200) [Size: 1406]
/fonts                (Status: 301) [Size: 193] [--> http://192.168.56.101/fonts/]
/images               (Status: 301) [Size: 193] [--> http://192.168.56.101/images/]
/includes             (Status: 301) [Size: 193] [--> http://192.168.56.101/includes/]
/index.php            (Status: 200) [Size: 6892]
/index.php            (Status: 200) [Size: 6892]
/js                   (Status: 301) [Size: 193] [--> http://192.168.56.101/js/]
/robots.txt           (Status: 200) [Size: 53]
/robots.txt           (Status: 200) [Size: 53]
/whatever             (Status: 301) [Size: 193] [--> http://192.168.56.101/whatever/]
Progress: 18456 / 18460 (99.98%)
===============================================================
Finished
===============================================================
```



<!--
Voila un peu de lecture :

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.


-->

<!-- 

Fun right ?
source: loem.
Good bye  !!!!

-->

<!--
You must come from : "https://www.nsa.gov/".
-->

<!--
Where does it come from?
Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.


-->
