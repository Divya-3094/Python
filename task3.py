#palindrome
str="madam"
rev=str[::-1]
if str==rev:
    print("palindrome")
else:
    print("not palindrome") 

#write a program to reverse a num without converting into string
num=int(input())
while(num>0):
    rem=num%10
    num=num//10
    print(rem, end="")



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

#print perfect numbers using comprehensions.

#print neon numbers using comprehensions
def neonnumbers(n):
    sqare=n*n
    digit_sum=sum(int(digit) for digit in str(sqare))
    digit_sum=n
print(digit_sum)
#print sunny numbers using comprehensions
#print perfect sqares using comprehsions 

x=15
if x%3==0 and x%5==0:
    print("FizzBuzz")

list=[1,2,3]
print(len(list))
list.append(4)
print(list[-1])

def compare(a,b):
    if a>b:
        return "A"
    else:
        return "B"
print(compare(7,5)) 

a=[0]*3
a[1]=5
print(a)

for i in range(1,4):
    for j in range(1,i+1):
        print(j, end=" ")
    print()    

x=1
y=2
x,y=y,x
print(x,y)    

def calc(n):
    return n*n 
print(calc(5))   

a="hello"
print(a.upper())

x=3
while x>0:
    print(x)
    x-=1 

def show():
    print("inside function")
show()
print("outside function")      

n=15
if n%3==0 and n%5==0:
    print("multiples of both")
elif n%5==0:
    print("multiples of 5") 
elif n%3==0:
    print("multiples of 3")
else:
    print("none")    

user=input("enter the value:")
op=reverse=user[::-1]
print(op)

x="1234543214"
rev=x[::-1]
if x==rev:
    print("it is a palindrome")
else:
    print("not a palindrome")



# Sum of even numbers using list comprehension
even_sum = sum(num for num in a if num % 2 == 0)

print("Sum of even numbers:", even_sum)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum=sum(num for num in a if num%2==0)
print(even_sum)
#right angle triangle
for x in range(1,6):
    str=0
    for y in range(x):
        str=str*10+x
    print(str) 
#right angle triangle 
for x in range(1,6):
    line=""
    for y in range(x):
        line+="*"
    print(line)     
#right angle triangle
for x in range(1,6):
    str=0
    for y in range(x+1):
        str=str*10+y
    print(str) 
#right angle triangle aschii numbers
for x in range(97,102):
    str=""
    for y in range(97,x+1):
        str+=chr(x)
    print(str)    
#right angle triangle using string
word="chitti"
for x in range(1, len(word)+1):
    line=""
    for y in range(x):
        line+=word[y]
    print(line)  
#right angle triangle using numbers in string
word="1491625"
for x in range(1,len(word)+1):
    line=""
    for y in range(x):
        line+=word[y]
    print(line)  
#rignt angle triangle using string
str="something"
op=""
for i in str:
    op+=i 
    print(op)  

for x in range(1,6):
    str=0
    for y in range(1,x):
       str=str*10+y
    print(str)   
#reverse right angle triangke stars
for x in range(5,0,-1):
    line=""
    for y in range(x):
        line+="*"
    print(line) 
#reverse right angle triangle numbers
for x in range(5,0,-1):
    str=0
    for y in range(x+1):
        str=str*10+y
    print(str) 
