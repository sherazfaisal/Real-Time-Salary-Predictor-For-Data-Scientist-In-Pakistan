# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 12:36:33 2020

@author: dell
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
le = preprocessing.LabelEncoder()
#Loading all the jobs with or without salary contained in the following file 
df_ws = pd.read_csv('F:/Data_Cleaned_NoSalary.csv', index_col=0)
#Loading all the jobs having salary contained in the following file 
df_os = pd.read_csv('F:/Data_Cleaned_OnlySalary.csv', index_col=0)
# Get list of categorical variables
object_cols = ['Title','Location','Company']
# Make copy to avoid changing original data 
label_X_ws = df_ws.copy()
label_X_os = df_os.copy()
for col in object_cols:
    label_X_ws[col] = le.fit_transform(df_ws[col])
    label_X_os[col] = le.transform(df_os[col])
X_os = label_X_os.drop('Salary', axis =1)
X_os = X_os.drop('Synopsis', axis =1)
X_os = X_os.drop('min_salary', axis =1)
X_os = X_os.drop('max_salary', axis =1)
X_os = X_os.drop('avg_salary', axis =1)
y = label_X_os['avg_salary']
forest_model = RandomForestRegressor(n_estimators=100,random_state=1)
forest_model.fit(X_os, y)
X_ws = label_X_ws.drop('Salary', axis =1)
X_ws = X_ws.drop('Synopsis', axis =1)
melb_preds = forest_model.predict(X_ws)
df_ws['Predicted_Salary'] = pd.DataFrame(melb_preds*1000)
df_ws['Predicted_Salary'] = df_ws['Predicted_Salary'].apply(lambda x: int(x))

pred_salary = df_ws.drop('analysis_yn', axis =1)
pred_salary = pred_salary.drop('models_yn', axis =1)
pred_salary = pred_salary.drop('software_yn', axis =1)
pred_salary = pred_salary.drop('sales_yn', axis =1)
pred_salary = pred_salary.drop('security_yn', axis =1)
pred_salary = pred_salary.drop('marketing_yn', axis =1)
pred_salary = pred_salary.drop('experience_yn', axis =1)

