#inheritance
# single inheritance
class parent:
    def pmethod(self):
        print("method from parent")
class child:
    def cmethod(self):
        print("method from child")
obj1=parent()
obj1.pmethod()
obj2=child()
obj2.cmethod()  

class parent:
    def p1method(self):
        print("i am a method from parent")
    def p2method(self):
        print("i am a second method from parent")
class child:
    def cmethod(self):
        print("i am a method from child")
obj1=parent()
obj1.p1method()
obj1.p2method()
obj2=child()
obj2.cmethod()  

class parent:
    def p1method(self):
        print("i am a method from parent")
    def p2method(self):
        print("i am a second method from parent")
class child(parent):
    def cmethod(self):
        print("i am a method from child")
obj1=child()
obj1.p1method()
obj1.p2method()
obj1.cmethod() 

class parent:
    def p1method(self):
        print("method from parent")
    def p2method(self):
        print("second method from parent")
class child(parent):
    def cmethod(self):
        print("method from child")
        super().p2method() 
obj1=child()
obj1.cmethod()                   

#single inheritance
class user:
    def __init__(self,name,email):
        self.name=name
        self.email=email
class student(user):
    def __init__(self,name,email,enrolledcources):
        super().__init__(name,email)
        self.enrolledcources=enrolledcources
    def getcources(self):
        print(f"{self.name} is learning {self.enrolledcources}")    
class instructor(user):
    def __init__(self,name,email,cources_training):
        super().__init__(name,email)
        self.cources_training=cources_training
    def getcources(self):
        print(f"{self.name} is teaching {self.cources_training}")    
student_obj=student("divya","divya@gmail.com",["python","css","java"])
student_obj.getcources()
instructor_obj=instructor("chitti","chitti@gmail.com",["frontend","sql","js"]) 
instructor_obj.getcources()  
print(student_obj.name) 
print(student_obj.email)   
print(student_obj.enrolledcources)
print(instructor_obj.name)   
print(instructor_obj.email)
print(instructor_obj.cources_training)  

class user:
    def __init__(self,name,email):
        self.name=name
        self.email=email
class student(user):
    def __init__(self,name,email,enrolledcources):
        super().__init__(name,email)
        self.enrolledcources=enrolledcources
    def getcources(self):
        print(f"{self.name} is learning {self.enrolledcources}")
    def removecource(self,cource):
        self.enrolledcources.remove(cource)    
class instructor(user):
    def __init__(self,name,email,cources_training):
        super().__init__(name,email)
        self.cources_training=cources_training
    def getcources(self):
        print(f"{self.name} is teaching {self.cources_training}") 
    def removecource(self,cource):
        self.cources_training.remove(cource)     
student_obj=student("divya","divya@gmail.com",["python","css","java"])
student_obj.getcources()
student_obj.removecource("css")
student_obj.getcources()
instructor_obj=instructor("chitti","chitti@gmail.com",["frontend","sql","js"]) 
instructor_obj.getcources()  
instructor_obj.removecource("js")
instructor_obj.getcources() 

print(student_obj.name) 
print(student_obj.email)   
print(student_obj.enrolledcources)
print(instructor_obj.name)   
print(instructor_obj.email)
print(instructor_obj.cources_training)

#multiple inheritance
class parent1:
    def p1method(self):
        print("method from parent 1")
class parent2:
    def p2method(self):
        print("method from parent 2")  
class child(parent1,parent2):
    def cmethod(self):
        print("method from child")
obj1=child()
obj1.p1method()
obj1.p2method()
obj1.cmethod()

#multilevel inheritance
class parentactor:
    def __init__(self,pname,pworth):
        self.pname=pname
        self.pworth=pworth
        print(f"{self.pname} is a parent")
    def passets(self):
        print(f"{self.pname} assets are {self.pworth} cr") 
class childactor(parentactor):
    def __init__(self,pname,cname,pworth):
        super().__init__(pname,pworth) 
        self.cname=cname
        print(f"{self.cname} is came by the reference of {self.pname}")  
    def cassets(self,cworth):
        self.cworth=cworth
        print(f"{self.cname} is having worth of {self.cworth} cr")  
    def totalassets(self):
        print(f"total assets of {self.cname} is {self.pworth+self.cworth} cr")

ramcharan=childactor("chiranjeevi","ramcharan",100)
ramcharan.cassets(75)  
ramcharan.passets()
ramcharan.totalassets() 

class A:
    def __init__(self,val):
        self.val=val
    def show(self):
        print("A:", self.val)
class B(A):
    def show(self):
        print("B:", self.val)
class C(A):
    def show(self):
        print("C:", self.val)
class D(B,C):
    pass
d=D(50)
d.show() 
class A:
    def __init__(self,a):
        print("class A:", a)
class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        print("class B:", b)
class C(B):
    def __init__(self,b,a,c):
        super().__init__(a,b)
        print("class C:",c)
c=C(2,3,1)     


class person:
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,roll):
        super().__init__(name) 
        self.roll=roll
s=student("divya",101)
print(s.name)
print(s.roll)        


class Base:
    def __init__(self):
        self.value=10
class Derived(Base):
    def __init__(self):
        super().__init__()
        self.value=20
d=Derived()
print(d.value)    


class parent:
    name="parent"
class child(parent):
    name="child"
obj=child()
print(obj.name) 


class X:
    def __init__(self):
        print("Init of X")
class Y(X):
    def __init__(self):
        print("Init of Y")
        super().__init__()
class Z(Y):
    def __init__(self):
        print("Init of Z")
        super().__init__()
z=Z()    


class base:
    def __init__(self):
        self.base_val=100
class intermediate(base):
    def __init__(self):
        self.inter_val=200
class derived(intermediate):
    def __init__(self):
        self.derived_val=300
d=derived()
e=base()
print(e.base_val)   


class A:
    def display(self):
        print("class A")
class B(A):
    def display(self):
        super().display()
        print("class B")
class C(B):
    def display(self):
        super().display()
        print("class C")
obj=C()
obj.display()  


class A:
    def showA(self):
        print("A class")
class B(A):
    def show(self):
        print("B class")
obj=B()
obj.showA()       

class person:
    def __init__(self,name):
        self.name=name
p=person("divya")
print(p.name) 

