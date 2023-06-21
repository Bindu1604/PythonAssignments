# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 21:13:24 2023

@author: bindu
"""

list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
print("Output:")
for i in list1:   
    if i >= 0:
        print(i,end=" ")
positive_num = [num for num in list2 if num >= 0]
print("Output:",positive_num)