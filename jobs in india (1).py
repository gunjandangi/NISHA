#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


job_india=pd.read_csv("jobs_in_data[1].csv",encoding="unicode escape")
job_india


# In[3]:


job_india.head(5)


# In[4]:


job_india.describe()


# In[5]:


job_india.isnull().sum()


# In[6]:


job_india.info()


# In[7]:


job_india.count()


# In[8]:


scientist_senior=job_india[(job_india["job_title"]=="Data scientist") & (job_india["experience_level"]=="senior")]
scientist_senior


# In[9]:


scientist_salary=job_india[(job_india["job_title"]=="Data scientist")& (job_india["salary"]==93300)]
scientist_salary


# In[10]:


average_salary=job_india[(job_india["job_title"]=="Data Scientist")]["salary"].mean()
average_salary


# In[11]:


#count data scintist in job title
category_scientist=job_india["job_title"].count()
category_scientist


# In[12]:


max_salary=job_india["salary"].max()
max_salary


# In[13]:


plt.plot( job_india['work_year'] ,job_india['salary'])
plt.title("salary and experience of job")
plt.xlabel("work_year")
plt.ylabel("salary")
plt.show()


# In[14]:


top_salary_in_usd=job_india.nlargest(5,"salary_in_usd")
top_salary_in_usd


# In[15]:


top_salary=job_india.nlargest(5,"salary")


# In[16]:


top_salary


# In[17]:


top_five_salary=sorted(job_india["salary"],reverse=True)[:5]


# In[18]:


top_five_salary


# In[19]:


plt.plot(top_salary["salary_in_usd"], top_salary["salary"])
plt.title("top salary with top five")
plt.xlabel("top_salary_in_usd")
plt.ylabel('top_salary')
plt.show()


# In[21]:


sns.barplot(data=job_india,hue="experience_level",x="employment_type",y="work_year")


# In[22]:


sns.histplot(data=job_india,x="experience_level")


# In[23]:


sns.barplot(data=job_india,x="company_size",y="salary_in_usd")


# In[24]:


job_graph=job_india["job_title"].count()
job_graph


# In[25]:


sns.pairplot(data=job_india)


# In[26]:


sns.violinplot(data=job_india,y="salary")


# In[27]:


average_scientist=job_india[(job_india["job_title"])=="Data Scientist"]["salary"]
average_scientist.mean()


# In[28]:


scientist=[]
for i in job_india["job_title"].unique():
    x=job_india["job_title"].value_counts()[i]
    print(i,x)
    scientist.append(x)
    


# In[29]:


y=[]
d=[]
for i in job_india["employee_residence"].unique():
    x=job_india["employee_residence"].value_counts()[i]
    print(i,x)
    y.append(i)
    d.append(x)
    plt.plot(y,d)
    plt.show()


# In[30]:


average_salary=job_india.groupby("job_title")["salary"].mean()
average_salary

