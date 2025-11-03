#functions
def add(a,b):
  print(a+b)  
add(53,1000)  

def function_name(a,b):
    print(a+b)
function_name(10,20)  
#positional arguments
def details(name, age):
    print(name)
    print(age)
details(20,"divya")   
#keyword arguments
def details(name,id): 
  print(name)
  print(id)
details(name="divya",id=20)  
#default arguments
def details(name, batch):
    print(name)
    print(batch)
details("chitti",53)    
#perfect sqare
num=25
res=num**0.5
print(res==int(res))
# *args
def add(*numbers):
   print(numbers)
add(1,2,3,4,5,6,7,8,9,10)   

def add(*numbers):
   print(sum(numbers))
add(1,2,3,4,5,6,7,8,9,10)  

def stationary(*price):
  print(sum(price))
  print(len(price))
stationary(5,67,87,90,12)  

def stationary(*prices):
  print("total count of items:",len(prices))
  print(sum(prices))
stationary(10,20,30,40,50)  

def details(*details, batch):
  print(details)
  print(batch)
details("divya",10,"python", batch=53)  
# **arguments
def details(name, batch, cource):
    print(f"{name} from {batch} batch my cource is {cource}")
details(name="divya",batch=53,cource="python")    
#functions
def my_function():
  print("hello i am from hyderabad")
my_function()
#return function
def add(a,b):
   return a+b
result=add(50,50)
print(result)  
#function with parameters
def greet(name):
  print("hello" + name) 
greet("chittidivya")  

def greet(name="guest"):
  print("hello"+ name)
greet()  
#arbitary arguments
def my_function(*kids):
  print("the youngest child is" + kids[2])
my_function("chintuu","pinkyy","sweetyy")  
#keyword arguments
def my_function(child1,child2):
  print("the youngest child is" + child1)
my_function(child1="divya", child2="chittii")  
# **kwargs
def my_function(**kids):
  print("his last name is"+ kids["lname"])
my_function(fname="divya", lname="chittii")  
#recursion
def factorial(n):
  if n==1:
    return 1
  else:
    return n*factorial(n-1) 
print(factorial(5))  

#problems
num=int(input("enter the number:"))
if num>0:
  if num%2==0:
    print("given number is positive and even")
  else:
    print("given number is positive and odd")
elif num<0:
  if num%2==0:
    print("given number is negative and even")
  else:
    print("given number is negative and odd")
else:
  print("given number is zero")  
#age group classifier
age=int(input("enter the age:"))
if age<=12:
  print("kids")
elif age<=19:
  print("teenage")
elif age<=40:
  print("young")
elif age<=59:
  print("prime")
elif age>=60:
  print("senior") 
else:
  print("dead")                 
#grade evaluation
s1=int(input("enter the sub1 marks:"))
s2=int(input("enter the sub2 marks:"))
s3=int(input("enter the sub3 marks:"))
s4=int(input("enter the sub4 marks:"))
s5=int(input("enter the sub5 marks:"))
s6=int(input("enter the sub6 marks:"))
t1=s1+s2+s3+s4+s5+s6
p=(t1/600)*100
print(p)
if p>=90:
   print("A grade")
elif p>=89:
  print("B grade")
elif p>=79:
  print("C grade")  
elif p>=69:
  print("D grade")
elif p<60:
  print("fail")
else:
  print("invalid input")  
#triangle type checker
a=int(input("enter value a:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if (a==b==c):
  print("we can form equilatoral triangle")
elif (a==b) or (b==c) or (c==a):
  print("we can form isosles triangle")
elif (a!=b!=c):
  print("we can form scalane triangle")
elif ((a+b)>=c) or ((b+c)>=a) or ((c+a)>=b):
  print("inequality triangle")
else:
  print("cannot form a triangle")    
#atm withdrawl
balance=25000
withdraw=int(input("enter withdrawl amount:"))
if(balance>withdraw):
  if(withdraw%100==0):
     print(f"rupees {withdraw} sucessfully withdrawn")
  else:
    print("withdraw amount should be multiples of 100 only")
else:
  print("insufficient balance")

#problems based on functions
def great():
  return ("hello how are you")
print(great())    

def mul(a,b):
  mul=a*b
  return mul
print(mul(50,50))

def add(a,b):
  add=a+b 
  return add
print(add(46,66))  

def sub(a,b):
  sub=a-b 
  return sub
print(sub(45,30))   

def div(a,b):
  div=a/b 
  return div
print(div(30,25))

def calculator(a,b,op):
  if(op=='+'):
     return a+b 
  elif(op=='-'):
     return a-b 
  elif(op=='*'):
     return a*b 
  elif(op=='%'):
     return a%b 
  else:
    return ("invalid syntax")
print(calculator(100,23,'%'))   


