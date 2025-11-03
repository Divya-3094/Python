n=[1,2,3]
n.insert(10,5)
print(n)


maths=40
physics=45
chemistry=20


studentMarks=35
if(studentMarks>=35):
    print("student passed in maths")
elif(studentMarks>=35):
    print("student passed in physics")
elif(studentMarks>=35):
    print("student passed in chemistry")
else:
    print("student is failed")


amount=5725
notes_1000=amount//1000    #5
rem_change=amount-(notes_1000*1000)
notes_500=rem_change//500    #1
rem_change=rem_change-(notes_500*500)
print(notes_1000, notes_500, rem_change)


num=25
res=num**0.5
print(res==int(res)) 


num=77
res=num**0.5
print(res==int(res))
                     


num=int(input("enter the number:"))
if num>0:
    if num%2==0:
        print("number is even and positive")
    else:
        print("number is odd and positive")
elif num<0:
    if num%2==0:
        print("number is even and negative")
    else:
        print("number is odd and negative")
else:
    print("the number is zero")            


age=int(input("enter the age:"))
if age<=12:
    print("kid")
elif age<=19:
    print("teenage")
elif age<=40:
    print("young")
elif age<=59:
    print("prime")
elif age>60:
    print("senior")
else:
    print("dead")                    


s1=int(input("enter sub1 marks:"))
s2=int(input("enter sub2 marks:"))
s3=int(input("enter sub3 marks:"))
s4=int(input("enter sub4 marks:"))
s5=int(input("enter sub5 marks:"))
s6=int(input("enter sub6 marks:"))
T=s1+s2+s3+s4+s5+s6
p=(T/600)*100
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
    print("invalid syntax")  


a=int(input("enter value a:"))
b=int(input("enter value b:")) 
c=int(input("enter value c:"))
if (a==b==c):
    print("equilateral triangle")
elif ((a==b) or (b==c) or (c==a)):
    print("isosceles triangel") 
elif (a!=b!=c):
    print("scalen triangle")
elif ((a+b)>=c or (b+c)>=a or (c+a)>=b):
    print("iniquality triangle")
else:
    print("cannot form a triangle")      


balence=25000
amnt_withdraw=int(input("enter withdraw amount:"))
if (balence>amnt_withdraw):
    if (amnt_withdraw*100==0):
        print(f"rupees {amnt_withdraw} successfully withdrawn")
    else:
        print("withdraw amount should be multiples of 100")
else:
    print("insufficient balance")    
        

def greet():
    print("hello, how are you?")
greet()                                            

def greet():
    return "hello, how are you?"
print(greet())       


def greet(stud_name="divya", branch="engineering"):
    print(f"hello {stud_name}, hope you are dong good in {branch} program")
greet() 


st=input("enter student name:")
br=input("enter branch name:")
greet(st,br)


op=lambda:"hi"
print(op) 


for x in range(1,11):
    print(f"2 x {x} = {2*x}")

def mul(n):
    for x in range(1,11):
        print(f"{n} x {x} = {n*x}")  
mul(10)          


for x in range(1,11):
    print(x**2)

for x in range(1,11):
    if(x%2==0):
        print(x**2, "sqares")
    else:
        print(x**3, "cubes") 


for x in range(1,21):
    if(x%2 and x%3):
        print(f"{x}-fizzbuzz")
    elif(x%3==0):
        print(f"{x}-buzz")
    elif(x%2==0):
        print(f"{x}-fizz")
    else:
        print("invalid")  


sum=0
for x in range(1,11): 
    sum+=x
print(sum, end=" ") 

sum=0
for x in range(1,11):
      y=x**2
      sum+=y
print(sum, end=" ")

for x in range(2,21):
    if(x%2==0):
        print(x, end=" ") 

for x in range(1,100):
    if x%2!=0:
        print(x,end=" ") 

for x in range(1,51):
    if(x%5==0):
        print(x, end=" ")

for i in range(1,51):
    if(i%5==0 and i%3==0):
        print(i, "multiples of both 5 and 3")
    elif(i%5==0):
        print(i,"multiples of 5")
    elif(i%3==0):
        print(i, "multiples of 3") 
else:
    print("multiples of none")   

count=0
for i in range(1,101):
    if i%3==0 and i%7==0:
        print(i)
        count+=1
print(f"{count} numbers divisible by 3 and 7")                    

str1="DivyAChiTtIKaNapALa"
count1=0
count2=0
for char in str1:
    if char.isupper():
        print(char,"is upper case")
        count1+=1
    else:
        print(char,"is lower case")
        count2+=1
print("we have upper case letters",count1)
print("we have lower case letters",count2)      

for x in range(1,101):
    if (x**0.5).is_integer():
        print(x, end=" ")

for num in range(2,101):
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num,end=" ")

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
for num in range(1,101):
    if is_prime(num):
        print(num,end=" ")  


for i in range(5):
    if i+1==3:
      break
    print("i:",i)
    print("loop ended")

s=""
for i in range(4):
    if i%2==0:
      s="A"
    else:
      s+="B"
      print(s)  

word="python3"
print(word[1:4]+word[-1]+word[:1])                 

