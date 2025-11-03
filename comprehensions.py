
#creat a list of perfectsqares using comprehension
def perfectsqare(num):
    isperfect=False
    for x in range(1,num):
        if x**2==num:
            isperfect=True
            break
    if(isperfect):
        return True
    else:
        return False
op=[x for x in range(1,101) if perfectsqare(x)] 
print("list of perfect square numbers are:", op)  

#create list of perfectnumbers using comprehensions
def perfectnumber(num):
    sum=0
    for x in range(1,num):
        if num%x==0:
            sum+=x
    if sum==num:
        return True
    else:
        return False
op=[x for x in range(1,101) if perfectnumber(x)]
print("list of perfect numbers are:", op)            

#create list of neon numbers using comprehensions
def neonnumber(num):
    square=num**2
    sum=0
    while(square>0):
        ld=square%10
        sum+=ld
        square=square//10
    if sum==num:
        return True
    else:
        return False     
op=[x for x in range(1,101) if neonnumber(x)]
print("list of neon numbers are:", op) 

#create list of sunny numbers using comprehensions
def sunnynumber(num):
    issunny=False
    for x in range(1,num):
        if (x**2==num+1):
            issunny=True
            break
    if issunny:
        return True
    else:
        return False
op=[x for x in range(1,101) if sunnynumber(x)]
print("list of sunny numbers are:", op)  

#list of prime numbers using comprehensions
def primenumber(num):
    isprime=True
    if num<=1:
        print("please give number greater than 1")
    else:
        for x in range(2,num):
            if num%x==0:
                isprime=False
                break
        if isprime:
            return True
        else:
            return False
op=[x for x in range(2,101) if primenumber(x)]
print("list of prime numbers are:", op) 

#create list of reversed strings using comprehensions
str1=["divya","chitti","cryso","asha"]
reversed_strings=[word[::-1] for word in str1]
print(reversed_strings)

