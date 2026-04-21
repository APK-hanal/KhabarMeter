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
            links.append(f"https://kathmandupost.com{href}")
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
    eco_articles = []
    pol_articles = []
    #The Kathmandu Post
    kp_eco_link = 'https://kathmandupost.com/money'
    kp_eco_link_list = get_headerlinks_kp(kp_eco_link)
    kp_pol_link = 'https://kathmandupost.com/politics'
    kp_pol_link_list = get_headerlinks_kp(kp_pol_link)
    for kp_link_eco in kp_eco_link_list:
        kp_article_eco = scrape_kp(kp_link_eco)
        if kp_article_eco:
            eco_articles.append(kp_article_eco)
        time.sleep(1)
    for kp_link_pol in kp_pol_link_list:
        kp_article_pol = scrape_kp(kp_link_pol)
        if kp_article_pol:
            pol_articles.append(kp_article_pol)
        time.sleep(1)
    # OnlineKhabar as ok
    ok_eco_link ='https://english.onlinekhabar.com/category/economy'
    ok_pol_link ='https://english.onlinekhabar.com/category/political'
    ok_politics_links = get_headerlinks_ok(ok_pol_link)
    ok_eco_link_list = get_headerlinks_ok(ok_eco_link)
    for ok_link in ok_eco_link_list:
        ok_article_eco = scrape_ok(ok_link)
        if ok_article_eco:
            eco_articles.append(ok_article_eco)
        time.sleep(1)
    for ok_link in ok_politics_links:
        ok_article_pol = scrape_ok(ok_link)
        if ok_article_pol:
            pol_articles.append(ok_article_pol)
        time.sleep(1)
    save_article(eco_articles,'data/economy.json')
    save_article(pol_articles,'data/politics.json')
    print("Yessirski data saved!!")        
    