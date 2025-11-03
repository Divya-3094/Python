#Loops Questions:
#1.Print all numbers from 1 to 100 using a for loop.
for i in range(1,101):
    print(i)
#Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)
n=int(input("Enter A positive number: "))
sum=n*(n+1)//2
print(f"The sum of the first {n} natural numbers: {sum}")

num=int(input("Enter a positive number: "))
sum=0
for i in range(1,num+1):
    sum+=i
print(f"the sum of forst {num} natural numbers is: {sum}")     
#Print all even numbers between 1 and 50 using a while loop. 
n=2
while n<=50:
    print(n)
    n+=2

for i in range(1,51):
    if i%2==0:
      print(i)
#Write a program to display the multiplication table of a given number. First 20
num=int(input("Enter the number: "))
for i in range(1,21):
    print(f"{num} x {i} = {num*i}")    
#Reverse a number using a while loop. Also can we get the sum of all the digits.
num=int(input("Enter a number: "))
original_num=num
reversed=0
sum=0
while num>0:
    digit = num%10             #to get the last digit
    reversed=reversed*10+digit   #for reversed number
    sum+=digit                 #add digit to sum
    num=num//10                #Remove the last digit
print(f"Original number: {original_num}")
print(f"Reversed number: {reversed}")
print(f"Sum of digits: {sum}")


   



