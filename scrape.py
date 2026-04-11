#im using Onlinekhabar's english version as the source of my news
import requests
from bs4 import BeautifulSoup
import time
HEAD = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# Get links from economy archives 
def eco_headerlinks():
    link = "https://english.onlinekhabar.com/category/economy"
    response = requests.get(link,headers=HEAD)
    soup = BeautifulSoup(response.text ,"html.parser" )
    div = soup.find("div", class_= "ok-details-content-left")
    heads = div.find_all("a",href=True)
    links = []
    for a_tag in heads:
        href = a_tag['href']
        if href.startswith("https://english.onlinekhabar.com/") and href.endswith('.html'):
            links.append(href)
    #remove duplicate values
    return list(set(links))
    
    
if __name__ == "__main__":
    eco_headers = eco_headerlinks()
    