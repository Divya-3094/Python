#Python Programming Questions
#If Else Questions:
#1)a or b which is bigger
a=10
b=30
if a>b:
    print("Bigger number is a: ",a)
else:
    print("Bigger number is b: ",b)    
#2) a or b or c which is bigger.
a=50
b=30
c=70
if (a>=b and a>=c):
    print("Bigger number is a: ",a)
elif (b>=a and b>=c):
    print("Bigger number is b: ",b)
else:
    print("Bigger number is c: ",c) 
#4)Wap to find a number is even or odd
number =int(input("enter the number: "))
if number%2==0:
    print("Number is Even")
else:
    print("Number is Odd") 
#3)Wap to find Leap Year
year=int(input("Enter a Year: "))
if(year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")    
#4) Write a program to check if a given number is positive, negative, or zero.
number=int(input("Enter the Number: "))
if number>0:
    print(f"{number} is positive number")
elif number<0:
    print(f"{number} is negative number")
else:
    print(f"{number} is a zero")  
#5) Check if a person is eligible to vote (age >= 18).
age=int(input("Enter the Age: "))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")   
#6) Print "Pass" if a student scores more than 40 marks; otherwise, print "Fail." 
marks=int(input("Enter Marks: "))
if marks>40:
    print("pass")
else:
    print("fail")    
#7) Write a program to display the day of the week based on a number input (1 for Monday, 2 for Tuesday, etc.). 
day_number=int(input("Enter a Number (1-7): "))
days={
    1:"Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Thursday",
    5:"Friday",
    6:"Saturday",
    7:"Sunday",
}   
if 1 <= day_number <= 7:
    print(f"The day is {days[day_number]}")
else:
    print("Invalid Input! Please enter a number between 1 and 7.")    
#8) Implement a simple calculator to perform addition, subtraction, multiplication, and division.
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

print("select operation")
print("1. Addition (+)")
print("2.Substraction (-)")
print("3. Multiplication (*)")
print("4. Dvision (/)")

choice= input("Enter Choice (1/2/3/4): ")

if choice == '1':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif choice == '3':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error! Division by Zero is not allowed.")
else:
    print("Invalid input! please choose 1, 2, 3, or 4.")            
#9) Write a program to classify a character entered by the user as a vowel, consonant, or neither.
char=input("Enter a single character: ")
if len(char) == 1 and char.isalpha():
    vowels = "aeiouAEIOU"
    if char in vowels:
        print(f"{char} is a vowel")
    else:
        print(f"{char} is a consonant")
else:
    print(f"{char} is neither a vowel nor a consonant")            
#10) Calculate the grade of a student based on the marks they score: 1. 90-100: Grade A 2. 80-89: Grade B 3. 70-79: Grade C 4. <70: Fail. 
marks=int(input("Enter the marks: "))
if 90 <= marks <= 100:
    print("Grade: A")
elif 80 <= marks <= 89:
    print("Grade:B")
elif 70 <= marks <= 79: 
    print("Grade: C")
elif 0 <= marks < 70:
    print("Fail")
else:
   print("Invalid marks! please enter marks between 0 to 100")    
#11) Write a program to check if three sides length form a valid triangle
a=int(input("enter the length of side 1: "))
b=int(input("enter the length of side 2: "))
c=int(input("enter the length of side 3: "))

if (a+b>c) and (a+c>b) and (b+c>a):
    print("The sides form a valid triangle")
else:
    print("The sides donot form a valid triangle")    


