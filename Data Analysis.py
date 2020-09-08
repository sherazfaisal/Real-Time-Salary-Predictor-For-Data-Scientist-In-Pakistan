# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 18:49:10 2020

@author: dell
"""


#Loading dependencies
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.util import bigrams
from nltk.collocations import *
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

#Loading Files
#Loading all the jobs with or without salary contained in the following file 
df_ws = pd.read_csv('F:/Data_Cleaned_NoSalary.csv', index_col=0)
#Loading all the jobs having salary contained in the following file 
df_os = pd.read_csv('F:/Data_Cleaned_OnlySalary.csv', index_col=0)

total_no_company=df_ws['Company'].nunique()
print('Total number of firms with data science job vacancies',total_no_company)

df_ws.drop_duplicates(subset=['Title','Company','Synopsis'],inplace = True)
len(df_ws)
df_ws.head()

ds_main_cities= pd.DataFrame(df_ws.groupby(['Location'])['Title'].count())
ds_main_cities.columns = ['Number of Jobs']
ds_main_cities = ds_main_cities.drop("None", axis=0)
ds_main_cities = ds_main_cities.sort_values(by=['Number of Jobs'],ascending=False)

# Set the width and height of the figure
plt.figure(figsize=(12,4))

plt.title("Number of Data Science Jobs in Each City", fontsize = 12)

ax = sns.barplot(x=ds_main_cities.index, y=ds_main_cities['Number of Jobs'])
ax.set_xticklabels(ds_main_cities.index, fontsize =12) 
ax.set_xlabel('City',fontsize=16, color='black')
ax.set_ylabel('Number of Jobs',fontsize=16) 

most_vacancies= pd.DataFrame(df_ws.groupby(['Company'])['Title'].count())
most_vacancies.columns = ['Vacancies']
most_vacancies = most_vacancies.sort_values(by=['Vacancies'],ascending=False)
#most_vacancy.head(35)
most_vacancies = most_vacancies.iloc[0:20]


# Fixing random state for reproducibility
np.random.seed(19680801)

plt.rcdefaults()
fig, ax = plt.subplots(figsize = (6,7))

# Example data
y_pos = np.arange(len(most_vacancies.index))
error = np.random.rand(len(most_vacancies.index))

ax.barh(y_pos, most_vacancies['Vacancies'], xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(most_vacancies.index)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Number of Vacancies', fontsize = 15)
ax.set_title('Top 20 Firms with most vacancies in Aug 2020', fontsize=20)

plt.show()

# Finding total number of unique roles in data science domain from the given dataset
total_no_roles=df_ws['Title'].nunique()
print('Total number of roles across all the firms',total_no_roles)

# most offered roles across all the firms
most_offd_roles=pd.DataFrame(df_ws.groupby(['Title'])['Synopsis'].count())
most_offd_roles.columns = ['Times it offered']
most_offd_roles = most_offd_roles.sort_values(by=['Times it offered'],ascending=False)
most_offd_roles = most_offd_roles.iloc[0:15]
#most_offd_roles = most_offd_roles.iloc[0:20] 
#print('Top 15 most wanted roles across firms',most_offd_roles)

sns.set_context("talk")
ax = sns.barplot(x=most_offd_roles['Times it offered'], y=most_offd_roles.index, data=most_offd_roles, orient='h', saturation=0.7)
ax.axes.set_title("Top 15 most wanted roles across firms", fontsize=20, y=1.01)
ax.set(xlabel='Times It Offered', ylabel='Roles')

#removing punctuations and stopwards
summary = df_ws['Synopsis']
summary = summary.apply(lambda x: " ".join(x.lower() for x in x.split()))
summary = summary.str.replace('[^\w\s]','')
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop = stopwords.words('english')
summary = summary.apply(lambda x: " ".join(x for x in x.split() if x not in stop))
freq = pd.Series(' '.join(summary).split()).value_counts()[:10]

ax = freq.plot.bar(figsize=(12,5))
plt.title("Common Words in Job Description", fontsize = 18)
ax.set_xlabel('Common Words',fontsize=14, color='black')
ax.set_ylabel('Number of occurences',fontsize=14)
ax.set_xticklabels(freq.index, fontsize =13, rotation = 0) 
plt.show()

most_offd_roles_by_salary=pd.DataFrame(df_os.groupby(['Title'])['avg_salary'].mean())
most_offd_roles_by_salary.columns = ['Average Salary(K)']
most_offd_roles_by_salary = most_offd_roles_by_salary.sort_values(by=['Average Salary(K)'],ascending=False)
most_offd_roles_by_salary = most_offd_roles_by_salary.iloc[0:35]
plt.figure(figsize=(12,20))
plt.title("Salaries of most wanted Roles in Data Science", fontsize = 22)
ax=sns.heatmap(data=most_offd_roles_by_salary, annot=True, fmt='g')
ax.set_ylabel('Roles',fontsize=16) 
plt.show()