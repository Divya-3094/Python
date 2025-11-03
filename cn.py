#check even or odd  
n=int(input("enter the number:"))
if n%2==0:
    print("even number")
else:
    print("odd number") 

#age group classifier        
age=int(input("enter the age:"))
if age<13:
    print("child")
elif age>13 and age<=20:
    print("teenage")
elif age>=20:
    print("adult")
else:
    print("senior")        

#positive or negative number
n=int(input("enter the number:"))
if n>0:
    print("positive number")
elif n<0:
    print("negative number")
else:
    print("zero") 

#check if the number is divisible by  both 3 and 5
n=int(input("enter the number:"))
if n%3==0 and n%5==0:
    print("number is divisible by both")
elif n%5==0:
    print("number is divisible by 5")
elif n%3==0:
    print("number is divisible by 3")
else:
    print("none")            

#largest numbr
a=int(input("enter the number:"))
b=int(input("enter the number:"))
if a>b:
    print(f"{a} is the largest number")
else:
    print(f"{b} is the largest number")    

#triangle validity checker
s1=15
s2=10
s3=23    
if (s1+s2)>s3 and (s1+s3)>s2 and (s2+s3)>s1:
    print("can form a triangle")
else:
    print("cannot form a triangle")    

#for loop with seqential data
input_str="hello"
for char in input_str:
    print(char, end=" ")

#sum of the first 10 natural numbers
sum=0
for i in range(1,11):
      sum += i
      print("sum of first 10 natural numbers is:",sum)

#print even numbers from 1 to 20
for i in range(1,21):
    if(i%2==0):
        print(i)

#Print elements in a list
items=["pen", "pencil", "eraser"]
for item in items:
 print(item)

#print common elements in two lists
list1=["pen","pencil","eraser","book"]
list2=["pen","book","pencil","sharpner"]
for item in list1:
    if item in list2:
        print(item)

#Print all elements in a set
my_set = {"apple", "banana", "cherry"}
for items in my_set:
  print(items)

#Count how many items are in a set using a loop
count=0
colors = {"red", "blue", "green", "yellow"}
for items in colors:
    count += 1
    print(items)

#Print all keys and values in a dictionary
person = {"name": "divya", "age": 21, "city": "AP"}
for key, value in person.items():
    print(key, ":",value)

#Count how many values in a dictionary are greater than 50
count=0
scores = {"math": 45, "english": 55, "science": 80, "history": 40}
for value in scores.values():
    if value>50:
        count +=1
        print("number of values greater than 50 are:", count)

#Create a new dictionary with only items where the value is even
data = {"a": 1, "b": 4, "c": 6, "d": 3}
even_dict={}
for key, value in data.items():
    if value%2==0:
        even_dict[key]=value
        print("dictionary with even values:",even_dict)




