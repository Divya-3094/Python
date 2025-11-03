# #creating single or static object from class
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# obj1=person("chittii",25)
# print(obj1.name)
# print(obj1.age)
# # creating dynamic or multiple objects from class
# class person:
#     def __init__(self,name,gender,age):
#         self.name=name
#         self.gender=gender
#         self.age=age
# obj_chitti=person("chitti","male",25)
# obj_divya=person("divya","female",21) 
# print(obj_chitti.name)
# print(obj_chitti.gender)
# print(obj_chitti.age)
# print(obj_divya.name)  
# print(obj_divya.gender)
# print(obj_divya.age)   
# #creating dynamic objects
# class Application:
#     def __init__(app,name,color,usage):
#         app.name=name
#         app.color=color
#         app.usage=usage
#     def purpose(self):
#         print("social media purpose")   
# insta=Application("instagram","pink","entertainment")   
# zomato=Application("zomato","red","food") 
# rapido=Application("rapido","yellow","travelling")
# print(insta.name)  
# print(insta.color)
# print(insta.usage)
# insta.purpose()     
# print(zomato.name)  
# print(zomato.color)
# print(zomato.usage)  
# zomato.purpose()   
# print(rapido.name)  
# print(rapido.color)
# print(rapido.usage)
# rapido.purpose()     

# class Application:
#     def __init__(app,name,color,usage):
#         app.name=name
#         app.color=color
#         app.usage=usage
#     def purpose(self,app_name,purpose):
#         print(f"{app_name} is used for {purpose}")   
# insta=Application("instagram","pink","entertainment")   
# zomato=Application("zomato","red","food") 
# rapido=Application("rapido","yellow","travelling")
# print(insta.name)  
# print(insta.color)
# print(insta.usage)
# insta.purpose("instagram","socialmedia")     
# print(zomato.name)  
# print(zomato.color)
# print(zomato.usage)  
# zomato.purpose("zomato","food")   
# print(rapido.name)  
# print(rapido.color)
# print(rapido.usage)
# rapido.purpose("rapido","travelling") 

# class bankaccount:
#     def __init__(acnt,name,email,phno,balance):
#         acnt.name=name
#         acnt.email=email
#         acnt.phno=phno
#         acnt.balance=balance   
#     def deposit(acnt,d_amnt):
#         acnt.balance+=d_amnt  
#     def withdraw(acnt,w_amnt):
#         acnt.balance-=w_amnt 
#     def checkbalance(acnt):
#         print(acnt.balance)     
# chitti_acnt=bankaccount("chitti","chitti@gmail.com","6305078330","50000")
# chitti_acnt.checkbalance()
# print(chitti_acnt.name)  
# print(chitti_acnt.email)
# print(chitti_acnt.phno)
# print(chitti_acnt.balance)
# chitti_acnt.deposit(10000)
# chitti_acnt.checkbalance()
# chitti_acnt.withdraw(20000) 
# chitti_acnt.checkbalance()   



# import random 
# class BANK:
#     T_Holders=[]
#     def Create_New_Account(self):
#         H_Details={}
#         data=random.randint(100000000000,999999999999)
#         H_Details["H_name"]=input("Enter The Name:")
#         H_Details["Mobile No"]=input("Enter Mobile Number:")
#         H_Details["Aadhar No"]=input("Enter Aadhar Number:") 
#         H_Details["Account_Number"]=data
#         n1=input("Select Type of Account Saving/Zero.......")
#         while True:
#             if n1=="Saving":
#                 n2=int(input("Deposite 1000 rupees....."))
#                 if n2==1000:
#                     H_Details["Balance"]=n2
#                     break
#                 else:
#                     print("Deposite 1000 rupees....")
#             elif n1=="Zero":
#                 n3=int(input("Deposite 500 rupees..."))
#                 if n3==500:
#                     H_Details["Balance"]=n3
#                     break
#                 else:
#                     print("Deposite 500 rupees...")
#         BANK.T_Holders.append(H_Details)
#         print(BANK.T_Holders)  

# obj=BANK()
# obj.Create_New_Account()                     



# import random
# class bank:
#     t_holders=[]
#     def create_new_account(self):
#         h_details={}
#         data=random.randint(100000000000,999999999999)
#         h_details["h_name"]=input("enter the name:")
#         h_details["mobile no"]=input("enter mobile number:")
#         h_details["aadhar no"]=input("enter aadhar number:")
#         h_details["account_no"]=data
#         n1=input("select type of account saving/zero:")
#         while True:
#             if n1=="saving":
#                 n2=int("deposite 1000 rupees...")
#                 if n2==1000:
#                     h_details["balance"]=n2
#                     break
#                 else:
#                     print("deposite 1000 rupees:")
#             elif n1=="zero":
#                 n3=int("deposite 500 rupees:")
#                 if n3==500:
#                     h_details["balance"]=n3
#                     break
#                 else:
#                     print("deposite 500 rupees:")
#         bank.t_holders.append(h_details)
#         print(bank.t_holders)  
# obj=bank()
# obj.create_new_account() 
# 
# 