word=[1,2,3,4,5]
print(str(word[1:4])+str(word[-1])+str(word[:1]))

result=(3+4)*2**2-5
print(result)

list1=[1,2,3,4,5,6,7,8,9,10]
count1=0
count2=0
for num in list1:
   if num%2==0:
      count1+=1
   else:
      count2+=1
print("number of even numbers are:",count1)
print("number of odd numbers are:",count2)  

list1=[23,43,28,57,12,11]
x=list[0]
for i in list1:
   if i>x:
      x=i
      print(i)
      

str1="TENET"
palindrome=True
for i in range(len(str1)//2):
    if str1[i]!=str1[-(i+1)]:
        palindrome=False
        break
if palindrome:
    print("string is palindrome")
else:
    print("string is not a palindrome")

str1="madam"
rev=str1[::-1]
if str1==rev:
    print("palindrome")
else:
    print("not a palindrome")   

str1="MADAM"
palindrome=True
for i in range(len(str1)//2):
    if str1[i]!=str1[-(i+1)]:
        palindrome=False
        break
if palindrome:
    print("palindrome")
else:
    print("not a palindrome") 

str1="abc123xyz456" 
sum=0
for i in str1:
    if i in "0123456789":
        sum+=int(i)
print(sum)     

list1=[1,2,3,1]
empty=[]
for i in list1:
    if i not in empty:
        empty.append(i)
print(empty)  

list1=["javascript","python","html","css","java","sql","hello","hi"]
for i in range(len(list1)-1-1-1):
    print(list[i])

for x in list1:
    print(x[0])

for x in list1:
    if (len(x)%2==0):
        print(x) 
sum=0
for x in range(1,101):
    if x%2==0:
        print(x,end=" ")
        sum+=x
print("the number of all even numbers from 1 to 100 are:", sum) 

num=int(input("enter the number:"))
fact=1
for i in range(1,num):
    fact*=i
    print("the factorial of the number is :",fact)

for i in range(1,51):
    ps=i**0.5
    if (ps==int(ps)):
        print(i,"is a perfect sqares")

for x in range(1,10):
    print(x)
    if x==5:
        break 

for x in range(1,10):
    if x==5:
        continue
    x+=1
    print(x)   

stops=["kphb","srnagar","ameerpet","paradise","paradeground","kukatpally"]
for stop in stops:
    if(stop=="paradise"):
        continue
    print(stops)

list1=[4,6,8,912,34,56]
for x in list1:
    print(x) 

list1=[4,6,8,912,34,56] 
x=0
while(x<len(list1)):
    print(list1[x])
    x+=1  

for x in range(1,11):
    print(x)
y=1
while(y<=10):
    print(y)
    y+=1        

flashsale=True
while(flashsale):
    print("do shopping with more offers")  
    break  

x=1
while(x<=20):
    if(x%2==0):
     print(x)
     x+=1

num=1
while(num<=20):
   if(num%2==0):
      print(num)
      num+=1  

x1=["a","b","c","d","e"]
for x in range(len(x1)-1,-1,-1):
    print(x1[x])

str1="hello"
for char in range(len(str1)-1,-1,-1):
    print(str1[char],end="")
    
str1="olleh"
for char in range(len(str1)-1,-1,-1):
    print(str1[char],end="")  

#reverse a string
str1="TENET"
op=""
for char in range(len(str1)-1,-1,-1):
    op+=str1[char]
print(op)    
if(op==str1):
    print("it is a palindrome")
else:
    print("not a palindrome")  
#reverse the number
num=123456789
cnvrt=str(num)
for x in cnvrt:
    print(x)
for x in range(len(cnvrt)-1,-1,-1):
    print(cnvrt[x],end="")  
    
#reverse a number 
num=123456
cnvrt=str(num)
while(num>0):
    ld=num%10
    print(ld)
    num=num//10
print(num)    
#sum of the all digits in a number
num=125
sum=0
while(num>0):
    ld=num%10
    sum+=ld
    num=num//10
print(sum)       
#sum of sqares of all digits in a number
num=125
sum=0
while(num>0):
    ld=num%10
    sum+=ld**2
    num=num//10
print(sum)    
#count of total digits in a number using while loop
num=123456
count=0
while(num>0):
    ld=num%10
    count+=1
    num=num//10
print(count) 
#reverse a num using while loop
num=123456
rev=0
while(num>0):
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev)

num=12345654321
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
#
num=123456
num1=num
if(num%10!=0):
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
else:
    print("given number which are not divisible by 10 beacuse we cannot check for palindrome``")               
#check given number is armstrong or not
num=int(input("enter the number:"))
sum=0
temp=num
n=len(str(num))
while(temp>0):
    digit=temp%10
    sum+=digit**n
    temp=temp//10
if (sum==num):
    print("number is armstrong")
else:
    print("number is not armstrong") 

#prime number code
num=int(input("enter the number:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("not prime number") 
            break
        else:
            print("prime number")
            break
else:
    ("invalid syntax")  
#palindrome
num=int(input("enter the number:"))
temp=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev) 
if(temp==rev):
    print("palindrome")
else:
    print("not palindrome")         

