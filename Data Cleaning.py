# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 13:25:27 2020

@author: dell
"""


import pandas as pd


df_more = pd.read_csv('F://DataSet_Not_Cleaned.csv')
df_more.drop('Unnamed: 0', axis=1, inplace=True)

print (df_more.head())
print (df_more.shape)
print (df_more[df_more.Salary != 'None'].shape)
df_more2 = df_more[df_more.Salary != 'None'].drop_duplicates().dropna()
print (df_more2.shape)

df_more = df_more.drop_duplicates().dropna()

df_more2['Salary'] =df_more2['Salary'].apply(lambda x: x.split(' a')[0])
df_more2['Salary'] = df_more2['Salary'].apply(lambda x:x.replace('Rs ',''))
df_more2['Salary'] = df_more2['Salary'].apply(lambda x:x.replace(' ',''))
df_more2['Salary'] = df_more2['Salary'].apply(lambda x:x.replace(',',''))

df_more2 = df_more2.join(df_more2['Salary'].str.split('-', 1, expand=True).rename(columns={0:'min_salary', 1:'max_salary'}))
df_more2['min_salary'] = (df_more2['min_salary'].astype('float64')/1000)
df_more2['max_salary'] = (df_more2['max_salary'].astype('float64')/1000)
df_more2['avg_salary'] = (df_more2.min_salary + df_more2.max_salary)/2
df_more2['max_salary'] = df_more2['max_salary'].fillna(df_more2['min_salary'])
df_more2['avg_salary'] = df_more2['avg_salary'].fillna(df_more2['min_salary'])


def parse_synopsis(df_more2=df_more2):
    #parse data by the type of job
    #data analysis/analyst/reports/business intelligence
    df_more2['analysis_yn'] = df_more2['Synopsis'].apply(lambda x: 1 if 'data analysis' in x.lower() or 'analyst' in x.lower() or 'report' in x.lower() or 'business intelligence' in x.lower() else 0)
    df_more2.analysis_yn.value_counts()
    #dota models/data scientist
    df_more2['models_yn'] = df_more2['Synopsis'].apply(lambda x: 1 if 'data models' in x.lower() or 'data scientist' in x.lower() or 'models' in x.lower() else 0)
    df_more2.models_yn.value_counts()
    #software developers/software engineer
    df_more2['software_yn'] = df_more2['Synopsis'].apply(lambda x: 1 if 'software developers' in x.lower() or 'software engineer' in x.lower() else 0)
    df_more2.software_yn.value_counts()
    #parse data by the type of department
    #sales
    df_more2['sales_yn'] = df_more2['Synopsis'].apply(lambda x: 1 if 'sales' in x.lower() else 0)
    df_more2.sales_yn.value_counts()
    #security
    df_more2['security_yn'] = df_more2['Synopsis'].apply(lambda x: 1 if 'security' in x.lower() else 0)
    df_more2.security_yn.value_counts()
    #marketing
    df_more2['marketing_yn'] = df_more2['Synopsis'].apply(lambda x: 1 if 'marketing' in x.lower() else 0)
    df_more2.marketing_yn.value_counts()
    #experience
    df_more2['experience_yn'] = df_more2['Synopsis'].apply(lambda x: 1 if 'experience' in x.lower() else 0)
    df_more2.experience_yn.value_counts()
    
parse_synopsis(df_more2)
parse_synopsis(df_more)
df_more2 = df_more2.reset_index(drop=True)
df_more = df_more.reset_index(drop=True)
df_more2.to_csv('F://Data_Cleaned_OnlySalary.csv' , encoding='utf-8')
df_more.to_csv('F://Data_Cleaned_NoSalary.csv' , encoding='utf-8')
