# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 23:54:45 2022

@author: tyagi
"""

import requests
import pandas as pd
import urllib3
from lxml import html
from lxml import etree


#Fetch webpage from imbd
#Link : 
# 
search_list = []
for page in range(10000):
    print(page)
    if page == 0:url = "https://www.imdb.com/search/title/?title_type=feature&year=1800-01-01,2022-12-31&countries=in&sort=alpha,asc"
    else:
        url = f"https://www.imdb.com/search/title/?title_type=feature&year=1800-01-01,2022-12-31&countries=us&sort=alpha,asc&start={50*page+1}&ref_=adv_nxt"
    
    print("retrieving ", url)
    
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Host': 'www.imdb.com',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
                }
    
    response = requests.get(url, verify=False, headers=headers)
    print("parsing page")
    
    if response.status_code == 200:
        print("Success")
        parser = html.fromstring(response.text)
        root = html.fromstring(response.content)
        title = root.xpath('/html/body/div[2]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[1]/div[3]/h3/a') 
        listing = root.xpath('/html/body/div[2]/div/div[2]/div[3]/div[1]/div/div[3]')[0]
        for i in listing.iterchildren():
            for j in i.iterchildren():
                text = j.text_content().replace("\n",'').replace("  ","")
                text = text.replace('Rate this\xa0\xa0123456789107.9/10X\xa0','')
                text_list = [i.strip() for i in text.split('|')]
                search_list.append(text_list)
                print(text_list)
                
        
            




















