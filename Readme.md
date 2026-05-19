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
