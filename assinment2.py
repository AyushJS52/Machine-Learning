
# coding: utf-8

# ## Answer 1

# In[1]:


import numpy as np


# In[2]:


x=np.random.random([10,1])


# In[3]:


x


# In[4]:


np.mean(x)


# # Answer2

# In[5]:


y=np.random.random([20,1])


# In[6]:


y


# In[7]:


np.var(y)


# In[8]:


np.std(y)


# # Answer 3

# In[9]:


z=np.random.random([10,20])


# In[10]:


a=np.random.random([20,25])


# In[13]:


e = np.dot(z,a)


# In[14]:


e


# In[15]:


e.shape


# In[16]:


np.sum(e)


# # Answer 4

# In[17]:


w = np.arange(10).reshape(10,1)


# In[18]:


def myfunc(x,axis):
    return 1/(1+ np.exp(-x))


# In[19]:


np.apply_over_axes(myfunc,w,1)

