#tuple
days=("sun","mon",["tue,fri"],"True",(1,2,3))
print(type(days))
print(len(days))
print(days[0][0])
print(days[2][0])
print(days[2][0][1])
print(f"{len(days[4])}")
print(f"size of the tuple is {len(days[4])}")
print(days)


#problems on tuple
#Create a tuple with 5 elements and print it.
days=("sun","mon","tue","wed","thurs","fri","sat")
print(days)
#Access the third element of a tuple.
days=("sun","mon","tue","wed","thurs","fri","sat")
print(days[2])
#Slice a tuple to get the first 3 elements.
days=("sun","mon","tue","wed","thurs","fri","sat")
print(days[:3])
#Check if an item exists in a tuple.
days=("sun","mon","tue","wed","thurs","fri","sat")
item="wed"
if item in days:
    print(f"{item} exists in tuple") 
else:
    print(f"{item} dosnt exists in tuple")    
#Concatenate two tuples.
x=("sun","mon","tue","wed")
y=("thurs","fri","sat")
z=x+y
print(z)
#Repeat a tuple three times.
days=("sun","mon","tue","wed","thurs","fri","sat")
z=days*3
print(z)
#Find the length of a tuple.
days=("sun","mon","tue","wed","thurs","fri","sat")
print(len(days))
#Convert a list into a tuple.
days=["sun","mon","tue","wed","thurs","fri","sat"]
convert=tuple(days)
print(convert)
#Convert a tuple into a list.
days=("sun","mon","tue","wed","thurs","fri","sat")
convert=list(days)
print(convert)
#Find the index of an element in a tuple.
days=("sun","mon","tue","wed","thurs","fri","sat")
print(days.index("wed"))
#Count occurrences of an element in a tuple.
days=("sun","fri","tue","sun","tue","fri","sun")
print(days.count("fri"))
#Create a nested tuple and access inner elements.
days=(1,2,3,(3,4,6,),9,(9,8,7),10)
print(days[5])
print(days[3][1])
#Check if all elements in a tuple are integers.
x=(1,2,3,4,5,6,7,8,9,10)
print(all(isinstance(item,int) for item in x))
#Unpack a tuple into variables.
data=(10,20,30,40)
a,b,c,d=data
print(a)
print(b)
print(c)
print(d)
#Swap values of two variables using a tuple.
a="divya"
b="chitti"
a,b=b,a 
print(a,b)
#Iterate through a tuple using a loop.
data=("divya","chitti","kanapala","vallabhapuram")
for item in data:
    print(item)
#Find the max and min values in a numeric tuple.
data=(10,20,30,40,50,60,70,80,90)
print(min(data))
print(max(data))
#Sort elements of a tuple (convert and sort).
data=(50,30,80,10,40)
print(sorted(data))
convert=sorted(data)
print(convert)
#Merge tuples of equal length into pairs.
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
merged=tuple(zip(tuple1,tuple2))
print(merged)
#Create a tuple of even numbers using range().
even_numbers=tuple(range(0,20,2))
print(even_numbers) 