#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


milk_choclate=pd.read_csv("chocolate[1].csv",encoding="unicode escape")
milk_choclate


# In[3]:


milk_choclate.tail()


# In[4]:


milk_choclate.info()


# In[5]:


milk_choclate.describe()


# In[6]:


milk_choclate.duplicated()


# In[7]:


milk_choclate_ingredients=milk_choclate[(milk_choclate["ingredients"]=="3-B,S,C")]
milk_choclate_ingredients


# # find cocoa_percent percentage is 71%

# In[8]:


milk_choclate_percent=milk_choclate[(milk_choclate["cocoa_percent"]=="71%")]
milk_choclate_percent


# In[9]:


milk_choclate[2454:2542]


# In[10]:


milk_choclate.iloc[3:5]


# In[11]:


milk_choclate["review_date"]


# # choose date where year is 2014

# In[12]:


milk_choclate=milk_choclate[(milk_choclate["review_date"]==2014)]
milk_choclate


# # choose where year is 2014 and country is austria

# In[13]:


milk_choclate=milk_choclate[(milk_choclate["review_date"]==2014) & (milk_choclate["company_location"]=="Austria")]
milk_choclate


# # choose where rating is >3.00

# In[14]:


milk_choclate=milk_choclate[(milk_choclate["rating"]>3.00)]
milk_choclate


# # count country

# In[24]:


for i in milk_choclate["company_location"].unique():
    x=milk_choclate["company_location"].value_counts()[i]
    print(i,x)


# In[25]:


milk_choclate_top=milk_choclate.head(5)
milk_choclate_top


# # company location with date top 5

# In[26]:


plt.plot(milk_choclate_top["review_date"],milk_choclate_top["company_location"])
plt.title("company location with date ")
plt.xlabel("company_location")
plt.ylabel("review_date")
plt.show()


# # barchart

# In[27]:


sns.barplot(data=milk_choclate_top,x="cocoa_percent",y="review_date")


# In[22]:


milk_choclate_hist=milk_choclate.iloc[19:30]
milk_choclate_hist


# # histogram graph

# In[23]:


sns.histplot(data=milk_choclate_hist,hue="review_date",x="rating")


# In[28]:


sns.histplot(data=milk_choclate_hist,hue="review_date",x="rating",bins=10,kde=True)


# # compare all graphs

# In[29]:


sns.pairplot(data=milk_choclate)


# In[12]:


milk_choclate_head_ten=milk_choclate.head(5)
milk_choclate_head_ten


# In[ ]:




