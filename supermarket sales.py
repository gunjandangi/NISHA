#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


supermarket_sales=pd.read_csv("supermarket_sales_-_sheet1[1].csv",encoding="unicode escape")
supermarket_sales


# In[4]:


supermarket_sales.head(10)


# In[5]:


supermarket_sales.tail(10)


# In[6]:


supermarket_sales.info()


# In[7]:


supermarket_sales.count()


# In[8]:


supermarket_sales_gender=supermarket_sales["Gender"].value_counts()
supermarket_sales_gender


# In[9]:


supermarket_sales_sum=supermarket_sales["Quantity"].sum()
supermarket_sales_sum


# In[10]:


supermarket_sales_accessories=supermarket_sales[(supermarket_sales["Product line"]=="electronic accessories")]
supermarket_sales_accessories


# In[11]:


count=[]
value=[]
for i in supermarket_sales["Product line"].unique():
    x=supermarket_sales[("Product line")].value_counts()[i]
    print(i,x)
    count.append(i)
    value.append(x)


# In[12]:


supermarket_sales_salary=supermarket_sales["Total"].max()
supermarket_sales_salary


# In[13]:


product_value=[]
product_count=[]
for i in supermarket_sales["Product line"].unique():
    x=supermarket_sales[(supermarket_sales["Product line"]==i)]["Total"].mean()
    print(i,x)
    product_value.append(x)
    product_count.append(i)
    


# In[9]:


sns.pairplot(data=supermarket_sales)


# In[7]:


supermarket_sales_head=supermarket_sales.head(20)
supermarket_sales_head


# In[15]:


supermarket_sales_payment=supermarket_sales[(supermarket_sales["Payment"]=="Ewallet")].value_counts()
supermarket_sales_payment


# In[50]:


plt.bar(supermarket_sales_head["Payment"],supermarket_sales_head["Quantity"],color=["red","green","blue"])
plt.title("quantity with payment")
plt.xlabel("quantity")
plt.ylabel("Payment")
plt.show()


# In[12]:


supermarket_sales_head_five=supermarket_sales.head()
supermarket_sales_head_five


# In[28]:


count=[]
value=[]
for i in supermarket_sales_head["Payment"].unique():
    x=supermarket_sales_head["Payment"].value_counts()[i]
    print(i,x)
    count.append(i)
    value.append(x)


# In[24]:


plt.bar(supermarket_sales_head["count"],supermarket_sales_head["payment"],color=["blue","red","green"])
plt.xticks(rotation=90)
plt.title("payment count")
plt.xlabel("Payment")
plt.ylabel("count")
plt.show()


# In[26]:


sns.scatterplot(data=supermarket_sales_head_five,x="Product line",y="Quantity",hue="Gender")
plt.title("Product with quantity")
plt.xlabel("Product line")
plt.ylabel("Quantity")
plt.show()


# In[29]:


sns.barplot(data=supermarket_sales_head_five,x="City",y="Unit price",hue="Branch")
plt.title("Product with quantity")
plt.xlabel("city")
plt.ylabel("unitprice")
plt.show()


# In[13]:


sns.violinplot(data=supermarket_sales_head_five,y="Quantity")


# In[15]:


sns.barplot(data=supermarket_sales_head_five,y="cogs")


# In[23]:


#beauty products ki rating 7 se kam hai
supermarket_sales_rating=supermarket_sales_head_five[(supermarket_sales_head_five["Rating"]>7)].value_counts()
supermarket_sales_rating


# In[39]:


a=[]
b=[]
for i in supermarket_sales["Product line"].unique():
    x=supermarket_sales["Product line"].value_counts()[i]
    print(i,x)
    a.append(i)
    b.append(x)
    plt.plot(a,b)
    plt.show()
    

