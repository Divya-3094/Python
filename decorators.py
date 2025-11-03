#decorators

#enhance---> Adding Additional Features without 
# changing the original functionality

#Decorator:- It's a Function that enhances other function
#@decorator_name

def sum(a,b):
    if type(a)!="int" or type(b)!="int":
       print("not possible")
    print(a+b)   
sum(5,3)
# sum("hello",5)    

#function is a reusable block of code 
#decorators are also higher-order function
#defining a decorator
def check_msg(func):     #this is the decorator name  main function
    def wrapper():       #for adding additional functionalities for the original function
        print("before original function")
        func()
        print("after the original function")
    return wrapper    
@check_msg     # using a decorator on a function
def say_hello():
    print("hello world")
say_hello()  
@check_msg
def greet():
    print("good evening")
greet()    


def check_int(fun):
    def wrapper(a,b):
        if not isinstance(a,int) or not isinstance(b,int):
            return "invalid inputs"
        res=fun(a,b)   #only when there is a return statement in the original function
        return res
    return wrapper    
@check_int
def sum(a,b):
    return a+b
print(sum("2",3))
@check_int
def add_num(m,n):
    return m+n
print(add_num(10,20))

# print(isinstance("1",str))
def check_str(func):
    def wrapper(n):
        if not isinstance(n,str):
            return "not a name"
        res=func(n)
        return res
    return wrapper

@check_str
def wish(name):
    return "hello "+name
print(wish(123))

#using *args **kwargs

def has_zero(org):
    def wrapper(*args):
        if 0 in args:
           res=org("divya")
           return res
        else:
           res=org(*args)   
           return res
    return wrapper
@has_zero
def params(*args):
    return args
print(params(1,2,3,4,5,6,7,8,9,10))

# @api_view
# @csrf_exempt

# def decorator_name(original func as a parameter):
#     def wrapper(to access parameters of original function):
#         res=original(parameter)
#         return res
#     return wrapper
# @decorator_name

def minus(n):
    return n-1
print(minus(10))