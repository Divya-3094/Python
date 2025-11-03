sets={1,2,3,4,5}
print(type(sets))
print(sets)

sets.add("hi")
print(sets)

sets.remove(3)
print(sets)

set1=frozenset([1,3,5,7,8,8])
print(type(set1))
print(set1) 

print(type(3.14))
x=5+3*2
print(x)
x="python"
print(f"language:,{x}")

print(type(True))

x=5
y=2
print((x//y)+(x%y))

a=10
b=10.0
print(a==b)

x=153 21 79 232
y=sorted(str1)
print(x)

#abstraction
from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def travelvehicle(self):
        pass
class car(vehicle):
    def travelvehicle(self):
        print("travel by using car")
class bike(vehicle):
    def travelvehicle(self):
        print("travel by using bike")  
class train(vehicle):
    def travelvehicle(self):
        print("travel by using train") 
c=car()
b=bike()
t=train()
c.travelvehicle()
b.travelvehicle()
t.travelvehicle()

#problems on sets()
#Create a set with integers and print it.
set1={1,2,3,4,5,6,7,8,9,10}
print(set1)
#Add a single item to a set.
sets={1,2,3,4,5,6}
sets.add("hi")
print(sets)
#Add multiple items to a set using update().
sets={1,2,3,4,5}
sets.update([6,7,8,9])
print(sets)
#Remove an element using remove().
sets={1,2,3,4,5,6,7,8,9}
sets.remove(6)
print(sets)
#Remove an element using discard().
sets={1,2,3,4,5,6,7,8,9}
sets.discard(4)
print(sets)
#Pop an item from a set and display it.
sets={1,2,3,4,5,6,7,8,9}
print(sets)
x=sets.pop()
print(sets)
print(x)
#Clear a set completely.
sets={1,2,3,4,5,6,7}
sets.clear()
print(sets)
#Check membership of an element in a set.
sets={1,2,3,4,5,6,7}
if 3 in sets:
    print("3 is in set")
else:
    print("3 is not in set")    
#Create union of two sets.
set1={1,2,3,4,5}
set2={6,7,8,9,10}
x=set1.union(set2)
print(x)
#Find intersection of two sets.
set1={1,2,3,4,5}
set2={3,5,8,9,10}
x=set1.intersection(set2)
print(x)
#Find the difference between two sets.
set1={1,2,3,4,5}
set2={3,5,8,9,10}
x=set1.difference(set2)
print(x)
#Find symmetric difference between sets.
set1={1,2,3,4,5}
set2={3,5,8,9,10}
x=set1.symmetric_difference(set2)
print(x)
#Check if one set is subset of another.
set1={3,5}
set2={3,5,8,9,10}
if set1.issubset(set2):
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")    
#Check if one set is a superset of another.
set1={3,5}
set2={3,5,8,9,10}
if set2.issuperset(set1):
    print("set2 is superset of set1")
else:
    print("set2 is not a superset of set1")    
#Convert a list with duplicates into a set.
list1=[1,2,3,1,2,4,5,6,7]
set1=set(list1)
print(set1)
#Use set comprehension to create square numbers.
op={x**2 for x in range(1,10)}
print(op)
#Iterate over a set and print items.
set1={"divya","chitti","cryso","asha","sneha"}
for item in set1:
     print(item)
#Copy a set using copy().
set1={"divya","chitti","cryso"}
x=set1.copy()
print(x)
#Remove duplicates from a list using set().
list1=[1,2,3,1,2,4,5,6,7]
x=set(list1)
print(x)
#Use a set to store unique characters of a string.
str1="chitti"
x=set(str1)
print(x)
#Create an empty set and add elements one by one.
set1=set()
set1.add(10)
set1.add(20)
set1.add(30)
print(set1)
#Use a set in a loop to collect unique items.
x=[10,20,30,20,30,40,50]
y=set()
for num in x:
    y.add(num)
print(y)    
#Test if two sets are disjoint.
set1={1,2,3,4,5}
set2={6,7,8,9,10}
if set1.isdisjoint(set2):
    print("the sets are disjoint")
else:
    print("the sets are not disjoint")    
#Use frozenset and demonstrate immutability.
set1=frozenset([1,2,3,4,5,6,7,4,6])
print(set1)
#set1.remove(1)
#Convert tuple to set.
tuple1=("sun","mon","tue","wed")
set1=set(tuple1)
print(set1)
#Convert set to list.
set1={"divya","chitti","cryso"}
list1=list(set1)
print(list1)
#Merge multiple sets into one.
set1={10,20,30}
set2={40,50,60}
set3={70,80,90}
merged_set=set1.union(set2,set3)
print(merged_set)
#Filter a list using set membership.
list1=["apple","banana","mango","cherry"]
set1={"apple","cherry"}
x= [item for item in list1 if item in set1]
print(x)
#Find unique words in a sentence using set.
x="my name is divya!! i am from guntur.. my cource is python full stack"
words=x.split()
y=set(words)
print(y)
#Count unique vowels in a string.

#Get common elements from three sets.
set1={1,2,3,4,5}
set2={4,5,3,7,8}
set3={1,2,8,3,5}
x=set1.intersection(set2,set3)
print(x)
#Find non-overlapping items between two sets.
set1={1,2,3,4}
set2={3,4,5,6}
x=set1.symmetric_difference(set2)
print(x)
#Use set to find repeated items in a list.
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates
my_list = [1, 2, 3, 4, 2, 3, 5, 6, 1]
repeats = find_duplicates(my_list)
print("Repeated items:", repeats)
#Compare two sets and print differences.
set1={1,2,3,4,5}
set2={4,5,6,7}
diff1=set1-set2
print("items in set1 but not in set2:", diff1)
diff2=set2-set1
print("items in set2 but not in set1:", diff2)
difference=set1.symmetric_difference(set2)
print("items in either set but not both:", difference)
#Perform chained union of multiple sets.
set1={1,2,3}
set2={3,4,5}
set3={5,6,7}
result=set1.union(set2,set3)
print("chained union:",result)
#Check length of a set after each operation.
set1=set()
print("initial length:", len(set1))
set1.add(10)
print("length after adding 1st element:",len(set1))
set1.add(20)
print("length after adding 2nd element:",len(set1))
set1.add(30)
print("length after adding 3rd element:",len(set1))
#Use set to filter out special characters from a string.
str1="hello@# world!! welcome$%&*"
allowed_chars=set("abcdefghijklmnopqrstuvwxyz")
filtered_str="".join(ch for ch in str1 if ch in allowed_chars)
print("original:",str1)
print("filtered:",filtered_str)
#Use set to group users by unique roles.
users=[ 
    {"name":"divya","role":"admin"},
    {"name":"chitti","role":"editor"},   
    {"name":"cryso","role":"viewer"},
    {"name":"ashaa","role":"trainer"},
    {"name":"sneha","role":"trainee"}
]
x={user["role"] for user in users}
print("unique roles:",x)
#Find all even numbers from 1 to 50 using set.
even_numbers={num for num in range(1,51) if num%2==0}
print("even numbers from 1 to 50:",even_numbers)
#Combine numbers and letters into a single set.
letters=set("divyachitti")
numbers=set([1,2,3,4,5])
x=letters|numbers
print("combined set:",x)
#Find missing elements from a full range set.
list1={1,2,4,6,7}
full_range_set=set(range(min(list1),max(list1)+1))
set1=set(list1)
missing_elements=full_range_set-set1
print("missing_elements:",sorted(missing_elements))
#Compare performance of set vs list in membership tests. 

#Use set to validate inputs in a quiz app.
valid_choices={"A","B","C","D"}
print("Questions: What is the capital of France?")
print("A. Berlin")
print("B. Madrid")
print("C. Paris")
print("D. Rome")
user_answer=input("enter your answer (A/B/C/D):").strip().upper()
if user_answer in valid_choices:
    if user_answer == "C":
        print("Correct")
    else:
        print("Incorrect. The correct answer is C.")
else:
    print("Invalid input. please enter one of A,B,C or D.")            
#Compare two dictionaries by converting their keys to sets.
dict1={"a":1,"b":2,"c":3}
dict2={"b":4,"c":3,"d":5}
keys1=set(dict1.keys())
keys2=set(dict2.keys())
common_keys=keys1&keys2
unique_to_dict1=keys1-keys2
unique_to_dict2=keys2-keys1
all_keys=keys1|keys2
print("common keys:",common_keys)
print("unique to dict1:",unique_to_dict1)
print("unique to dict2:",unique_to_dict2)
print("All keys:",all_keys)
#Analyze word frequency using set and dict together.
text="apple orange banana apple mango banana apple"
words=text.split()
unique_words=set(words)
word_freq={}
for word in words:
    word_freq[word]=word_freq.get(word,0)+1
print("unique words:",unique_words)
print("word frequencies:")
if word in unique_words:
    print(f"{word}:{word_freq[word]}")    
#Identify duplicate words from a paragraph using set.
paragraph = "Python is easy to learn. Python is powerful and easy to use."
words = paragraph.lower().replace('.', '').split()
seen = set()
duplicates = set()
for word in words:
    if word in seen:
        duplicates.add(word)
    else:
        seen.add(word)
print("Duplicate words:", duplicates)
#Find if any letter is repeated in a string using set.
def has_repeated_letters(s):
    seen=set()
    for char in s:
        if char in seen:
           return True
        seen.add(char)
    return False
string="hello"
if has_repeated_letters(string):
    print("repeated letter found.")
else:
    print("all letters are unique")            
#Print ASCII codes of unique characters in a string.
text="hello world"
unique_chars=set(text)
for char in unique_chars:
    print(f"'{char}':{ord(char)}")
#Demonstrate set behavior with mutable and immutable elements.
valid_set={1,"apple",(2,3)}
print("valid set:",valid_set)
#Build a set from user input until 'stop' is entered.
user_inputs=set()
print("enter values (type 'stop' to finish):")
while True:
    value=input(">>").strip()
    if value.lower()=='stop':
        break 
    user_inputs.add(value)
print("\nunique inputs entered:")
print(user_inputs)    