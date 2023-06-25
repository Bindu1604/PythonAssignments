# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 21:13:24 2023

@author: bindu
"""

def most_frequent(string):
    freq_dict = {}
    for char in string:
        if char.isalpha():  
            char = char.lower()  
            freq_dict[char] = freq_dict.get(char, 0) + 1
    sorted_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_dict:
        print(f"{char} = {count:02d}", end=" ")
    print() 
input_string = input("Please enter a string: ")
most_frequent(input_string)