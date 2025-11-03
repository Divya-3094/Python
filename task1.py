fruits=["apple","mango","banana"]
print(fruits)
print(fruits[0])
print(fruits[2])
fruits[1]="pineapple"
print(fruits)

x=["divya","sneha","lite","ashaa"]
print(id(x))
print(x)
x[2]="cryso"
print(x)
print(id(x))

data=[1,2,[4,5],[6,7],8,"something",]
print(data)
print(data[2][0])
print(data[3][0])
print(data[5][2])

mixed=[1,2,"hi",12.5,True]
print(mixed)
print(type(mixed))
value=1
value1="hi"
print(type(value))
print(type(value1))

#WAP to chech whether the number is armstrong or not
num = int(input("Enter a number: "))
n= len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit **n
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")



#neon or sunny number
import math
num = int(input("Enter a number: "))
sqrt_val = math.isqrt(num + 1)
if sqrt_val * sqrt_val == num + 1:
    print(num, "is a Sunny number.")
else:
    print(num, "is not a Sunny number.")

#list & tuple packing and unpacking

#Add all elements of a list.
list1=[1,2,3,4,5,6,7,8,9,10]
list1.extend([11,12,13,14,15])
print(list1)

#Find max and min in a list.
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(max(list1), min(list1))

#Count even and odd numbers in a list.
numbers = [10, 21, 4, 45, 66, 93, 1]
even_count = len(list(filter(lambda x: x % 2 == 0, numbers)))
odd_count = len(list(filter(lambda x: x % 2 != 0, numbers)))
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

#reversing
numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)

#dulicates removing from list
list1=[1,2,3,12,1,3,4,5,6,7,8,9,9,8,7,6,5,4,]
list1.pop()
print(list1)

#. Sort a list of strings by length.
words = ["apple", "banana", "kiwi", "grape", "orange"]
sorted_words = sorted(words, key=len)
print("Sorted by length:", sorted_words)

#Find the second largest number in the list.
numbers = [10, 20, 4, 45, 99, 99]
unique_numbers = sorted(set(numbers))
if len(unique_numbers) >= 2:
    second_largest = unique_numbers[-2]
    print("Second largest number:", second_largest)
else:
    print("List doesn't have enough unique elements.")

#Find sum of all nested list elements.
nested_list = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
total = 0
for sublist in nested_list:
    for item in sublist:
        total += item
print("Sum of all nested elements:", total)

#Check if two lists are equal.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
if("list1 == list2"):
     print("True") 
else:
    print("False")

#Merge two lists and sort them.
list1 = [5, 2, 9]
list2 = [1, 3, 8]
merged_sorted_list = sorted(list1 + list2)
print("Merged and sorted list:", merged_sorted_list)

#Convert tuple to list and back.
my_tuple = (1, 2, 3, 4)
my_list = list(my_tuple)
print("List:", my_list)

new_tuple = tuple(my_list)
print("Tuple:", new_tuple)

#Check if the tuple contains a value.
my_tuple = (10, 20, 30, 40, 50)
value = 30
if value in my_tuple:
    print(f"{value} is in the tuple.")
else:
    print(f"{value} is NOT in the tuple.")

#Unpack a tuple into variables
my_tuple = (10, 20, 30)
a, b, c = my_tuple
print("a =", a)
print("b =", b)
print("c =", c)

#Create a list of squares using comprehension.
squares = [x**2 for x in range(1, 11)] 
print("List of squares:", squares)

#Count how many times a number appears in a list.
numbers = [1, 2, 3, 2, 4, 2, 5]
target = 2
count = numbers.count(target)
print(f"{target} appears {count} times in the list.")

#Find index of element in tuple.
my_tuple = (10, 20, 30, 40, 50)
element = 30
index = my_tuple.index(element)
print(f"Index of {element} in tuple:", index)

#Slice a tuple from index 1 to 3.
my_tuple = (10, 20, 30, 40, 50)
sliced_tuple = my_tuple[1:3]
print("Sliced tuple:", sliced_tuple)

#Replace element in list with another
my_list = [10, 20, 30, 40, 50]
old_value = 30
new_value = 99
if old_value in my_list:
    index = my_list.index(old_value)
    my_list[index] = new_value
    print("Updated list:", my_list)
else:
    print(f"{old_value} not found in the list.")

#Filter only strings from mixed lists.
mixed_list = [1, "apple", 3.14, "banana", 42, "cherry"]
strings_only = [item for item in mixed_list if isinstance(item, str)]
print("Strings only:", strings_only)

#Take input of the list from the user and print sum.
user_input = input("Enter numbers separated by space: ")
numbers = list(map(int, user_input.split()))
total = sum(numbers)
print("Sum of the list elements:", total)
#vowelcount
list1=["hi","divyav","chitti","king","queen"]
def vowelcount(ip):
    count=0
    for x in ip:
        if(x in ["a","e","i","o","u"]):
          count+=1
    if(count%2==0):
        return True 
    else:
        return False 
