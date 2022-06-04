from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
def get_nft(marketplace,url,browser):
    browser.get(url)
    html = browser.page_source
    soup = bs(html, 'html.parser')
    time.sleep(5)
    #print(html)

    if(marketplace == "opensea"):
        description = ""
        nft = soup.find_all("img", {"class": "Image--image"})

        if(len(nft) == 0):
            nft = soup.find_all("video", {"class": "AssetMedia--video"})[0]
            nft = nft.children.__next__()['src']
        else:
            nft = nft[0]['src']
        title = soup.find_all("h1", {"class": "sc-1xf18x6-0 hDbqle item--title"})[0].text
        if(len(soup.find_all("div", {"class": "sc-1xf18x6-0 hDbqle item--description-text"}))>0):
            description = soup.find_all("div", {"class": "sc-1xf18x6-0 hDbqle item--description-text"})[0].text

        collection = soup.find_all("div",{"class":"sc-1xf18x6-0 hDbqle"})[0].text
        creator_link =  soup.find_all("a",{"class":"sc-1pie21o-0 hmVtez sc-1xf18x6-0 FNmrM AccountLink--ellipsis-overflow"})[0]['href']


        browser.get("https://opensea.io" + creator_link)
        time.sleep(10)
        html = browser.page_source
        soup = bs(html, 'html.parser')
        profile_pic = soup.find_all("img",{"class":"sc-ya60av-0 koxJAZ"})[0]['src']

        values = { "nft":nft, "title":title,"description":description,"collection":collection, \
                "creator_link":creator_link,"profile_pic":profile_pic

        }
        return values
    if(marketplace == "rarible"):
        pass
    if(marketplace == "makersplace"):
        pass
    if(marketplace == "fountadion"):
        pass