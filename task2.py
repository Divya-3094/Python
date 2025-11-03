#conditional statements
#even or odd or positive or negative
n=int(input("enter your number:"))
if n%2==0:
    result="even"
else:
    result="odd" 
if n>0:
    sign="positive"
elif n<0:
    sign="negative"
else:
    sign="zero"
print(f"the number is {result} and {sign}.")  

#age group classifier
a=int(input("enter the age:"))
if a<=12:
    print("kids")
elif a<=20:
    print("teenage")
elif a<=40:
    print("young")
elif a<=60:
    print("prime")
else:
    print("senior")                 


#grade evaluation
m1=int(input("enter the sub1 marks: "))
m2=int(input("enter the sub2 marks: "))
m3=int(input("enter the sub3 marks: "))
m4=int(input("enter the sub4 marks: "))
m5=int(input("enter the sub5 marks: "))
m6=int(input("enter the sub6 marks: "))
t1=m1+m2+m3+m4+m5+m6
p=(t1/600)*100
print(p)
if p>=90:
    print("A grade")
elif p>=80:
    print("B grade")    
elif p>=70:
    print("C grade")
elif p>=60:
    print("D grade")
else:
    print("fail")            


#triangle type checker
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))
 
if(a==b==c):
    print("we can form equilant triangle")
elif((a==b)or(b==c)or(c==a)):
    print("wecan form isosceles triangle")
elif(a!=b!=c):
    print("we can form scalene triangle")
elif(((a+b)>=c)or((b+c)>=a)or((c+a)>=b)):
    print("we can form inequality triangle")
else:
    print("cannot form a triangle")        


#ATM withdrawl simulator
balence=30000
withdraw=int(input("enter withdraw amount: "))
if(balence>withdraw):
   if(withdraw%100==0):
        print(f"rupees(withdraw) succesfully withdrawn")
elif(withdraw*100): 
        print("withdraw amount should be mulltiples of 100")
else:
    print("insufficient balance")   

#functions

