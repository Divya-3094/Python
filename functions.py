#Function Exercises (1–50)
#Write a function to add two numbers.
def add(a,b):
    add=a+b
    return add
print(add(2,5))

def add(a,b):
    print(a+b)
add(3,6)    
#Write a function to return the square of a number.
def sqare(a,b):
    sqare=a**b
    return sqare
print(sqare(5,2))

def sqare(a,b):
    print(a**b)
print(sqare(5,2))    

def sqare(num):
    return num*num
print(sqare(7))
#Write a function to find the factorial of a number.
def factorial(x):
    result=1
    for i in range(1,x+1):
        result*=i
    return result
print(factorial(5))     
#Write a function to find the greatest of two numbers.
def greaternum(a,b):
    if a>b:
        return a
    else:
        return b
print(greaternum(76,98))       
#Write a function that returns whether a number is even or odd.
def function(x):
   if x%2==0:
       return "even"
   else:
       return "odd"
print(function(35))   
#Write a function to check if a number is prime.
def is_prime(x):
    if x<=1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
print(is_prime(7))    
#Write a function to return the sum of first n natural numbers.    
def natural_numbers(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
print(natural_numbers(5))
#Write a function to return maximum of three numbers.
def max_of_three_numbers(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
print(max_of_three_numbers(10,20,30))    
#Write a function to reverse a number.
def reversed_number(num):
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    return rev
print(reversed_number(2345))    
#Write a function to count digits in a number.
def count_digits(num):
    count=0
    while num>0:
        num=num//10
        count+=1
    return count
print(count_digits(453687))    
#Write a function to convert Celsius to Fahrenheit.
def celcious_to_fahrenheit(celcius):
    return (celcius*9/5)+32
print(celcious_to_fahrenheit(35))
#Write a function to find power of a number (base, exponent).
def power(base,exponent):
    return base**exponent
print(power(2,3))
#Write a function to check if a year is a leap year.
def is_leap_year(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False
print(is_leap_year(2020))    
#Write a function to check whether a number is palindrome.
def is_palindrome(num):
    original=num
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    return original==rev        
print(is_palindrome(12321))   
#Write a function to calculate simple interest.
def simple_intrest(principle,rate,time):
    return (principle*rate*time)/100
print(simple_intrest(1000,5,2))
#Write a function that accepts a number and returns its absolute value.
def absolute_value(num):
    if num<0:
        return -num
    else:
        return num
print(absolute_value(-20))    
#Write a function to return the area of a circle.
import math
def area_of_a_circle(radius):
    return math.pi*radius*radius
print(area_of_a_circle(5))
#Write a function to convert minutes to hours and minutes.
def convert_minutes(total_minutes):
    hours=total_minutes//60
    minutes=total_minutes%60
    return hours,minutes
h,m=convert_minutes(163)
print(f"{h} hours and {m} minutes")
#Write a function to calculate compound interest.
def compound_intrest(principle,rate,time):
    amount=principle*(1+rate/100)**time
    ci=amount-principle
    return ci
print(compound_intrest(1000,5,2))
#Write a function to return all factors of a number.
#Write a function to print multiplication table of a number.
#Write a function to calculate average of numbers in a list.
#Write a function that takes name and age and prints a message.
#Write a function to calculate BMI and return category.
#Write a function to convert decimal to binary.
#Write a function to find greatest common divisor (GCD).
#Write a function to calculate LCM of two numbers.
#Write a function to return the nth Fibonacci number.
#Write a function that returns whether a number is Armstrong or not.
#Write a function that prints all prime numbers up to n.
#Write a function to find sum of digits of a number.
#Write a function to calculate perimeter of rectangle.
#Write a function to return second largest of three numbers.
#Write a function to swap two numbers.
#Write a function to return product of digits of a number.
#Write a function to calculate total bill with tax and tip.
#Write a function to validate if age is eligible for driving.
#Write a function that counts number of even numbers in a list.
#Write a function that returns True if a number is perfect.
#Write a function to convert days into weeks and days.
#Write a function to check triangle validity from 3 sides.
#Write a function to return max digit in a number.
#Write a function to reverse digits of a number.
#Write a function to generate first n odd numbers.
#Write a function to find minimum value from a list.
#Write a function to return the square root of a number.
#Write a function to check if a number is divisible by both 3 and 5.
#Write a function to simulate a basic calculator (add, sub, mul, div).
#Write a function to return number of digits in an integer.
#Write a function that finds sum of all even digits in a number.
