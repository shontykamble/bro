#!/usr/bin/env python
# coding: utf-8

# In[8]:


a=1
b=2
c=a+b
c


# In[9]:


pip install seaborn


# In[10]:


import numpy as np


# In[11]:


import pandas as np


# In[12]:


import seaborn as sns


# In[13]:


pip install sklearn


# In[14]:


import sklearn


# In[16]:


from sklearn import tree
features = [[140,1],[130,1],[150,1],[170,1]]
labels=[0,0,1,1]
clf= tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
print(clf.predict([[150,0]]))


# In[ ]:




