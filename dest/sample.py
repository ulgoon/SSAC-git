#!/usr/bin/env python
# coding: utf-8

# # Simple http request example
# 
# [Get data from starbucks](https://www.starbucks.co.kr/store/getStore.do?r=VWW6MBSUM0)

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


response = requests.get('https://www.google.com/')
response.status_code


# In[3]:


print(input('Enter some number:'))


# [latex](http://www.ktug.org/xe/index.php?mid=KTUG_open_board&document_srl=248288)
# 
# 
# $y=x+1$

# In[4]:


for j in range(10):
    print(j)


# In[ ]:




