#List Comprehension

'''
Problem:
    Write a program to add two 3 x 4 matrices using
    (a) lists
    (b) list comprehension
'''


#Solution:
#(a) Solution by using simple list

#this are simple matrices here
mat1=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
mat2=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
mat3=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        mat3[i][j]=mat1[i][j]+mat2[i][j]

print(mat3)

#(b) Solution by using list comprehension
# most simplist way
# one line code

mat3=[[mat1[i][j]+mat2[i][j] for j in range(len(mat1[0]))]
      for i in range(len(mat1))]
print(mat3)























'''
import random

lst=[x for x in range(1,11)]
print(lst)

lst1=[x**2 for x in range(1,11)]
print(lst1)

lst2=[random.randint(10,101) for n in range(20)]
print(lst2)
'''