op1=[x.upper() for x in list1 if vowelcount(x)]
print(op1)  
#comprehensions
op=[x for x in range(1,10)]
print(op)
#comprehensions
op=[x for x in range(1,20)]
print(op)

#list of sqares using comprehensions 1 to 20
op=[x**2 for x in range(1,21)]
print(op)

list=["chitti","divya","cryso","sneha","asha"]
op=[x.upper() for x in list]
print(op)
#squares of even numbers from 10 to 31 using comprehensions
op=[x**2 for x in range(10,31) if x%2==0]
print(op)
#
list1=["hi","divyav","chitti","king","queen"]
op1=[x.upper() for x in list1 if len(x)%2==0]
print(op1)

#perfect number
num=int(input("enter the number:"))
sum=0
for x in range(1,num):
    if(num%x==0):
        sum+=x
if(sum==num):
    print("it is a perfect number")
else:
    print("it is not a prime number") 
  

#problems on int()
#convert float() into int()
value=4.89
print(int(value))
#string to int and multiply with 5
value1="7"
result=int(value1)*5
print(result)
print(type(result))
#problems on float()
#convert an integer input to float
num=30
result=float(num)
print(result)
#convert string "3.1415" to float and add 1
value="3.1415"
result=float(value)+1
print(result)
#problems on complex()
#create a complex number from real and imaginary inputs
real_part=30
imaginary_part=20
x=complex(real_part, imaginary_part)
print(x)
#return sqare of a complex number using complex()
x=complex(2,3)
sqare=x**2
print(sqare)
#problems on round()
#round 6.72849 to 2 decimal places
x=6.72849
print(round(x, 2))
#round user-input float to nearest integer
num=float(input("enter the  float number: "))
print(int(round(num)))
#problems on min() max()
#find min and max from [2,5,1,9,-3,6]
x=[2,5,1,9,-3,6]
print(min(x), max(x))
#find the  largest of three numbers using max()
x=30
y=35
z=25
largest=max(x,y,z)
print("largest number is:", largest)
#find alphabetically first name from ["Zara","Bob","Alice"]
names=["Zara","Bob","Alice"]
first_name=min(names)
print("alphabetically first name is:",first_name)
#problems on pow()
#find 2**5 using pow()
a=2
b=5
print(pow(a,b))
#get base and exponent from user, return result
base=float(input("enter the float number:"))
exponent=float(input("enter the float number:"))
result= base**exponent
print(result)
#use pow(x,y,z) to find (x**y)%z with inputs x=2, y=3, z=5
x=2
y=3
z=5
print(pow(x,y,z))
#problems on divmod()
#use divmod() for 23 divided by 5
a=23
b=5
print(divmod(a,b))
#write function to return quotient and  remainder
quotient , remainder= divmod(23,5)
print(quotient, remainder)
#convert number to binary using repeated divmod(num,2)
def to_binary(num):
    if num == 0:
        return "0"
    bits = []
    while num > 0:
        num, remainder = divmod(num, 2)
        bits.append(str(remainder))
    bits.reverse()
    return ''.join(bits)
number = 23
binary_rep = to_binary(number)
print(f"Binary representation of {number} is {binary_rep}")
#problems on abs()
#print absolute value of a user-input number
a=float(input("enter the value:"))
print(abs(a))
#get absolute difference between two numbers
def absolute_difference(a,b):
 return abs(a-b)
a=10
b=30
print(absolute_difference(a,b))
#compute manhattan distance from (x,y) to origin
def manhattan_distance(x, y):
    return abs(x) + abs(y)
x, y = 3, -4
distance = manhattan_distance(x, y)
print(f"Manhattan distance from ({x},{y}) to origin is {distance}")
#bonus practice
#multiply two string inputs as integers
a=str(input("enter the value:"))
b=str(input("enter the value:"))
result=int(a)*int(b)
print(result)
#round pow(5,3)/7 to 3 decimal places
a= pow(5, 3) / 7
result = round(a, 3)
print(result)
#print largest absolute value from [-2,-8,3,7]
num = [-2, -8, 3, 7]
largest_abs = max(num, key=abs)
print("Largest absolute value:", largest_abs)
#round user float input then use as exponent for 2
input = float(input("Enter a float number: "))
rounded_exp = round(input)
result = 2 ** rounded_exp
print(f"2 raised to the power {rounded_exp} is {result}")


