import requests
from bs4 import BeautifulSoup
import time
import json
from html import unescape
import sys

HEAD = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# Get links from archives 
def get_headerlinks_ok(link):
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

def get_headerlinks_kp(link):
    response = requests.get(link, headers= HEAD)
    soup = BeautifulSoup(response.text,'html.parser')
    div = soup.find('div', class_ ='block--morenews' )
    heads = div.find_all('a', href = True)
    links = []
    for a_tag in heads:
        href = a_tag['href']
        if href.startswith("/") and not href.startswith('/author/'):
            links.append(href)
    #Duplicates arise as the link is also present in the images of the article :>
    return list(set(links))
            
    
#get headers and body content from the specific article
def scrape_ok(link):
    try:
        response = requests.get(link,headers=HEAD,timeout= 10)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "html.parser")
        #header
        head_div = soup.find('div', class_ ='ok-post-header')
        header = unescape(head_div.find('h1').text.strip())
        #body
        body = ""
        body_div = soup.find('div', class_= "post-content-wrap")
        for bodies in body_div.find_all('p'):
            body += unescape(bodies.text.strip())
        return {
            "source":"Onlinekhabar",
            "link" :link,
            "header" : header,
            "body" : body
        }
    except Exception as e:
        print(f"Failed to scrape {link} due to : {e}")
        return None

def scrape_kp(link):
    try:
        response = requests.get(link,headers= HEAD)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text,'html.parser')
        head_div = soup.find('div', class_="col-sm-8")
        header = unescape(head_div.find('h1').text.strip())
        body = ''
        body_section = soup.find('section' ,class_="story-section")
        for bodies in body_section.find_all('p'):
            body += unescape(bodies.text.strip())
        return {
            "source":"The Kathmandu Post",
            "link":link,
            "header":header,
            "body":body
        }        
    except Exception as e:
        print("Error in scraping", e)

# Save to a json file UwU
def save_article(articles, file):
    with open(file , 'w',encoding = "utf-8") as f:
        json.dump(articles, f , ensure_ascii= False, indent = 2)
    
#Executive Block
if __name__ == "__main__":
    link = 'https://kathmandupost.com/money'
    f = get_headerlinks_kp(link)
    print(f[:2])
    sys.exit()
    eco_link ='https://english.onlinekhabar.com/category/economy'
    pol_link ='https://english.onlinekhabar.com/category/political'
    politics_links = get_headerlinks_ok(pol_link)
    eco_link_list = get_headerlinks_ok(eco_link)
    articles_eco = []
    articles_pol = []
    for link in eco_link_list:
        article = scrape_ok(link)
        if article:
            articles_eco.append(article)
        time.sleep(1)
    for link in politics_links:
        article = scrape_ok(link)
        if article:
            articles_pol.append(article)
        time.sleep(1)
    save_article(articles_eco,'data/economy.json')
    save_article(articles_pol,'data/politics.json')
    print("Yessirski data saved!!")        
    