#OOPS
# class vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

#     def engineStart(self):
#         print(f"{self.model} of {self.brand} has started")
#     def engineStop(self):
#         print(f"{self.model} of {self.brand} has stopped")  

# car1=vehicle("BMW","classic 350")
# car1.engineStart()
# car1.engineStop()   

#Encapsulation:
#Wrapping up of data inside a class or method so that it cannot be accessed directly
#three types of access specifiers
#1.public:- it can be accessed directly
#2.protected:-



# class BankAccount:
#     def __init__(self,name,balance):
#         self._name=name
#         self._balance=balance
    
#     def getBalance(self):
#         print(f"Your current balance is : {self._balance}")

#     def deposit(self,amount):
#         if amount>0:
#             self._balance+=amount
#             print(f"{amount} has been credited to your account")
#             print(f"available balance is : {self._balance}")
#         else:
#             print("invalid amount")

#     def withdraw(self,amount):
#         if 0<amount<self._balance:
#             self._balance-=amount
#             print(f"{amount} has been debited from your account")
#             print(f"your current balance is : {self._balance}")
#         else:
#             print("Insufficient balance")    


# customer1=BankAccount("Chitti",50000)  
# customer1.getBalance()  
# customer1.deposit(25000)    
# customer1.withdraw(35000)


# #polymorphism
# #functions with same name performing differently based on classes and objects
# #1.Duck Typing :- if it walks like a duck and quacks like a duck then it is duck
# #if an object has certain features then it is considered as an object of certain category, irrespective of its real identity

# class dog:
#     def speak(dog):
#         print("dog speaks")
#     def walk(dog):
#         print("dog walks")

# class cat:
#     def speak(cat):
#         print("cat speaks")
#     def walk(cat):
#         print("cat walks")

# class Human:
#     def speak(Human):
#         print("Human speaks")
#     def walk(Human):
#         print("Human walks")

# def checking(obj):
#     obj.speak()
#     obj.walk()
#     print("then it is a man")
# dog1=dog()
# cat1=cat()
# human1=Human()
# checking(dog1)    
# checking(cat1)  
# checking(human1)  

# #2.Method Overriding without inheritance

# class father:
#     def work(self):
#         print("he does work to provide his family")
        
# class mother:
#     def work(self):
#         print("she takes care of family")

# father1=father()
# mother1=mother()
# father1.work()
# mother1.work()

#Method Overriding with inheritance

# class vehicle:
#     def start(self):
#         print("vehicle started")

# class car(vehicle):
#     def start(self):
#         print("car started") 

# car1=car()
# car1.start()        

#3. simulating Method Overloading using default arguments

# class math:
#     def add(self,a=0,b=0,c=0,d=0):
#         return a+b+c+d
    
# m1=math()
# print(m1.add(3))   
# print(m1.add(3,4))  
# print(m1.add(3,4,5,6))   


#4.Operator Overloading

# class book:
#     def __init__(self,pages):
#         self.pages=pages
       
#     def __add__(self,otherbook):
#         return self.pages+otherbook.pages   
# book1=book(250)
# book2=book(300)   
# print(book1+book2)   

#magic methods
#these are used to overload performance of symbols and some keywords. it is also called as dunder methods
#ex:- 
#__init__:- To initialize values to an object. it is automatically called when an object is created
#  __add__: to add two objects 
#  __sub__: to subtract 2 objects
# __call__:- it is used to make an object behave like a function
#__del__:- it is used to delete an object
#  __gt__:- 

#polymorphism
class class1:
    def __init__(self,name):
        self.name=name 

    def __call__(self):
        print(f"hello {self.name}, how are you?")  
    
    def __del__(self):
        print("this object is deleted")

        
man1=class1('chitti')
man1()     
del man1   

#inheritance
#def:-acquring data and methods from one class to another class
#types:
#single:- for parent class is inherited
class animal:
    def eat(self):
        print('this animal eats')
    
    
    
class dog(animal):
    def speak(self):
        print('this animal speak')

dog1=dog()
dog1.eat()
dog1.speak()

class father:
    def skills(self):
        print("reparing electrical devices, farming")

    class mother:

   