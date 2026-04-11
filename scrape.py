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
    links = soup.find_all("a",href=True)
    for a_tag in links:
        print(a_tag.text)
        time.sleep(1)    
    
    
    
    
if __name__ == "__main__":
    eco_headerlinks()