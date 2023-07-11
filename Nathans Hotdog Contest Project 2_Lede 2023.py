#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Website with Contest winners 

#https://www.lastsandwich.com/articles/sandwich-sports/all-time-list-of-nathan-s-hot-dog-eating-champions


# In[132]:


import requests 
from bs4 import BeautifulSoup
import pandas as pd
import numpy


# In[133]:


#Get the info from website
hotdog_url = ("https://www.lastsandwich.com/articles/sandwich-sports/all-time-list-of-nathan-s-hot-dog-eating-champions")
hotdog_url = requests.get(hotdog_url)


# In[75]:


#Gets the text from a website
hotdog_url = hotdog_url.text
print(hotdog_url) #Provides the text of the website


# In[76]:


#Soup is now the variable for the HTML link 
hotdog = BeautifulSoup(hotdog_url)
type(hotdog) #Type shows you what the variable represents 


# In[77]:


#Got the contents of ONLY the website table 
hot_table = hotdog.find('div', id = "droptablestable85")
print(hot_table)


# In[78]:


#Turned the table into a dataframe with pandas 
hot_table_df = pd.read_html("https://www.lastsandwich.com/articles/sandwich-sports/all-time-list-of-nathan-s-hot-dog-eating-champions") 
hot_table_df 


# In[79]:


hot_table_dfs = pd.read_html('https://www.lastsandwich.com/articles/sandwich-sports/all-time-list-of-nathan-s-hot-dog-eating-champions')

# pandas.read_html() returns a list of DataFrames. Specify the index to select the desired table, even if it's the only one.
hot_table_df = hot_table_dfs[0]
hot_table_df.info()


# In[80]:


#Removed unwanted columns 
table = hot_table_df.drop(columns = ["Event", "Date", "Eat Off", "Time (Minutes)" ])
table
                                


# In[81]:


#Most Hotdogs Ate by Woman 
max(table["Hot Dogs.1"])


# In[82]:


#Most Hotdogs are by men or unisex (Not working for some reason)
max(table["Hot Dogs"])


# In[145]:


#Renamed the Column by calling it by column because referencing it by it's original title was not working 
r_table.rename(columns={r_table.columns[1]: 'Mens',r_table.columns[3]:'Womans'})


# In[148]:


r_table1 = r_table.rename(columns={r_table.columns[1]: 'Mens',r_table.columns[3]:'Womans'})
r_table1


# In[172]:


#All the times Joey Chestnut won 
jc=r_table1.loc[r_table1['Mens'] == "Joey Chestnut"]
jc


# In[178]:


tk=r_table1.loc[r_table1['Mens'] == "Takeru Kobayashi"]
tk


# In[196]:


ms = tk=r_table1.loc[r_table1['Womans'] == "Miki Sudo"]
ms


# In[198]:


#Total number of Hot dogs ate by JC
62+63+76+75+71+74+72+70+61+69+68+62+54+68+59+66


# In[199]:


#Total number of hot dogs ate by tk
53.75+49+53.5+44+50.5+50


# In[200]:


#Total number of hot dogs ate by ms
38.5+40+48.5+31.0+37+41+38.5+38+34


# In[ ]:




