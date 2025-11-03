#encapsulation
#private
class sample:
    def __init__(self):
        self._name="chitti"
obj=sample()
print(obj._name)  

class parent:
    def __init__(self):
        self._user="divya"
class child(parent):
    def __init__(self):
        super().__init__()
        print(self._user)
obj1=child()
print(obj1._user)        

class sample:
    def __init__(self):
        self._name="chitti"
    def getdetails(self):
        print(self._name)
obj=sample()
print(obj.getdetails())        

class demo:
    def __init__(self):
        self.name="cryso"
obj=demo()
print(obj.__dict__)  
obj.name="chitti"
obj._name="divya"
obj.__name="cryso"
print(obj.__dict__)  

class demo:
    def __init__(self):
        self.__name="divya"
    def setdetails(self):
        self.__name="chitti"
obj=demo()
print(obj.__dict__)
obj.setdetails()
print(obj.__dict__)            