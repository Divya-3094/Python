#problems on lists
#create a list of 5 integers
list=[1,2,3,4,5]
print(list)
#access 3rd element of a list
list=[20,30,40,50,60]
print(list[2])
#change value at index 2
list=[10,20,30,40,50]
list[2]=60
print(list)
list.append(70)  # append an elemnet to the list
print(list)
list.insert(1,25)    #insert an element at index 1
print(list)
list.remove(25)     # remove an element by value
print(list)
list=[10,20,30,40,50]
list.pop(0)       #remove an elemnet by index
print(list)
print(len(list))   #find length of the list
#check if an element exists in a list
list=[10,20,30,40,50]
if 30 in list:
    print(" 30 exists in list")
else:
    print(" 30 doesnt exists")    
#loop through a list and print each item
list=[10,20,30,40,50]  
for item in list:
    print(item)
#sort a list in ascending order
list=[90,80,30,70,50]
list.sort()
print(list)
list.sort(reverse=True)  # sort a list in descending order
print(list)
#reverse a list using reverse()
list=[10,20,30,40,50]
list.reverse()
print(list)
#reverse a list using slicing
list=[90,80,30,70,50]
reverse=list[::-1]
print(reverse)
#copy a list using slicing 
list=[90,80,30,70,50]
list1=list[:]
print(list1)
#copy a list using copy() method
list=[1,2,3,4,5,6]
list.copy()
print(list)
#clear all elements in list
list=[90,80,30,70,50]
list.clear()
print(list)
#count accurences of a number
list=[1,4,6,3,1,3,6,8,1,7,6,1]
print(list.count(1))
#find index of a number
list=[90,80,30,70,50]
x=list.index(30)
print(x)
#concatenate 2 lists
list=[90,80,30,70,50]
list1=[1,4,6,3,1,3,6,8,1,7,6,1]
list.extend(list1)
print(list)
#concatenation
list=[90,80,30,70,50]
list1=[1,4,6,3,1,3,6,8,1,7,6,1]
combine=list+list1
print(combine)
#repeate a list 3 times
list=[90,80,30,70,50]
repeat=list*3
print(repeat)
#print every second element
list=[90,80,30,70,50,60]
print(list[1::2])
#print every second element
list=[90,80,30,70,50,60]
for i in range(1,len(list),2):
    print(list[i])
#print elements from index 2 to 5
list=[90,80,30,70,50,60,10]  
print(list[2:6])
#check if all elements are positive
x=[90,80,30,70,50,60,10]
if (num>0 for num in list):
    print("positive")
else:
    print("negative")
#convert list to a string with commas
x=["apple","banana","mango"]
y=','.join(x)   
print(y)  
#find max element
x=[90,80,30,70,50,60,10]
y=max(x)
print(y)
#find min element
x=[90,80,30,70,50,60,10]
y=min(x)
print(y)
#summ of all numbers in a list
x=[90,80,30,70,50,60,10]
y=sum(x)
print(y)
#sqare every number in a list
list=[90,80,30,70,50,60,10]
y=[x**2 for x in list] 
print(y)
#e=filter even numbers from list
list=[90,85,30,75,50,65,10]
y=[ x for x in list if x%2==0]
print(y) 
#filter odd numbers from list
list=[90,85,30,75,50,65,10]
y=[x for x in list if x%2!=0]
print(y)
#find duplicates in list
list=[90,85,30,75,50,65,10,30,90,75]
x=set()
y=set()
for item in list: 
    if item in y:
        x.add(item)
    else:
        y.add(item) 
print(x)         
#remove duplicates from list
list1=[1,2,3,2,4,5,3,6,3]
unique_list=[]
seen=set()
for item in list1:
    if item not in seen:
        unique_list.append(item)
        seen.add(item)
print(unique_list) 
#get unique elements using set()
list1=[1,2,3,2,4,5,3,6,3]
unique_list=set(list1)
print(unique_list)
#
list1=[1,2,3,2,4,5,3,6,3]
unique_elements=set(list1)
print(unique_elements)
#check if a list is empty
list2=[]
if len(list2)==0:
    print("list is empty")
else:
    print("list is not empty")  
#initialize a list of n zeros
n=5
list=[0]*n      
print(list)
#swap 2 elements in a list
list1=[10,20,30,40]
list1[1], list1[3]=list1[3],list1[1]
print(list1)
#get last element of a list
list1=[10,20,30,40]
print(list1[3])
#convert a string to a list of chars
str1="chitti"