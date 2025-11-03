x=10
def show():
    x=5
    print(x)
show()
print(x) 

#Above program shows that x=10 value declared as global value and x=5 is declared as local value.
#there is difference in declaring the values

def outer():
    x=10
    def inner():
        print(x)
    inner()
outer()            
#here it will prints 10 when we declare as inner because it declared as local value
#it gives outer when we want to print outer() beacuse we can't declare any value out side 
# of the def outer() function/we can't declare global value

x="global"
def outer():
    x="outer"
    def inner():
       x="inner"
    inner()
    print("outer:",x)
outer()
print("global:",x)
#here we declared a global value so that it will print global value


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
        