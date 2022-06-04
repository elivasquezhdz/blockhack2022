from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import time
from get_nft import get_nft
import qrcode
with open("links.txt") as f:
    lines = f.readlines()

links = [x.rstrip("\n") for x in lines if "https" in x]
results = []

browser = webdriver.Chrome()

time.sleep(20)


for l in links:
    if("opensea" in l):
        results.append(get_nft("opensea",l,browser))
    '''if("rarible" in l):
        results.append(get_nft("rarible",l,browser))
    if("makersplace" in l):
        results.append(get_nft("makersplace",l,browser))
    if("fountadion" in l):
        results.append(get_nft("get_nft",l,browser))'''


df = pd.DataFrame(results)

df.to_csv("nfts_.csv")