#Generate 5 random floats between 0 and 1.
import random
values= [random.random() for  _ in range(5)]
print(values)
#Dice roll simulator using random.randint.
import random
print(random.randint(1,6))
#Convert 90 degrees to radians.
import math
degrees=90
radians=degrees*(math.pi/180)
print(radians)
#Factorial of a user-given number.
import math
num=int(input("enter the  number:"))
print(math.factorial(num))
#Shuffle a list of 10 integers.
import random
a=[20,30,45,65,73,22,64]
random.shuffle(a)
print(a)
#Lottery draw of 6 unique numbers from 1 to 49.
#Approximate using Monte Carlo.
#Calculate compound interest using math.pow.
#Trigonometry calculator using degrees.
#Roll two dice 1000 times and plot the sum frequency.'''

#
for x in range(1,6):
    line=""
    for y in range(x):
       line = line+"*"
    print(line)


for x in range(1,6):
    line=""
    for y in range(x):
        line=line+str(x)
    print(line) 

for x in range(1,6):
    line=""
    for y in range(x):
        line=line+"*"
    print(line) 

word="chitti"
for x in range(1, len(word)+1):
    line=""
    for y in range(x):
        line+=word[y]
    print(line)  

word="abcde"
for i in range(1, len(word)+1):
    line=""
    for j in range(i):
        line+=word[j]
    print(line)        




fruits=["apple","mango","banana"]
print(fruits[0])
print(fruits[2])
print(len(fruits))
fruits[1]="pineapple"
print(fruits)

x=["harish","naresh","suresh","mahesh"]
print(id(x))
x[2]="kiran"
print(x)
print(id(x))

data=[1,2,[4,5],[6,7],8,["something"]]
print(data[2][0])
print(data[3][0])
print(data[5][0][2])

mixed=[1,2,"hi",12.5,True]
print(mixed)
print(type(mixed))
value=1
value1="hi"
print(type(value))
print(type(value1))

p=int(input("enter the price:"))
t=int(input("enter the time period:"))
r=int(input("enter the rate:"))
si=(p*t*r)/100
print(si)

c=int(input("enter the temperature in celcius:"))
f=(c*9/5)+32
print(f)

a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
average=(a+b+c)/3
print(average)

r=int(input("enter the radius:"))
area=3.14*r**2
print(area)

x=10
def show():
    x=5
    print(x)
show()
print(x)

def outer():
    x=10
    def inner():
        print(x)
    inner()
outer()

x="global"
def outer():
    x="outer"
    def inner():
        x="inner"
    inner()
    print("outer:", x) 
outer()
print("global:", x) 

num=int(input("enter the number:"))
if(num%2==0):
    print("even number")
else:
    print("odd number")

age=int(input("enter the age:"))
if(age<13):
    print("child")
elif(13<=age<20):
    print("teen")
elif(age>=20):
    print("adult")
else:
    print("prime")   

x=int(input("enter the number:"))
if(x>0): 
  if(x%2==0):
    print("number is positive and even") 
  else:
    print("number is positive and odd") 
elif(x<0): 
  if(x%2!=0):
    print("number is negative and odd")
  else:
    print("number is negative and even")
else:
    print("you have entered is zero")

num=int(input("enter the number:"))
if num%3==0 and num%5==0:
    print("number is divisible by both 3 and 5") 
elif num%5==0:
    print("number is divisible by 5")
elif num%3==0:
    print("number is divisible by 3") 
else:
    print("zero/invalid number") 

a=int(input("enter the number:"))
b=int(input("enter the number:"))
if a>b:
    print("the largest number is a",a)
else:
    print("the largest number is b:",b) 

s1=15
s2=10
s3=23
if (s1+s2)>s3 and (s2+s3)>s1 and (s1+s3)>s2:
    print("can form a triangle")
else:
    print("cannot form a triangle") 

x="hello"
for char in x:
    print(char, end="")

sum=0
for i in range(1,11):
    sum+=1
print("sum of first 10 natural numbers are:",sum)

for i in range(1,21):
    if i%2==0:
        print(i)

items=["pen","pencil","eraser"]
for item in items:
    print(item)

list1=["divya","chitti","lite","sneha",]
list2=["divya","chitti","lite","asha",]
for item in list1:
    if item in list2:
        print(item)

my_set={"apple","banana","cherry"}
for item in my_set:
    print(item)
count=0
colors={"red","blue","green","yellow"}
for items in colors:
    count+=1
    print(items)

person={"name":"divya","age":"21","city":"hyd"}
for key, value in person.items():
    print(key,":",value)

count=0
scores={"math": 45,"english": 55,"science": 80,"history": 40}
for value in scores.values():
    if value>50:
        count+=1
        print("number of values greater than 50 are:",count)

data={"a":1,"b":4,"c":6,"d":3}
even_dict={}
for key, value in data.items():
   if value%2==0:
    even_dict[key]=value
    print("dictionary with even values:",even_dict)        
