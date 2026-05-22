import requests
from bs4 import BeautifulSoup

BASE_URL = "http://192.168.56.101/.hidden/"

def crawl(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    for link in soup.find_all("a"):
        href = link.get("href")
        
        # skip parent directory
        if not href or href == "../":
            continue
            
        # if it's a README, fetch and print it
        if href == "README":
            readme = requests.get(url + href).text.strip()
            if readme != "Nope" and readme:
                print(f"[FOUND] {url + href}")
                print(f"Content: {readme}\n")
                
        # if it's a directory, recurse into it
        elif href.endswith("/"):
            crawl(url + href)

crawl(BASE_URL)