from styleframe import StyleFrame
from typing import Text
import test
import pandas as pd
from openpyxl.workbook import Workbook
from webdriver_manager.driver import Driver
import sys



def ConvertProblemDoc(tag):
  tag = tag.replace(" ","-")
  url = f'https://leetcode.com/tag/{tag}/'
  test.driver.get(url)
  test.time.sleep(5)
  content = test.driver.page_source.encode('utf-8').strip()

  soup = test.BeautifulSoup(content,'html.parser')

  q = soup.find('tbody',{'class':'reactable-data'}).find_all('tr')

  test.driver.quit()


  question_list = []

  for element in q:
    link = "https://leetcode.com" + element.find('td',{'label':'Title'}).find('a')['href']
    question_attr = {
    'Problem Link' : '=HYPERLINK("{}", "{}")'.format(link, link),
    'Problem Title' : element.find('td',{'label':'Title'}).find('a').text,
    'Acceptance' : element.find('td',{'label':'Acceptance'}).text,
    'Difficulty' : element.find('td',{'label':'Difficulty'}).text,
    }
    question_list.append(question_attr)

  df = pd.DataFrame(question_list)
  
  
  
  

  df.to_excel(f"ProblemSet__{tag}.xlsx")

  



  



argument = ""

length = len(sys.argv)

for i in range(1,length):
  argument += sys.argv[i]
  if i!=length-1:
    argument += " "


ConvertProblemDoc(argument)












