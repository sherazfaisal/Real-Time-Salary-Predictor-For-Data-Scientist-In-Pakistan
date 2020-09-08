

import urllib
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import re

url= 'https://pk.indeed.com/jobs?q=Data+Scientist+&l=Lahore'



def parse(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser', from_encoding="utf-8")
    df = pd.DataFrame(columns=["Title","Location","Company","Salary", "Synopsis"])
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
    return df

df= parse(url)

df.head()
    
# max_results_per_city = 2000 
# i = 0
#  df_ = pd.DataFrame()
# results = []
# df_more = pd.DataFrame(columns=["Title","Location","Company","Salary", "Synopsis"])
# for city in set(['Karachi', 'Lahore', 'Islamabad', 'Peshawar', 'Quetta', 
#     'Bhawalpur', 'Faisalabad', 'Rawalpindi', 'Multan', 'Abbottabad']):
#     for start in range(0, max_results_per_city, 10):
#         # append the city in url
#         url = url_template.format(city, start)
#         # now, add the dataframes of everycity in dataframe
#         df = parse(url)
#         df_more = df_.append({'Title':df[title], 'Location':df[location], 'Company':df[company], 'Salary':df[salary], 'Synopsis':df[synopsis]}, ignore_index=True)
        