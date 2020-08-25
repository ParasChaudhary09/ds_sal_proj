# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 23:51:22 2020

@author: Ken & Paras 
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

#Salary Parsing

df = df[df['Salary Estimate'] != '-1']


df['Hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['Employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)



salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_dollar = salary.apply(lambda x: x.replace('K','').replace('$',''))
minus_hr = minus_dollar.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['Min_Salary'] = minus_hr.apply(lambda x: int(x.split('-')[0]))
df['Max_Salary'] = minus_hr.apply(lambda x: int(x.split('-')[1]))
df['Avg_Salary'] = (df.Max_Salary + df.Min_Salary) / 2

#Company Name

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

#Job State

df['Job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.Job_state.value_counts()


#Headquarters

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#ageOfComapny

df['age_of_company'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)

# Parsing the job description

df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python.value_counts()

df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

df['R'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R.value_counts()

df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

df['SQL'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df.SQL.value_counts()

df['devops'] = df['Job Description'].apply(lambda x: 1 if 'devops' in x.lower() else 0)
df.devops.value_counts()

df['tensorflow'] = df['Job Description'].apply(lambda x: 1 if 'tensorflow' in x.lower() else 0)
df.tensorflow.value_counts()

df['ml'] = df['Job Description'].apply(lambda x: 1 if 'machine learning' in x.lower() else 0)
df.ml.value_counts()

df['dl'] = df['Job Description'].apply(lambda x: 1 if 'deep learning' in x.lower() else 0)
df.dl.value_counts()

df['tableau'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
df.tableau.value_counts()

df['datawrangling'] = df['Job Description'].apply(lambda x: 1 if 'data wrangling' in x.lower() else 0)
df.datawrangling.value_counts()

df['cloudcomputing'] = df['Job Description'].apply(lambda x: 1 if 'cloud computing' in x.lower() else 0)
df.cloudcomputing.value_counts()

df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

df['databasemanagement'] = df['Job Description'].apply(lambda x: 1 if 'database management' in x.lower() else 0)
df.databasemanagement.value_counts()

df['hadoop'] = df['Job Description'].apply(lambda x: 1 if 'hadoop' in x.lower() else 0)
df.hadoop.value_counts()


df['communication'] = df['Job Description'].apply(lambda x: 1 if 'communication' in x.lower() else 0)
df.communication.value_counts()

df_out = df.drop(['Unnamed: 0'], axis = 1)
df_out.to_csv('salary_data_cleaned.csv',index = False)
