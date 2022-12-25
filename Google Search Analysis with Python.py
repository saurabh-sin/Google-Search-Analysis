#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install pytrends 


# In[7]:


import pandas as pd
from pytrends.request import TrendReq # Unofficial API for Google Trends, allows simple interface for automating downloading of reports from Google Trends
import matplotlib.pyplot as plt
trends= TrendReq()


# In[8]:


#Creating dataframe of top 10 countries for analysing google search trends
trends.build_payload(kw_list=["Machine Learning"])
data=trends.interest_by_region()
data=data.sort_values(by="Machine Learning",ascending=False)
data=data.head(10) #top 10 countries
print(data)


# In[19]:


#Visualization by bar chart
data.reset_index().plot(x="geoName",y="Machine Learning",figsize=(10,15),kind="bar")
plt.style.use('fivethirtyeight')
plt.show()


# In[21]:


#Increase or decrease of total search queries on Google
data= TrendReq(hl='en-US',tz=360)
data.build_payload(kw_list=['Machine Learning'])
data=data.interest_over_time()
fig, ax=plt.subplots(figsize=(20,15))
data['Machine Learning'].plot()
plt.style.use('fivethirtyeight')
plt.title('Total Google Searches for Machine Learning',fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()

