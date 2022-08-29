"""Write a function that accepts a number as a parameter. The function should return a number that’s the difference between the largest and smallest numbers that the digits of the provided number can form."""

import itertools
num=input("Enter the Number : ")
l_num = list(num)
l_permutations=[]
list1=itertools.permutations(l_num)
for a in list1 :
     str_num=""
     for i in a :
          str_num=str_num+i
     int_num=int(str_num)
     l_permutations.append(int_num)
print ("Difference of Maximum possible and Minimum possible Number : ", max(l_permutations)-min(l_permutations))

""" 
Test Case :
Input = 213
Output = 198
"""
