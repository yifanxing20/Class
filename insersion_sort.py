#!/usr/bin/env python
# coding: utf-8

# In[17]:


import random 
import time 

def insersion_sort(list_):
    i=1
    while i < len(list_):
        j=i-1
        key=list_[i]
        while j >=0:
            if key <list_[j]:
                list_[j+1],list_[j] = list_[j],list_[j+1]
            j=j-1
        i=i+1
    return list_

def cal_time(list_):
    start = time.time()
    f= insersion_sort(list_)
    end = time.time()
    est_time = end- start
    return est_time

def cal_num(list_):
    worst_result =[]
    best_result=[]
    average_result=[]
    for num in list_ :
        print(num)
        worst_list = list(range(num,1,-1))
        best_list = list(range(1,num))
        average_list = random.sample(list(range(num)),k=num)
        worst_result.append(cal_time(worst_list))
        best_result.append(cal_time(best_list))
        average_result.append(cal_time(average_list))
        
    return [worst_result,best_result,average_result]

list_series= [1000,2000,4000,6000,8000,10000]
result = cal_num(list_series)
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(list_series,result[0],label = 'worst')
plt.plot(list_series,result[1],label = 'best')
plt.plot(list_series,result[2],label = 'average')
plt.legend()
plt.show()


# In[ ]:




