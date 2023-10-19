#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Q1. Pearson correlation coefficient is a measure of the linear relationship between two variables. Suppose
you have collected data on the amount of time students spend studying for an exam and their final exam
scores. Calculate the Pearson correlation coefficient between these two variables and interpret the result."""


# In[2]:


# importing lib for furthere refrence

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


data = {
    'Study Time (hours)': [10, 8, 6, 12, 14, 5, 7, 9, 11, 13],
    'Exam Score (out of 100)': [75, 80, 60, 90, 95, 65, 70, 85, 75, 92]
}

# Create a DataFrame
df = pd.DataFrame(data)


# In[5]:


df.head(2)


# In[6]:


## covariance 
covariance =df['Study Time (hours)'].cov(df[ 'Exam Score (out of 100)'])


# In[7]:


std_study_time = df['Study Time (hours)'].std()
std_exam_score = df['Exam Score (out of 100)'].std()
correlation = covariance /std_study_time*std_exam_score


# In[8]:


correlation ## here we got the correlation


# In[9]:


"""Q2. Spearman's rank correlation is a measure of the monotonic relationship between two variables.
Suppose you have collected data on the amount of sleep individuals get each night and their overall job
satisfaction level on a scale of 1 to 10. Calculate the Spearman's rank correlation between these two
variables and interpret the result."""


# In[18]:


data1 = {
    'Hours of Sleep': [7, 6, 8, 5, 6, 7, 9, 5, 8, 7],
    'Job Satisfaction': [8, 7, 9, 6, 7, 8, 9, 6, 7, 8]
}
df1 = pd.DataFrame(data1)
df1.head()


# In[23]:


import pandas as pd
from scipy.stats import spearmanr

data1 = {
    'Hours of Sleep': [7, 6, 8, 5, 6, 7, 9, 5, 8, 7],
    'Job Satisfaction': [8, 7, 9, 6, 7, 8, 9, 6, 7, 8]
}
df1 = pd.DataFrame(data1)

# Calculate Spearman's rank correlation
spearman_corr, p_value = spearmanr(df1['Hours of Sleep'], df1['Job Satisfaction'])

print(f"Spearman's Rank Correlation Coefficient: {spearman_corr}")
print(f"P-value: {p_value}")


# In[24]:


"""Q3. Suppose you are conducting a study to examine the relationship between the number of hours of
exercise per week and body mass index (BMI) in a sample of adults. You collected data on both variables
for 50 participants. Calculate the Pearson correlation coefficient and the Spearman's rank correlation
between these two variables and compare the results."""


# In[25]:


data = {
    'Hours_of_Exercise': [3, 4, 2, 5, 6, 3, 7, 4, 5, 6],
    'BMI': [29.1, 28.5, 30.2, 27.8, 26.5, 29.8, 25.9, 28.3, 27.6, 26.9]
}
df2 = pd.DataFrame(data)


# In[26]:


df2.head(2)


# In[28]:


## covariance 
covariance =df2['Hours_of_Exercise'].cov(df2[ 'BMI'])


# In[29]:


std_data_1 = df2['Hours_of_Exercise'].std()
std_data_2 = df2['BMI'].std()


# In[30]:


correlation = covariance/std_data_1*std_data_2


# In[32]:


correlation ## here is the person correlation cofficient


# In[34]:


data = {
    'Hours_of_Exercise': [3, 4, 2, 5, 6, 3, 7, 4, 5, 6],
    'BMI': [29.1, 28.5, 30.2, 27.8, 26.5, 29.8, 25.9, 28.3, 27.6, 26.9]
}
df2 = pd.DataFrame(data)
# Calculate Spearman's rank correlation
spearman_corr, p_value = spearmanr(df2['Hours_of_Exercise'], df2['BMI'])

print(f"Spearman's Rank Correlation Coefficient: {spearman_corr}")
print(f"P-value: {p_value}")


# In[35]:


"""Q4. A researcher is interested in examining the relationship between the number of hours individuals
spend watching television per day and their level of physical activity. The researcher collected data on
both variables from a sample of 50 participants. Calculate the Pearson correlation coefficient between
these two variables."""


# In[36]:


data = {
    'Hours_of_TV': [3, 2, 4, 5, 1, 6, 2, 4, 3, 2],
    'Physical_Activity_Level': [2, 3, 1, 1, 4, 1, 3, 2, 2, 3]
}
df3 = pd.DataFrame(data)
## finding covariance here
covariance = df3['Hours_of_TV'].cov(df3['Physical_Activity_Level'])
## finding stad deviation
std_data1 = df3['Hours_of_TV'].std()
std_data2 = df3['Physical_Activity_Level'].std()
##finding correlation
correlation = covariance/std_data1*std_data2


# In[37]:


correlation


# In[39]:


"""Q5. A survey was conducted to examine the relationship between age and preference for a particular
brand of soft drink."""


# In[45]:


data = {
    'age':[25,42,37,19,31,28],
    'Soft drink Preference':['coke','pepsi','mountain dew' ,'coke', 'pepsi','coke']
}
df4 = pd.DataFrame(data)
##finding covariance
df4['Soft drink Preference'] = df4['Soft drink Preference'].map({'coke':1,'pepsi':2,'mountain dew':3})
covariance = df4['age'].cov(df4['Soft drink Preference'])
## finding stad deviation
std_data1 = df4['age'].std()
std_data2 = df4['Soft drink Preference'].std()
##finding correlation
correlation = covariance/std_data1*std_data2


# In[46]:


correlation


# In[47]:


"""Q6. A company is interested in examining the relationship between the number of sales calls made per day
and the number of sales made per week. The company collected data on both variables from a sample of
30 sales representatives. Calculate the Pearson correlation coefficient between these two variables."""


# In[48]:


data = {
    'Sales_Calls_Per_Day': [30, 25, 35, 20, 40, 32, 28, 37, 22, 33, 29, 31, 24, 36, 27, 38, 26, 34, 21, 39, 23, 31, 35, 26, 36, 28, 29, 30, 32, 33],
    'Sales_Made_Per_Week': [10, 8, 12, 5, 15, 11, 9, 13, 6, 12, 9, 10, 7, 14, 7, 14, 8, 13, 5, 16, 6, 10, 12, 7, 15, 9, 8, 10, 11, 11]
}
df5 = pd.DataFrame(data)


# In[50]:


df5.head(2)


# In[52]:


covariance = df5['Sales_Calls_Per_Day'].cov(df5['Sales_Made_Per_Week'])
## finding stad deviation
std_data1 = df5['Sales_Calls_Per_Day'].std()
std_data2 = df5['Sales_Made_Per_Week'].std()
##finding correlation
correlation = covariance/std_data1*std_data2


# In[53]:


correlation 


# In[ ]:




