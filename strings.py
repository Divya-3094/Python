#Create a string with your name and print it.
str1="divya"
print(str1)
#Get the first character from the string.
print(str1[0])
#Get the last character from the string.
print(str1[4])
#Concatenate two strings.
str1="divya"
str2="chitti"
result=str1+str2
print(result)
#Repeat a string 3 times.
str1="chitti"
print(str1*3)
#Slice the first 5 characters.
str1="chittikanapala"
print(str1[:5])
#Reverse a string using slicing.
str1="chittikanapala"
print(str1[::-1])
#Check if a substring exists in a string.
str1="python programming language"
substring="language"
if substring in str1:
    print("substring found!!")
else:
    print("substring not found!!!")    
#Find the length of a string.
str1="chittikanapala"
print(len(str1))
#Convert string to uppercase.
str1="chittikanapala"
print(str1.upper())
#Convert string to lowercase.
str1="chittikanapala"
print(str1.lower())
#Capitalize the first letter.
str1="chittikanapala"
print(str1.capitalize())
#Convert a string to title case.
str1="chittikanapala"
print(str1.title())
#Remove leading spaces using lstrip().
str1="****chitti kanapala****"
print(str1.lstrip("*"))
#Remove trailing spaces using rstrip().
str1="****chitti kanapala****"
print(str1.rstrip("*"))
#Remove both ends' spaces using strip().
str1="****chitti kanapala****"
print(str1.strip("*"))
#Replace all spaces with underscores.
str1="    chitti kanapala    "
print(str1.replace(" ","_"))
#Count how many times a character appears.
str1="chitti kanapala"
z="a"
print(str1.count(z))
#Find index of a character using find().
str1="chitti kanapala"
char="k"
index=str1.find(char)
print(index)
#Use rfind() to find last occurrence.
str1="chitti kanapala"
z=str1.rfind("kanapala")
print(z)
#Use index() to find substring position.
str1="python programming language"
substring=str1.index("language")
print(substring)
#Split a string by spaces.
str1="python programming language"
x=str1.split(" ")
print(x)
#Join a list of words into a string.
list1=["python","programming","language"]
str1=" ".join(list1)
print(str1)
#Check if string starts with "Hello".
str1="hello, how are you?"
print(str1.startswith("hello"))
#Check if string ends with "world".
str1="hello world"
print(str1.endswith("world"))
#Check if a string is digit.
str1="2004"
print(str1.isdigit())
#Check if a string is alphabet.
str1="chitti"
print(str1.isalpha())
#Check if a string is alphanumeric.
str1="divya2004"
print(str1.isalnum())
#Get ASCII value of a character.
str1="c"
ascii_value=ord(str1)
print(ascii_value)                                                     
#Convert ASCII to character.
ascii_value=65
print(chr(ascii_value))
#Remove punctuation from string.
import string
text="hello, world! how's it going?"
text2=text.translate(str.maketrans('', '', string.punctuation))
print(text2)
#Swap case of all characters.
text="Hello World! Python"
print(text.swapcase())
#Count total words in a string.
str1="divya chitti kanapala"
x=str1.split()
count=len(x)
print(count)
#Count total sentences in a string.
text="hello world! Welcome to python programming. How are you doing? I hope you're learning python. Let's code more."

#Convert string to list of characters.
str1="chitti"
x=list(str1)
print(x)
#Convert list of characters to string.
list1=["c","h","i","t","t","i"]
str1=str(list1)
print(str1)
#Pad string to the left with * to length 10.
data="chitti"
x=data.rjust(10,"*")
print(x)
#Center align string using center().
text="chitti"
x=text.center(10,"*")
print(x)
#Format string with variables using f-string.
a="chitti"
b=25
print(f"my name is {a} and i am {b} years old")
#Use % operator to format a string.
a="divya"
b=21
print("my name is %s and i am %d years old." %(a,b))