from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pandas as pd
import time
from get_nft import get_nft
import qrcode
with open("links.txt") as f:
    lines = f.readlines()

links = [x.rstrip("\n") for x in lines if "https" in x]
links = [x.rstrip("/") for x in lines if "https" in x]
results = []


chrome_options = Options()
chrome_options.add_argument("--headless")
#chrome_options.add_argument("--no-sandbox") # linux only
userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.56 Safari/537.36"
chrome_options.add_argument(f'user-agent={userAgent}')

browser = webdriver.Chrome(options=chrome_options)

time.sleep(20)


for l in links:
    print("Scrapping {}".format(l))
    if("opensea" in l):
        results.append(get_nft("opensea",l,browser))
    '''if("rarible" in l):
        results.append(get_nft("rarible",l,browser))
    if("makersplace" in l):
        results.append(get_nft("makersplace",l,browser))
    if("fountadion" in l):
        results.append(get_nft("get_nft",l,browser))'''


df = pd.DataFrame(results)

df.to_csv("nfts.csv")
