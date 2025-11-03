#[Numpy] Numerical Python
#for installing numpy we have  PIP :  pip install packages (package manager for python)
#it is a python library. which is used to perform numerical operations/computations on array of numbers.
#we can use numpy on ndarray(n dimentional array).
#[1,2,3,4]--> 1d Array
#[[1,2],[3,4,7],[5,6]]--> 2d array-->each row should contain equal number of columns
#website---- numpy.org
import numpy as np


# x=np.array([1,2,3,4,5])  #creating an array
# x=np.array([[1],[2],[3],[4],[5]])
# x=np.array([[[[1],[2],[3],[4],[5]]]])
# print(type(x))

# print(np.ndim(x))   # ndim check which type dimentional we can find dimentional of an array

# ip1=np.array([
#     [1,2,3],
#     [1,4,5],
#     [7,8,9],
#     [3,5,6]
# ])
# print(np.shape(ip1))     #shape gives how many rows and columns
# #2d array
# #shape--->3x3
# print(np.size(ip1))      #gives total number of values in an array
ip2=np.array([2.3,4.5])
print(ip2.dtype)           #gives which datatype

#16/10/2025
#what is numpy?
#it is a python library and collection of modules
#module:- python file containing variables,functions,classes,methods

#modules are classified into 3 types
#1.Builtin Modules --> Comes with python by default
#ex:-
import math
print(type(math))
#2.User Definied/Custom Modules --> Users will Create Modules
import sample
print(sample.name)
#3.Third Party Module 
#numpy module

#list --> collection of heterogenous elements
#array --> collection of elements but the elements are of same datatype
#Numpy is a powerfull python library used to perform fast mathematical operations on arrays.
# Data retrival is fast in numpy because it stores in an organized way like stack 
  
#np.array() method  
arr1=np.array((1,2,3,4,5))
print(arr1)

#using time module
import time
start=time.time()

for i in range(100000):
    i*2
print("time taken",time.time()-start)   

#using numpy module
start=time.time()
num_arr=np.array(1000000)*2
print("numpy time",time.time()-start)

#creating numpy array upto the range using one of the method called 
# np.arange() 
arr2=np.arange(5000)
print(arr2)

#1D Matrix
print(np.array([1,2,3]),"id")
#2D Matrix
print(np.array([[1,2],[3,4]]),"2d")

#np.Zeros() method
print(np.zeros(3))
print(np.zeros(6))
print(np.zeros((3,30),dtype=int))

#np.Ones() method
print(np.ones(4,dtype=int))
print(np.ones((5,6),dtype=int))

#linearspace   np.linspace() method
print(np.linspace(2,101,50))       #start stop stepvalue
print(np.linspace(1,1000,4))

#using list
list1=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in list1:
    sum+=i
print(sum)
print(sum/len(list1))    

#using numpy
#np.sum() method
print(np.sum([1,2,3,4,5,6,7,8,9,10]))
#np.mean() method  ---> average of the specified values 
print(np.mean([1,2,3,4,5,6,7,8,9,10]))
print(np.mean([[1,2,3,4,5],[6,7,8,9,10]],axis=0))
print(np.mean([[1,2],[3,4],[6,9]],axis=1))   # vertical calculations    axis=0 for horizontal calculations

#np.median() --> odd-- middle element, even -- average of middle 2 elements
list2=[1,2,3,4,5,5]
mid=len(list2)//2
print(mid)
print(list2[mid])
print(list2[mid],list2[mid-1])

print(np.median([1,2,3,4,5]))
print(np.median([1,2,3,4,5,6]))
print(np.median([1,2,3,5,5,6]))

#np.clip() method

#pandas-->pytorch
#metplotlib
#     -->sea
#17/10/2025

#np.mode() method -->most repeated value

#np.shape() method -->
mat = np.array([[1,2,3],[4,5,6]])    #2d
mat2 = np.array([[[1,2,3],[4,5,6]]])   #3d
print(np.shape(mat))
print(np.ndim(mat))
print(np.ndim(mat2))
#np.reshape() method -->
dim1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(np.reshape(dim1,(3,4)))
print(np.reshape(dim1,(6,2)))
print(np.reshape(np.arange(12),(2,2,3)))
#np.flatten() method -->
arr=[[1,2,3,4,5,6,],[7,8,9,10,11,12],[13,14,15,16,17,18]]
print(len(arr))      #3
print(np.array(arr).flatten())

#np.concatenate() method -->combines arrays
a=np.array([[1,2],[4,5]])
b=np.array([[6,7],[8,9]])
print(np.concatenate((a,b)))
print(np.concatenate((a,b), axis=1))
print(np.concatenate((a,b), axis=0))

#indexing
#np.where() method
div=[1,2,3,4,500,6,7,0,99]
np_div=np.array(div)
print(np_div)
print(np.where(np_div>50))
print(np.where(np_div%2==0))
#vector
#dimension and magnitude 
print([1,2,3]*2)                 #-->scalar column
print(np.array([1,2,3])*2)       #-->vector column

#np.unique() method 
print(np.unique([1,2,3,1,2,3,5]))

#matrix multiplication             algebraic methods
# no of rows in 1st matrix = no of columns in 2nd matrix
#np.dot() method
print(np.dot([1,2],[3,4]))
print(np.dot([[1,2],[3,4]],
             [[5,6],[7,8]]))
#np.transpose() method
print(np.transpose([[1,2],
                    [3,4]]))
#np.linalg.inv() method    (linear algebra)
print(np.linalg.inv([[1,2],
                     [3,4]]))
#np.random.rand() method
print(np.random.rand(5))
#np.random.randint(start stop size) method
print(np.random.randint(1,10,5))
#np.size() method
print(np.array([1,2,3,4,5,6,7,8,9,10]).size)

#720-->HD
#1080-->FullHD
#2160-->4k
