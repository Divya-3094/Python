#problems on loop
#print numbers 1 to 10 using loop
for i in range(1,11):
    print(i)
#print even numbers from 1 to 20  
for i in range(1,21):
  if i%2==0:
    print(i,end=",")   
#Print odd numbers from 1 to 20.
for i in range(1,21):
  if i%2!=0:
    print(i, end=",")
#Calculate the sum of numbers from 1 to 100.
total=sum(range(1,101))
print(total)
#Print multiplication table of 5.
def mul(num):
    for x in range(1,11):
      print(f"{num} x {x} = {num*x}")
mul(5)      
#Print all numbers divisible by 3 up to 50.
for i in range(1,51):
    if i%3==0:
        print(i, end=" ")
#Calculate the factorial of a number using a loop
num=int(input("enter the number:"))
factorial=1
if num<0:
    print("give positive number")
else:
    for i in range(1, num+1):
     factorial*=i 
print(f"factorial of a {num} is {factorial}.")        
#Reverse the digits of a number using a loop.
num=int(input("enter the number:"))
reversed_num=0
original_num=num
temp=abs(num)
while temp!=0:
    digit=temp%10
    reversed_num=reversed_num*10+digit
    temp=temp//10
print(reversed_num)
#Print squares of numbers from 1 to 10.
for i in range(1,11):
    print(i**2)
#Count the number of digits in an integer.
def count_digits(n):
  return len(str(n))
value=int(input("enter the value:"))
print(count_digits(value))  
#Find the sum of digits of a number.
sum=0
value=str(input("enter the value:"))    
for i in value:
    sum+=i
    print(sum)
#Print powers of 2 up to 2^10.
for i in range(1,11):
    print(f"2^{i}={2**i}")
#Check if a number is prime using a loop.
num=int(input("enter the number:"))
if num>0:
    for i in range(2,num):
        if num%i==0:
            print("not a prime number")
            break
        else:
            print("prime number")
            break
else:
    print("invalid number")                    
#Print first 10 natural numbers using while loop.
i=1
while i<=10:
    print(i)
    i+=1
#Count down from 10 to 1 using a loop.
for i in  range(10,0,-1):
    print(i)
#Find product of all numbers from 1 to 10.
product=1
for i in range(1,11):
    product*=i
    print(product)
#Print numbers from 1 to 100 in steps of 5.
for i in range(1,101,5):
    print(i)
#Find numbers between 1 to 50 divisible by both 3 and 5.
for i in range(1,51):
    if i%3==0 and i%5==0:
        print(f"divisible by both 3 and 5 is {i}")
#Print all prime numbers between 1 to 50.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
for num in range(1, 51):
    if is_prime(num):
        print(num)
#Display the reverse of an integer.
x=int(input("enter the value:"))
reverse=str(x)[::-1]
print(reverse)
#Find the smallest digit in a number.
x=str(input("enter the value:"))
smallest=min(x)
print(smallest)
#Find the largest digit in a number.
x=int(input("enter the value:"))
y=str(x)
largest=max(y)
print(largest)
#Print pattern: 1 2 3, 4 5 6, 7 8 9
for x in range(1,10):
    str=0
    for y in range(x+1):
        str=str*10+y
    print(str) 
#Print pattern of stars in triangle format.
for x in range(1,6):
    line=""
    for y in range(x):
        line+="*"
print(line)
#Print sum of odd digits in a number.
num=(input("enter the number:"))
sum=0
for x in num:
    if int(x)%2==0:
       sum+=int(x)
print(sum)
#Print table of a given number.
def mul(n):
    for x in range(1,11):
        print(f"{n} x {x} = {n*x}")
mul(12)        
#Count how many times a digit occurs in a number.

#Sum of squares of digits of a number.
x=input("enter the number:")
sum=0
for digit in x:
    op=(int(digit)**2) 
    print(op)
    sum+=op
print("sum of the sqares of digits is:", sum)
#Sum of cubes of digits of a number.
y=input("enter the number:")
sum=0
for digit in y:
    op=(int(digit)**3)
    print(op)
    sum+=op
print("sum of cubes of digits is:",sum)    
#Print sum of even digits in a number.
z=input("enter the number:")
sum=0
for digit in z:
   if int(digit)%2==0:
      print(digit)
      sum+=int(digit)
print("sum of even digits is:",sum)   
#Count multiples of 3 between 1 and 100.
count=0
for i in range(1,101):
    if i%3==0:
        print(i, end=" ")
#Print 10, 20, 30... up to 100.
for i in range(0,100,10):
   print(i, end=" ")
#Print reverse of a number using while loop.
num=123456
rev=0
while(num>0):
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev) 
#Find if number is Armstrong number (3-digit only)
num=int(input("enter the number:"))
n=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**n
    temp//=10
if num==sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")    
#Print Fibonacci series up to n terms.
num=int(input("enter the number:"))
a=0
b=1
count=0
while (count<num):
    print(a," ",end="")
    temp=a+b 
    a=b 
    b=temp
    count+=1      
#Print GCD of two numbers using loop.

#Print LCM of two numbers using loop.
#Display all even digits in a number.
num=input("enter tha value:")
for digit in num:
    if int(digit)%2==0:
        print(digit)
#Display all odd digits in a number.
num=input("enter the number:")
for digit in num:
    if int(digit)%2!=0:
       print(digit)
#Print the ASCII values from 65 to 90.
for i in range(65,90):
    print(f"{i} - {chr(i)}")






