dirb http://192.168.56.101//

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Sat May 16 21:06:29 2026
URL_BASE: http://192.168.56.101//
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://192.168.56.101// ----
+ http://192.168.56.101//admin (CODE:301 SIZE:193)                                                                                                                                                                                                        
+ http://192.168.56.101//audio (CODE:301|SIZE:193)                                                                                                                                                                                                        
+ http://192.168.56.101//css (CODE:301|SIZE:193)                                                                                                                                                                                                          
+ http://192.168.56.101//errors (CODE:301|SIZE:193)                                                                                                                                                                                                       
+ http://192.168.56.101//favicon.ico (CODE:200|SIZE:1406)                                                                                                                                                                                                 
+ http://192.168.56.101//fonts (CODE:301|SIZE:193)                                                                                                                                                                                                        
+ http://192.168.56.101//images (CODE:301|SIZE:193)                                                                                                                                                                                                       
+ http://192.168.56.101//includes (CODE:301|SIZE:193)                                                                                                                                                                                                     
+ http://192.168.56.101//index.php (CODE:200|SIZE:6892)                                                                                                                                                                                                   
+ http://192.168.56.101//js (CODE:301|SIZE:193)                                                                                                                                                                                                           
+ http://192.168.56.101//robots.txt (CODE:200|SIZE:53)                                                                                                                                                                                                    
+ http://192.168.56.101//whatever (CODE:301|SIZE:193)                                                                                                                                                                                                     
                                                                                                                                                                                                                                                          
-----------------
END_TIME: Sat May 16 21:06:34 2026
DOWNLOADED: 4612 - FOUND: 12

------------------------------------------------------------------------------------

# USING GO BUSTER:
sudo apt install gobuster
sudo snap install seclists

> gobuster dir -u http://192.168.56.101/ -w /usr/share/dirb/wordlists/common.txt --exclude-length 975

gobuster dir -u http://192.168.56.101/ -w /usr/share/dirb/wordlists/common.txt --exclude-length 975 -x php,html,txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
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