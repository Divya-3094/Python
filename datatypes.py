#datatypes
fruits=["banana","apple","mango",]  #collection of strings, list of fruits
ids=[1,2,3,4,5]                     #collection of integers, list of ids
prices=[123.5,35.6,346.8,76.9]      #collection of floting values, list of prices
mixed=[2,5,32.5,"divya",True,]
print(type(fruits))
print(type(ids)) 
print(type(prices))
print(type(mixed))

print(fruits[1])
print(ids[-2])
print(prices[3])
print(mixed[3][0])
print(len(fruits))
print(len(ids))
print(len(prices))
print(len(mixed))

#print lenth of the fruits collectin is 3

print(f"length of the fruits collection is {len(fruits)}")
print(fruits[len(fruits)-1])

a="divya"
print(id(a))
a="chitti"
print(id(a))

x=["divya","chitti","lite","sneha"]
print(x)

x[2]="cryso"
print(id(x))

x=[1,3]+[4,5]
print(x)

list=[2,3,8,33.2,"chitti",8+3j,True,[2,7,8,9],66]
op=list+["python"]+[28]
print(op)

str="hello"
print(str[-1])
str1="welcome"
op=str+str1+"[okok]"
print(op)

ip=[1,2,35.6,[3,45],[32,67],"something"]
print(ip[5][2]) 


#check if number is prime number or not using functions
def is_prime(n):
  if n<=1:
    return False
  for i in range(2,n):
    if n%i==0:
       return False
  return True
n1=int(input("enter the value:"))
print(is_prime)  


count=0
for i in range(n1,n1+1):
   if is_prime(i):
     count+=1
print(count)     

n1="0111"
n2="0100"
sum=0
j=0
for i in range(len(n1)-1,-1,-1):
    sum+=int(n1[i]*(2**j))
    j+=1
k=0
for i in range(len(n2)-1,-1,-1):
    sum+=int(n2[i]*(2**k))
    k+=1
print(str(bin(sum))[2:])    

name="sraaavan"
result=name[0]
c=1
for i in range(1,len(name)):
    if name[i]==name[i-1]:
        c+=1
        if c<3:
            result+=name[i]
    else:
        c=1
        result+=name[i]
print(result)      
#chocklates problem
a=21
t_c=a
w=a
while w>=3:
    e=w//3
    t_c+=e
    w=e+w%3
print(t_c)    

