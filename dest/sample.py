#!/usr/bin/env python
# coding: utf-8

# # Simple http request example
# 
# [Get data from starbucks](https://www.starbucks.co.kr/store/getStore.do?r=VWW6MBSUM0)

# In[3]:


import requests
from bs4 import BeautifulSoup


# In[4]:


response = requests.get('https://www.google.com/')
status = response.status_code
html = response.text
print(html[:200])


# In[5]:


print(input('Enter some number:'))


# [latex](http://www.ktug.org/xe/index.php?mid=KTUG_open_board&document_srl=248288)
# 
# 
# $y=x+1$

# In[6]:


for j in range(10):
    print(j)


# In[7]:


for i in range(1,15+1):
    if i%3==0:
        print('fizz')
    else:
        print(i)


# In[ ]:




