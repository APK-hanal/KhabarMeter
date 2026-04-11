#im using Onlinekhabar's english version as the source of my news
import requests
from bs4 import BeautifulSoup
import time
import json
HEAD = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}
## Economy section
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


## Politics
        
def get_politics_links():
    link = "https://english.onlinekhabar.com/category/political"
    response = requests.get(link , headers= HEAD)
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find('div', class_ = "ok-details-content-left")
    heads = div.find_all('a',href = True)
    links = []
    for a_tag in heads:
        href = a_tag['href']
        if href.startswith("https://english.onlinekhabar.com/") and href.endswith('.html'):
            links.append(href)
    #remove duplicated values
    return list(set(links))

def politics_scrape(link):
    response = requests.get(link , headers= HEAD)
    response.encoding= 'utf-8'
    soup = BeautifulSoup(response.text , 'html.parser')
    # headers 
    header_div = soup.find('div' , class_ = 'ok-post-header')
    header = header_div.find('h1').text.strip()
    #body 
    body = ''
    body_div = soup.find('div',class_ = 'post-content-wrap')
    body_paragraphs = body_div.find_all('p')
    for bod in body_paragraphs:
        body += bod.text.strip()
        
    return {
        "link":link,
        'header': header,
        'body': body
    }
    
    
    
    
    
    



# Save to a json file UwU
def save_article(articles, file):
    with open(file , 'w',encoding = "utf-8") as f:
        json.dump(articles, f , ensure_ascii= False, indent = 2)
    
#Executive Block
if __name__ == "__main__":
    politics_links = get_politics_links()
    eco_link_list = get_eco_headerlinks()
    articles_eco = []
    articles_pol = []
    for link in eco_link_list:
        article = eco_scrape(link)
        articles_eco.append(article)
        time.sleep(1)
    for link in politics_links:
        article = politics_scrape(link)
        articles_pol.append(article)
        time.sleep(1)
    save_article(articles_eco,'data/economy.json')
    save_article(articles_pol,'data/politics.json')
    print("Yessirski data saved!!")        
    