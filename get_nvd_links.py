#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 11:53:59 2019

@author: beileitang

scrap data from nvd json feed
"""

                      
#%%%
import requests
from bs4 import BeautifulSoup
import pandas as pd


def getHTML(url):
    r = requests.get(url)
    return r.content

def parseHTML(html):
    soup = BeautifulSoup(html,'html.parser')
 #   body = soup.body
  #  body_middle = soup.body.find('div',attrs={'class':'row'})
    table = soup.find('table',attrs={'class':'xml-feed-table'})
    tbody = table.find('tbody')
    
    des_name_list =[]
    
    for des_table_list in tbody.find_all('tr',{'class':'xml-feed-desc-row'}):
        des_name = des_table_list.get_text()
        des_name_list.append([des_name.encode('utf-8')])
    
    data_list =[]
    for data_table_list in tbody.find_all('tr',{'class':'xml-feed-data-row'}):        
        for data_link_list in data_table_list('td',{'class':'xml-file-type file-20'}):
            data_url = data_link_list.a['href']
            data_list.append([data_url.encode('utf-8')])
    return (des_name,data_list)

#%%
url='https://nvd.nist.gov/vuln/data-feeds#JSON_FEED'
html = getHTML(url)
parseHTML(html)
    

    

#%%
