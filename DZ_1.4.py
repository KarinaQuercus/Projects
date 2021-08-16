#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[22]:


x=np.arange(0, 20,0.1)
k1=1
k2=3
plt.plot(x, np.cos(k1*x))
plt.plot(x, np.cos(k2*x))


# In[ ]:




