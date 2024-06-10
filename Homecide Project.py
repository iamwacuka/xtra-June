#!/usr/bin/env python
# coding: utf-8

# In[143]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



# In[142]:


pip install plotly


# In[46]:


df=pd.read_csv(r'C:\Users\WSEDR\Downloads\homicide_by_countries.csv')
df


# In[47]:


df.head(10)


# In[48]:


df.shape


# In[49]:


df.isna().sum()


# In[50]:


#df.dropna([Location'],inplace=True)


# In[51]:


df.dtypes


# In[52]:


df['Rate']=df['Rate'].astype(int)


# In[53]:


df.dtypes


# In[54]:


my_list=['Rate','Count','Year']
for i in my_list:
    print(i)
    df[i]=df[i].astype(int)


# In[55]:


df.dtypes


# In[63]:


df['Region'].replace('Americas','America',inplace=True)


# In[61]:


df


# In[ ]:





# In[64]:


df1=df.sort_values('Count',ascending=False)
df1


# In[65]:


df1.reset_index(drop=True)


# In[66]:


df2=df[['Location','Count']].sort_values(by='Count',ascending=False).head(5)
df2['Perc']=(df2['Count']*100/df2['Count'].sum()).round(2)
df2


# In[29]:


df2.Location


# In[32]:


df2.plot(x='Location',y='Count',kind='pie',labels=df2.Location, autopct= '%1.2f%%')
plt.legend().set_visible(False)


# In[35]:


df


# In[68]:


df2=df.groupby('Region')['Count'].sum().sort_values(ascending=False)
df2


# In[70]:


df2.plot(kind='bar')
plt.show()


# In[71]:


df


# In[74]:


df3=df.groupby('Subregion')['Count'].sum().sort_values(ascending=False)
df3


# In[76]:


df3.index


# In[77]:


df3.values


# In[80]:


sns.barplot(x=df3.index,y=df3.values)
plt.xticks(rotation='vertical')
xlabel=None


# In[82]:


df


# In[84]:


df.Year.value_counts()


# In[87]:


df4=df[df['Region'].isin(['Asia','Europe'])]
df4


# In[88]:


df[(df['Region']=='Asia')| (df['Region']=='Europe')]


# In[91]:


df4=df4[df4['Year']>2016][['Region','Year','Count']]
df4


# In[99]:


df4=df4.groupby(['Region','Year']).sum(['Count'])
df4


# In[105]:


df_unstacked=df4.unstack(level=0)
df_unstacked


# In[110]:


df_unstacked.index=df_unstacked.index.astype(int).astype(str)


# In[111]:


df_unstacked.index


# In[113]:


df_unstacked.plot(kind='line',figsize=(10,6))
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Count of Asia and Europe over Years')


# In[115]:


df=pd.read_csv(r'C:\Users\WSEDR\Downloads\homicide_by_countries.csv')
df


# In[117]:


df5=df.groupby(['Year'])['Rate'].sum().sort_values(ascending=False)
df5


# In[121]:


df5.plot(kind='bar',figsize=(7,3),color='skyblue',edgecolor='black')
plt.xlabel('Year')
plt.ylabel('Sum of Rate')
plt.title('Sum of Rate by Region and Year')


# In[122]:


df


# In[129]:


df6=df[['Year','Region','Count']]
df6=df6.groupby(['Year','Region']).sum().sort_values(by='Year',ascending=False).head(20)
df6


# In[133]:


df6.plot(kind='bar',figsize=(12,6),colormap='viridis')
plt.xlabel('Year and Region')
plt.ylabel('Sum of Count')
plt.title('Sum of Count Per Year and Region')


# In[134]:


df


# In[137]:


df7=df.groupby('Subregion')['Count'].mean().sort_values(ascending=False).round(2)
df7


# In[138]:


df7.index


# In[139]:


df7.values


# In[141]:


data={
    'Category':df7.index,
    'Value':df7.values,
    'Info':df7.values
}
df=pd.DataFrame(data)
df


# In[147]:


fig=px.treemap(df,path=['Category'],values='Value',title='Treemap')
fig.update_traces(hovertemplate='Category: %{label}<br>Value:%{value}')
fig.show()


# In[ ]:




