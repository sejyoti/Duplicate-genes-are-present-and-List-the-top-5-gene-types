#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('PyCodingAssignment.data.csv')


# In[3]:


df.head()


# In[5]:


#Part 1 / Q1 / i
gene_ids = np.unique(np.array([df['GENE_ID']]))
print(len(gene_ids))


# In[6]:


#Part 1 / Q1 / ii / a
gene_names = np.array([df['GENE_NAME']])
unique, counts = np.unique(gene_names, return_counts = True)


# In[7]:


for i in range(len(unique)):
    print('Name: %s   Count: %d'%(unique[i], counts[i]))


# In[63]:


#Part 1 / Q1 / ii / b
ind = np.argpartition(counts, -5)[-5:]
ind = list(ind)
ind.reverse()
top5 = unique[ind]
print(top5)


# In[55]:





# In[59]:





# In[ ]:




