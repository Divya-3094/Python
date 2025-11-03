#Method Overriding
class vehicle:
    def speed(self):
        print("vehicle speed is normal")
class car(vehicle):
    def speed(self):
        print("car speed is 120kmph")
class cycle(vehicle):
    def speed(self):
        print("cycle speed is 20kmph")  
car=car()
cycle=cycle()
car.speed()
cycle.speed()              


class order:
    def __init__(self,customer,order_id):
        self.customer=customer
        self.order_id=order_id
    def deliver(self):
        print(f"{self.customer} will get this order number {self.order_id} with standerd delivery") 
class expressorder(order):
    def __init__(self,customer,order_id):
        super().__init__(customer,order_id)
    def deliver(self):
        print(f"{self.customer} will get this order number {self.order_id} with express delivery")
obj1=order("chitti","chitti234")
obj1.deliver()
obj2=order("divya","divya654")
obj2.deliver()
obj3=expressorder("cryso","cryso876")
obj3.deliver()
print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)
print(expressorder.__mro__)

