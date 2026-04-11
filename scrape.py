#im using Onlinekhabar's english version as the source of my news
import requests
from bs4 import BeautifulSoup
import time
import json
HEAD = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# Get links from economy archives 
def get_eco_headerlinks():
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
#get headers and body content from the specific article
def eco_scrape(eco_link_list):
    response = requests.get(eco_link_list,headers=HEAD)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    #header
    head_div = soup.find('div', class_ ='ok-post-header')
    header = head_div.find('h1').text.strip()
    #body
    body = ""
    body_div = soup.find('div', class_= "post-content-wrap")
    for bodies in body_div.find_all('p'):
        body += bodies.text.strip()
    return {
        "link" :eco_link_list,
        "header" : header,
        "body" : body
    }

# Save to a json file UwU
def save_article(articles, file):
    with open(file , 'w',encoding = "utf-8") as f:
        json.dump(articles, f , ensure_ascii= False, indent = 2)
    
        
        

    
if __name__ == "__main__":
    eco_link_list = get_eco_headerlinks()
    articles = []
    for link in eco_link_list:
        article = eco_scrape(link)
        articles.append(article)
        time.sleep(1)
    save_article(articles,'data/economy.json')
    print("Yessirski data saved!!")        
    