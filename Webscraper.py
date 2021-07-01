
import requests
from bs4 import BeautifulSoup
from openpyxl.workbook import Workbook

import pandas as pd

url = 'https://leetcode.com/problemset/all/'

r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')

tag_list = []

tag_summary = soup.find_all('a', { 'class': 'inline-flex items-center'})

#print(tag_summary)


for tagitem in tag_summary:
  taginfo = {
  'tag': tagitem.find_all('span')[0].text,
  'number' : int(tagitem.find_all('span')[1].text)
  }
  tag_list.append(taginfo)
  
  


df = pd.DataFrame(tag_list)
df.to_csv('tagList.csv')












