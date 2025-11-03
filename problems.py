#amount problem
amount=5725
notes_1000=amount//1000
rem_change=amount-(notes_1000*1000)
notes_500=rem_change//500
rem_change=rem_change-(notes_500*500)
print(notes_1000, notes_500, rem_change)

#car problem

#biggest among 2 numbers
a=500
b=300
if a>b:
    print("a")
else:
    print("b")    

#biggest among 3 numbers
a=500
b=800
c=600
if(a>=b and a>=c):
    print("the biggest number is a")
elif(b>=a and b>=c):
    print("the biggest number is b") 
else:
    print("the biggest number is c")
 
 #check whether the number is even or odd
num=int(input("enter the number:"))
if num %2== 0:
    print("even")
else:
    print("odd") 

#signal program
color=(input("enter the colour:"))
if(color=="red"):
    print("please stop")
elif(color=="orange"):
    print("please wait/ready to go")
elif(color=="green"):
      print("please go")
else:
     print("invalid colour input")

#eamcet rank
eamcetRank=60000
if(eamcetRank<50000):
    print("go and join in cmr")
elif(eamcetRank<70000):
    print("go and join in kakatheeya")    
elif(eamcetRank<85000):
    print("go and join in mallareddy")
elif(eamcetRank<1000000):
    print("go and join in scet")
else:
    print("go and join in degree") 

#user login or not
user="client"
if(user=="admin"):
    print("welcome to admin")
elif(user=="client"):
    print("welcome to client")
else:
    print("go and login")

#functions
def add():
    a=10
    b=20
print(a+b)  

def function_name(a,b):
    print(a+b)
function_name(30,50)

#positional arguments
def items(name,quantity,price=10000):
    print(f"{name},{quantity},{price}")
items("phone",1,10000)    

#perfect sqare
num=25
res=num**0.5
print(res==int(res))

#problems
