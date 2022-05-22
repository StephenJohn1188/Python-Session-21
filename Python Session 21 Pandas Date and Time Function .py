#!/usr/bin/env python
# coding: utf-8

# # Pandas Data and Time Funtions

# In[9]:


import pandas as pd

df=pd.read_csv('hrdata.csv')
print(df)


# In[12]:


d=pd.to_datetime({'year':[2022],'Month':[2], 'Day':[4]})
d


# In[14]:


df['HireDate']=pd.to_datetime(df['HireDate'])
df


# In[18]:


daterange=pd.date_range(start='1/1/2020', end='1/10/2020',freq='D')
daterange


# In[21]:


daterange=pd.date_range(start='1/1/2020', end='5/1/2020',freq='M')
daterange


# In[26]:


import datetime
dt=datetime.datetime.now()
print(dt)

print(dt + pd.to_timedelta(10, unit='D'))

#--->gives the date and time after 10 days


# In[29]:


#Saperating day, month and year
df['Day']=df['HireDate'].dt.day
df['Month']=df['HireDate'].dt.month
df['year']=df['HireDate'].dt.year
print(df)


# # Pandas SQL

# In[32]:


import pandas as pd

df=pd.read_csv('empl.csv')
df


# In[36]:


df1=pd.DataFrame(data=df, columns=['Name'])
df1


# In[37]:


df1=pd.DataFrame(data=df, columns=['Name','Age'])
df1


# In[40]:


df1=pd.DataFrame(data=df, columns=['Name','Age', 'salary'])
df1


# In[44]:


df[['Name','Age','Salary']].head(5)


# In[45]:


df[df['City']=='newyork']


# In[47]:


df[(df['City']=='newyork')&(df["Salary"]>50000)]


# In[50]:


df[(df['Country']=='Africa') | (df["Salary"]>65000)]


# In[52]:


df[df['Salary'].isna()]


# In[53]:


df[df['Salary'].notna()]


# In[54]:


dfs=df.dropna(axis=0)


# In[55]:


print(dfs)


# In[56]:


df.isnull().sum()


# In[57]:


dfs.isnull().sum()


# # Join in Pandas

# In[61]:


import pandas as pd

raw_data={
    'subject_id':['1','2','3','4','5'],
    'first_name':['Alex','Amy','Allen','Alice','Ayoung'],
    'last_Name':['Anderson', 'Ackerman', 'Ali', 'Aoni','Atiches']}
df_a=pd.DataFrame(raw_data, columns = ['subject_id', 'first_name','last_Name'])
df_a


# In[62]:


import pandas as pd

raw_data={
    'subject_id':['1','2','3','4','5'],
    'first_name':['Brain','Benny','Bryce','Bit','Bagg'],
    'last_Name':['Howard', 'Todd', 'Deakin', 'Movie','pat']}
df_b=pd.DataFrame(raw_data, columns = ['subject_id', 'first_name','last_Name'])
df_b


# In[63]:


df_new=pd.concat([df_a,df_b],ignore_index=True)
df_new


# In[65]:


import pandas as pd

raw_data={
    'subject_id':['1','2','3','4','5','6','7','8','9','10'],
    'test_id':[51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
df_n=pd.DataFrame(raw_data, columns = ['subject_id', 'test_id'])
df_n


# In[66]:


pd.merge(df_new,df_n)


# In[68]:



pd.merge(df_new,df_n, on='subject_id')


# In[69]:


pd.merge(df_a,df_b, on='subject_id', how='inner')


# In[70]:


pd.merge(df_a,df_b, on='subject_id', how='outer')

