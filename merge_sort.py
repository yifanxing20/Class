#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random 
import time

def merge_sort(list_):
    if len(list_) <= 1:
        return list_
    middle= len(list_)//2 
    left= merge_sort(list_[:middle])
    right=merge_sort(list_[middle:])
    return reduce(left,right)
        
def reduce(left,right):
    result=[]
    left_index= 0
    right_index= 0
    while True :

        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index +=1
        else:
            result.append(right[right_index])
            right_index +=1
        if left_index == len(left):
            result.extend(right[right_index:])
            break
        if right_index ==len(right):
            result.extend(left[left_index:])
            break
    return result 

def cal_time(list_):
    start = time.time()
    f= merge_sort(list_)
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




