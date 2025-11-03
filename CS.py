num=12
if(num%2==0):
    print("even")
else:
    print("odd")  


num=15
if(num&5==0):
    print("even")
else:
    print("odd")


eamcetRank=45000
if(eamcetRank<25000):
    print("got seat in CMR") 
elif(eamcetRank<50000):
    print("got seat in kakateeya")
elif(eamcetRank<75000):
    print("got seat in mallareddy")
elif(eamcetRank<100000):
    print("got seat in scet") 
else:
    print("go and join in bcom/bsc")           
 
list1=["hello","welcome","something","hello","apple","apple"]
dict1={}
for x in list1:
    if(x in dict1):
        dict1[x]+=1
    else:
        dict1[x]=1    
print(dict1)

str1="banana"  #op={"b":1,"a":3,"n":2}
dict1={}
for x in str1:
    if(x in dict1):
        dict1[x]+=1
    else:
        dict1[x]=1
print(dict1)   

str1="chittikanapala"
dict1={}
for x in str1:
    if(x in dict1):
        dict1[x]+=1
    else:
        dict1[x]=1
print(dict1)        


#creating static objects
class person:
    name="chitti"
    age=25
    gender="male"
obj1=person()
obj2=person()
print(obj1)
print(obj2) 
print(obj1.name)  
print(obj2.name) 

obj1.name="divya"
print(obj1.name)
print(obj2.name)
print(person().name) 
#creating static objects
class person():
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
obj_chitti=("chitti","male","25")
obj_divya=("divya","female","21")
print(obj_chitti)
print(obj_divya)  
#print(obj_chitti.name)
#print(obj_divya.name)

# creating dynamic objects
class Application():
    def __init__(app,name,color,use):
        app.name=name
        app.color=color
        app.use=use
insta=Application("instagram","pink","socialmedia")
zomato=Application("zomato","red","food")
ola=Application("ola","black","travelling")
youtube=Application("youtube","red","entertainment")
print(insta.name,insta.color,insta.use)
print(zomato.name,zomato.color,zomato.use)
print(ola.name,ola.color,ola.use)
print(youtube.name,youtube.color,youtube.use)
#
class Application():
    def __init__(app,name,color,use):
        app.name=name
        app.color=color
        app.use=use
    def purpose(self):
        print("social media purpose")    
insta=Application("instagram","pink","socialmedia")
insta.purpose()
print(insta.name,insta.color,insta.use)
#
class Application():
    def __init__(app,name,color,use):
        app.name=name
        app.color=color
        app.use=use
    def purpose(self,app_name,purpose):
       print(f"{app_name} is used for {purpose}")    
insta=Application("instagram","pink","socialmedia")
zomato=Application("zomato","red","food")
ola=Application("ola","black","travelling")
youtube=Application("youtube","red","entertainment")

insta.purpose("instagram","socialmedia")
zomato.purpose("zomato","food")
ola.purpose("ola","travelling")
youtube.purpose("youtube","entertainment")  


class ParentActor:
    def __init__(self,name,worth):
        self.Pname=name
        self.Pworth=worth
        print(f"{self.Pname} is the parent")
    def Passets(self): 
        print(f"{self.Pname} assets are {self.Pworth}cr")    
class ChildActor(ParentActor):
    def __init__(self,Pname,Cname,Pworth):
        super().__init__(Pname,Pworth)
        self.Cname=Cname
        print(f"{self.Cname} is came by reference of {self.Pname}")
    def Cassets(self,worth):
        self.Cworth=worth
        print(f"{self.Cname} is having worth of {self.Cworth}cr")
    def Totalassets(self):
        print(f"total assets of {self.Cname} is {self.Pworth+self.Cworth}")
ramcharan=ChildActor("chiranjeevi","ramcharan",100)
ramcharan.Cassets(75)
ramcharan.Totalassets()
ramcharan.Passets()


class person:
    name="divya"
    age="21"
    gender="female" 
obj1=person() 
obj2=person()
print(obj1.name)
print(obj2.name)
print(obj1.age) 
print(obj1.gender)

obj1.name="chitti"
print(obj1.name)
obj1.age=25
print(obj1.age)
obj1.gender="male"
print(obj1.gender)

class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender    
obj_chitti=person("chitti",25,"male")
obj_divya=person("divya",21,"female")
print(obj_divya.name)       
print(obj_divya.age)   
print(obj_divya.gender)   
print(obj_chitti.name)   
print(obj_chitti.age)   
print(obj_chitti.gender)  

class application:
    def __init__(app,name,color,usage):
        app.name=name
        app.color=color
        app.usage=usage
    def purpose(self):
        print("social media purpose")    
instagram=application("instagram","pink","socialmedia")
zomato=application("zomato","red","food")
rapido=application("rapido","yellow","travelling")
print(instagram.name,instagram.color,instagram.usage)
instagram.purpose()
print(zomato.name,zomato.color,zomato.usage)
zomato.purpose()
print(rapido.name,rapido.color,rapido.usage)  
rapido.purpose()      

class parent:
    def pmethod(self):
        print("i am a method from parent")
    def cmethod(self):
        print("i am a second method from child") 
class child(parent):
    def cmethod(self):
        print("i am a method from child")
        super().pmethod()           
obj1=child()
obj1.cmethod()
obj1.pmethod()

class user:
    def __init__(self,name,email):
        self.name=name
        self.email=email
class student(user):
    def __init__(self,name,email,enrolledcource):
        super().__init__(name,email)
        self.enrolledcource=enrolledcource
    def getcource(self):
        print(f"{self.name} is learning {self.enrolledcource}")           
class instructor(user):
    def __init__(self,name,email,cource_training):
        super().__init__(name,email)
        self.cource_training=cource_training
    def getcource(self):
        print(f"{self.name} is teaching {self.cource_training}")  

student_obj=student("divya","divya@gmail.com","python full stack")
student_obj.getcource()
instructor_obj=instructor("chitti","chitti@gmail.com","python full stack")          
instructor_obj.getcource()

