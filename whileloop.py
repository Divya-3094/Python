#while loop
n=int(input("enter the number:"))
n1=n
sum=0
p=(n)
while n>0:
    l1=n%10
    sum+=l1**p
    n=n//10
if sum==n1:
    print("It is Armstrong number")  
else:
    print("It is not a Armstrong number")   

def mul(a,b):
    mul=a*b
    return mul
print(mul(2,6))

def add(a,b):
    add=a+b
    return add
print(add(2,5))

def calculator(a,b,op):
    if(op=="+"):
        return a+b
    elif(op=="_"):
        return a-b
    elif(op=="*"):
        return a*b
    elif(op=="/"):
        return a/b
    else:
        return "invalid operator"   
print(calculator(2,5,"*"))  

data=1,2,3,4,5
print(data)
a,b,c,d,e=data
print(a)
print(b)

num="123456789"
cnvrt=str(num)
for x in cnvrt:
    print(x)
for x in range(len(cnvrt)-1-1-1):
    print(cnvrt[x], end=" ")    
    
num=125
sum=0
while(num>0):
    ld=num%10
    sum+=ld
    num=num//10
print(sum)

num=125
sum=0
while(num>0):
    ld=num%10
    sum+=ld**2
    num=num//10
print(sum)

num=12345
count=0
while(num>0):
    ld=num%10
    count+=1
    num=num//10
print(count)

num=123456
num1=num
rev=0
while(num>0):
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev)
if(num1==rev):
    print("number is a palindrome")
else:
    print("number is not a palindrome")    
if(num1%10!=rev):
    print("number is a palindrome")
else:
    print("number is not a palindrome") 
    


#reverse a number using while loop
num=123456
rev=0
while num>0:
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev)    

num=12345654321
num1=num
rev=0
while num>0:
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev) 
if (num1==rev):
    print("given number is palindrome")
else:
    print("given number is not a palindrome")

num=123456
num1=num
if num%10!=0:
    rev=0
    while num>0:
        ld=num%10
        rev=rev*10+ld
        num=num//10
    print(rev)
    if num1==rev:
        print("palindrome")
    else:
        print("not palindrome")
else:
    print("given number which are not divisible by 10 because we cannot check for palindrome")

num=int(input("enter the number:"))
sum=0
temp=num
n=len(str(num))
while(temp>0):
    digit=temp%10
    sum+=digit**n
    temp=temp//10
print(sum)
if sum==num:
    print("armstrong")
else:
    print("not armstrong")       

num=int(input("enter the number:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
        else:
            print("prime")
            break
else:
    print("invalid syntax")    
 
num=123456
rev=0
while num>0:
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev)         

num=int(input("enter the number:"))
sum=0
temp=num
n=len(str(num))
while(temp>0):
    digit=temp%10
    sum+=digit**n
    temp=temp//10
print(sum)
if sum==num:
    print("armstrong")
else:
    print("not armstrong") 

num=123454321
num1=num
rev=0
while num>0:
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev)
if num1==rev:
    print("palindrome")
else:
    print("not palindrome")  
       