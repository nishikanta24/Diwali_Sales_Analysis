#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df=pd.read_csv(r"D:\study\Python_Diwali_Sales_Analysis\Diwali Sales Data.csv",encoding="unicode_escape")
#r is added in the begining for understanding of specila charachters in the path like"_"


# In[4]:


df.shape #shows rows and columns


# In[5]:


df.head(5)#showing top 5 values of csv


# In[6]:


df.info()


# In[7]:


#removing blank columns Status and unnamed1
df.drop(['Status','unnamed1'],axis=1,inplace=True)


#axis=0 means "look at the rows".
#axis=1 means "look at the columns".
#So, axis=1 here means we want to remove columns.

#inplace=True
#When we do something to a DataFrame, there are two ways it can be done:

#Create a new DataFrame with the changes and keep the old one as it is.
#Change the original DataFrame directly and don’t keep the old version.
#inplace=True means we want to change the original DataFrame directly.


# In[8]:


df.info()


# In[9]:


pd.isnull(df)#shows false if value is there  and trrue if no value or bam]nk it is


# In[10]:


pd.isnull(df).sum()
#shows which all columns has blank or no values


# In[11]:


df.shape


# In[12]:


df.dropna(inplace=True)# if axis not mentioned it will by default remove the rows having nnull values


# In[13]:


df.shape


# In[14]:


df['Amount']=df['Amount'].astype('int')


# In[15]:


df['Amount'].dtypes


# In[16]:


df.columns


# In[17]:


df.describe()


# # GENDERS
# 
# 

# In[18]:


ax= sns.countplot(x='Gender',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[19]:


# females made more purchases than male


# In[20]:


df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[21]:


sales_gender=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
ax=sns.barplot(x='Gender',y='Amount',data=sales_gender)
for bars in ax.containers:
    ax.bar_label(bars)
    


# In[22]:


# we can see females spent greater amount orare the bigger buyers than men


# # Age
# 

# In[23]:


df.columns


# In[25]:


df['Age Group'] = df['Age Group'].astype('category')#here we converts Age Group column type to category data type 
age_group_order = df['Age Group'].cat.categories## Get the categories in ascending order
df['Age Group'] = df['Age Group'].cat.reorder_categories(age_group_order[::-1], ordered=True)#this sets the units in descending order
ax=sns.countplot(x='Age Group',hue='Gender',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[26]:


df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Age Group',ascending=True)



# In[27]:


sales_age=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=True)
ax=sns.barplot(x='Age Group',data=sales_age,y='Amount')


# 
# Among all age groups women dominates men in terms of buying
# 

# # State
# 

# In[29]:


df.columns


# In[31]:


df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False)


# In[44]:


Order_State=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(17,5)})
ax=sns.barplot(x='State',data=Order_State,y='Orders')
for bars in ax.containers:
    ax.bar_label(bars)


# In[45]:


df.groupby('State',as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)


# In[46]:


Amount_State=df.groupby('State',as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(17,5)})
ax=sns.barplot(x='State',data=Amount_State,y='Amount')
for bars in ax.containers:
    ax.bar_label(bars)


# we observe that most of the orders are from Uttar Pradesh, Maharashtra and Karnataka.

# # Marital Status
# 

# In[47]:


df.columns


# In[53]:


ax=sns.countplot(x='Marital_Status',data=df)
sns.set(rc={'figure.figsize':(3,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[64]:


Marital_Status_Amount=df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
ax=sns.barplot(x='Marital_Status',y='Amount',data=Marital_Status_Amount,hue='Gender')
sns.set(rc={'figure.figsize':(18,5)})
for bars in ax.containers:
    ax.bar_label(bars)

                              


# most ofthe buyers are married women and they have higher purcahsing power

# # Occupation

# In[65]:


df.columns


# In[99]:


sns.set(rc={'figure.figsize':(20,8)})
ax=sns.countplot(x='Occupation',data=df)
plt.xticks(rotation=45)
for bars in ax.containers:
    ax.bar_label(bars)


# In[75]:


Amount_Occupation=df.groupby('Occupation',as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(21,5)})
ax=sns.barplot(x='Occupation',data=Amount_Occupation,y='Amount')
for bars in ax.containers:
    ax.bar_label(bars)


# Nost of the buyers are in IT Healthcare and Aviation

# # Product Category

# In[105]:


top_10_categories=df['Product_Category'].value_counts().nlargest(10)
sns.set(rc={'figure.figsize':'10,5'})
top_10_categories.plot(kind='bar')
plt.xlabel('Product Categories')
plt.ylabel('Count')
plt.title('Top 10 Product Categories')
plt.xticks(rotation=45)
plt.show()


# Most of the sold Products are from Clothing and Apparel followed by Food then Electronics & Gadgets and then others
# 

# In[113]:


Product_Category_Amount=df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
ax=sns.barplot(x='Product_Category',y='Amount',data=Product_Category_Amount)
sns.set(rc={'figure.figsize':(18,10)})
plt.xticks(rotation=45)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()


# most sold  produccts are food clothing and the electronics
# 

# In[101]:


ProductID_Amount=df.groupby(['Product_ID'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
ax=sns.barplot(x='Product_ID',y="Amount",data=ProductID_Amount)
for bars in ax.containers:
    ax.bar_label(bars)


# In[118]:


Top_10_ProductID=df['Product_ID'].value_counts().nlargest(10)
Top_10_ProductID.plot(kind='bar')
plt.xlabel('Product_ID')
plt.xticks(rotation=45)
plt.ylabel('Count')
plt.title('Most no of Sold Product')
plt.show()


# Married women age group 26-35 yrs from UP,Maharashtra and  Karnataka working in IT,Healthcare and Aviaton are more likely to buy products from food clothing and electronics category
# 

# In[ ]:




