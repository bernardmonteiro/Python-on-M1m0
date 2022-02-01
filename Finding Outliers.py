#!/usr/bin/env python
# coding: utf-8

# In[ ]:


upper_limit = 91
lower_limit = 24
outlier = False
number = 8

if number > upper_limit:
  outlier = True
if number < lower_limit:
  outlier = True
if outlier == True:
  print(f"{number} is an outlier")

