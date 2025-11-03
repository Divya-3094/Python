#arthimatic operators
a=5
b=6
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a|b)
print(a**b)

#comparision operators
a=5
b=5
print(a==b)

input_Password="strongpassword"
db_stored_password="strongpassword"
print('input_password'=='db_stored_password')
print('input_password'!='db_stord_password')

a=10
b=5
print(a>b)

quantity_in_store=25
client_require=35
print(quantity_in_store>client_require)
print(quantity_in_store<client_require)

print(10>=10)
print(10<=8)

str1="welcome"
str2="something"
print(len(str1)==len(str2))
print(len(str1)<len(str2))
print(len(str1)>len(str2))


list1=[1,2,3,4,5]
list2=[10,11,12,4,6]
print(len(list1)!=len(list2))
print(list1[2]>list2[3])

#logical operators
a=5
b=3
print(True and True)
print(a<10 and b<5)
print(False and False)
print(a>10 and b>5)
print(True and False)
print(a<10 and b>5)
print(False and True)
print(a>10 and b>10)
print(True or True)
print(a>2 or b>2)
print(False or True)
print(a<3 or b<3)
print(True or False)
print(a>4 or b>2)
print(False or False)
print(a<1 or b<1)
print(True)
print(not True)
print(False)
print(not False)

#assignment operators
a=5
print(a)
a+=5
print(a)
a-=5
print(a)
a*=5
print(a)
a/=5
print(a)
a%=5
print(a)
a//=5
print(a)
a**=5
print(a)

#membership operators
str="hello world"
print("w" in str)
print("m" in str)

list1=[4,5,8,9,12,13]
print("10" in list1)
print("12" in list1)
op=12 in list1
print(op)

tuple=(3,8,9,13,33,45)
op=13 in tuple
print(op)
ip=30 in tuple
print(ip)

set1={"apple","banana","mango","grape"}
x="mango" in set1
print(x)
y="orange" in set1
print(y)

students=["chitti","divya","cryso","sneha","ashaa"]
stu="CHITTI"  in students
print(stu)

#identity operators
a=240
b=240
print(a is not b)
print(a is b)
print(id(a))
print(id(b))

#bitwise operators
3&3
print(3&3)
3&5
print(3&5)
3|5
print(3|5)
5^7
print(5^7)
3^6
print(3^6)
print(~5)
print(5>>4)
print(10>>2)
print(5<<2)

