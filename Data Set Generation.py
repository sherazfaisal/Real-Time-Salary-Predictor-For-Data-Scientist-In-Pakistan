# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 16:53:08 2020

@author: dell
"""
import urllib
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import re

url_template= 'https://pk.indeed.com/jobs?q={}+&l={}'


max_results_per_city = 500 
df = pd.DataFrame()
results = []
df_more = pd.DataFrame(columns=["Title","Location","Company","Salary", "Synopsis"])
for city in set(['Karachi', 'Lahore', 'Islamabad', 'Peshawar', 'Quetta', 
    'Bhawalpur', 'Faisalabad', 'Rawalpindi', 'Multan', 'Abbottabad']):
    for search in set(['Data+Scientist','Data+Analyst','Data+Engineer','Business+Analyst','Data+Administrator']):
        url = url_template.format(search,city)
        # Append to the full set of results
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'html.parser', from_encoding="utf-8")
        for each in soup.find_all(class_= "result" ):
            try: 
                title = each.find(class_='jobtitle').text.replace('\n', '')
            except:
                title = 'None'
            try:
                location = each.find('span', {'class':"location" }).text.replace('\n', '')
            except:
                location = 'None'
            try: 
                company = each.find(class_='company').text.replace('\n', '')
            except:
                company = 'None'
            try:
                salary = each.find('span', {'class':'no-wrap'}).text.replace('\n','')
            except:
                salary = 'None'
            try:
                synopsis = each.find('ul',{'style':'list-style-type:circle;margin-top: 0px;margin-bottom: 0px;padding-left:20px;'}).text.replace('\n', '')
            except:
                synopsis = 'None'    
            df = df.append({'Title':title, 'Location':location, 'Company':company, 'Salary':salary, 'Synopsis':synopsis}, ignore_index=True)



