#patterns
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

# for x in range(1,6):
#     for y in range(97,97+x):        # 97 is ASCII value of 'A'
#         print(chr(y), end=" ")      # Convert ASCII to character
#     print() 

# # Outer loop for each row
# for x in range(1,6):
# # Inner loop to print letters from 'A' to the ith letter
#     for y in range(65,65+x):      # 65 is ASCII value of 'A'
#       print(chr(y), end=" ")       # Convert ASCII to character
# # Move to next line      
#     print()        


# for i in range(1,6):
#     for j in range(6-i):
#         print(" ", end=" ")
#     for k in range(i):
#         print("$", end=" ")
#     print()        
         
# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()              
#input name="divya"  in the o/p  vowels should be replace with next alphabet
# name = "divya"
# output=" "
# for i in name:
#     if i in ("a","e","i","o","u"):

#input should be string and output should be the next 3rd letter of every character in that string
# name="Zebra"
# op=""
# add=2
# for i in name:
#     if ord(i)+add>122:
#         next_char=chr(96+add)
#         op+=next_char
#     else:
#         next_char=chr(ord(i)+2)
#         op+=next_char
# print(op)            

#input="aaabbcab"  o/p-> a3b2c1a1b1
# input="aaabbcab"

#input=["flower","floor","flood","flow"]      longest prefix=flo
# input=["flower","floor","flood","flow"]
# min=0
# smallest=""
# prefix=""
# for i in list:
#     if len(i)<min:
#         smallest=i
#         min=len(i) 

#palindrome "malayalam"
# word="malayalam"
# pal_count=0
# for i in range(len(word)):
#     temp=""
# for j in range(1,len(word)):
#     temp=word[j]
#     if len(temp)>j:
#         rev=temp[::-1]
#         if rev==temp:
#            pal_count+=1
# print(pal_count)  
#           
#sqare
# n=int(input("enter the size of the sqare: "))
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()
# #number right angle triangle
# n=int(input("enter number of rows: "))
# num=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()                         
# #rectangle
# m=int(input("Enter number of rows (m): "))
# n=int(input("enter number of columns (n): "))
# for i in range(m):
#     for j in range(n):
#         print("*",end=" ")
#     print()    
# #star right angle triangle
# n=int(input("enter the number: "))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()  
# #reverse right angle triangle
# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print() 

n=int(input("enter the number: "))
for i in range(1,n):
    for j in range(1,n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()        
#Inverted left_aligned triangle pattern 
n=int(input("Enter no of rows: "))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()  
#Inverted right_aligned triangle pattern
n=int(input("enter no of rows: "))
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(n-i):
        print("*",end=" ")
    print()           
# Centered Pyramid Pattern
n=int(input("enter no of rows: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()
# Diamond Pattern
n=int(input("enter no of rows: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()    
for i in range(n-2,-1,-1):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()
#Butterfly Pattern
n=int(input("enter no of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    for j in range(2*(n-i)):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()  
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    for j in range(2*(n-i)):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()    
# Left-Aligned Half Diamond Pattern
n = 4  # number of rows for the upper half

# Upper half of diamond
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Lower half of diamond
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
# Right-Aligned Half Diamond Pattern
n = 4  # number of rows for the upper half

# Upper half
for i in range(1, n + 1):
    # print spaces
    for j in range(n - i):
        print(" ", end=" ")
    # print stars
    for k in range(i):
        print("*", end=" ")
    print()

# Lower half
for i in range(n - 1, 0, -1):
    # print spaces
    for j in range(n - i):
        print(" ", end=" ")
    # print stars
    for k in range(i):
        print("*", end=" ")
    print()
# Sandglass Star Pattern
n = 4  # number of rows

# Upper inverted triangle
for i in range(n, 0, -1):
    # print spaces
    for j in range(n - i):
        print(" ", end=" ")
    # print stars
    for k in range(i):
        print("*", end=" ")
    print()

# Lower triangle
for i in range(2, n + 1):
    # print spaces
    for j in range(n - i):
        print(" ", end=" ")
    # print stars
    for k in range(i):
        print("*", end=" ")
    print()
# Increasing Width Triangle Pattern
n = 5  # number of rows

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()  # move to next line
# Decreasing Width Triangle Pattern
n = 5  # number of rows

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()  # move to the next line
# Right-Aligned Hill Pattern
n = 4  # number of rows

for i in range(1, n + 1):
    # print spaces
    for j in range(n - i):
        print(" ", end=" ")
    # print stars
    for k in range(i):
        print("*", end=" ")
    print()  # move to next line
# Hollow Square Pattern
n = 4  # size of the square

for i in range(n):
    for j in range(n):
        # Print stars on the border
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # move to next line
# Hollow Rectangle Pattern
m = 4  # number of rows
n = 5  # number of columns

for i in range(m):
    for j in range(n):
        # print stars on border positions
        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # move to next line
# Hollow Right-Angled Triangle (Left-Aligned)
n = 5  # number of rows

for i in range(1, n + 1):
    for j in range(1, i + 1):
        # print star for first or last column of each row, or the last row
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # move to the next line
# Hollow Right-Angled Triangle (Right-Aligned)
n = 5  # number of rows

for i in range(1, n + 1):
    # print leading spaces
    for j in range(n - i):
        print(" ", end=" ")
    # print stars and inner spaces
    for k in range(1, i + 1):
        if k == 1 or k == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # move to next line
# Hollow Inverted Triangle (Left-Aligned)
n = 5  # number of rows

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        # print star for borders or first/last row
        if i == n or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # move to next line
# Hollow Inverted Triangle (Right-Aligned)
n = 5  # number of rows

for i in range(n, 0, -1):
    # print leading spaces
    for j in range(n - i):
        print(" ", end=" ")
    # print stars and hollow spaces
    for k in range(1, i + 1):
        if i == n or k == 1 or k == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # move to next line
# Hollow Pyramid Pattern
n = 4  # number of rows

for i in range(1, n + 1):
    # print leading spaces
    for j in range(n - i):
        print(" ", end=" ")
    # print stars and inner spaces
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # move to the next line
# Hollow Diamond Pattern
n = 3  # number of rows for the upper half

# Upper half of diamond
for i in range(1, n + 1):
    # print leading spaces
    for j in range(n - i):
        print(" ", end=" ")
    # print stars and hollow spaces
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Lower half of diamond
for i in range(n - 1, 0, -1):
    # print leading spaces
    for j in range(n - i):
        print(" ", end=" ")
    # print stars and hollow spaces
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Hollow Butterfly Pattern
n = 4  # number of rows for each half

# Upper half
for i in range(1, n + 1):
    # Left wing
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    # Spaces between wings
    for j in range(2 * (n - i)):
        print(" ", end=" ")
    # Right wing
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Lower half
for i in range(n, 0, -1):
    # Left wing
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    # Spaces between wings
    for j in range(2 * (n - i)):
        print(" ", end=" ")
    # Right wing
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Hollow Hourglass (Sandglass) Pattern
n = 5  # number of rows

# Upper inverted hollow pyramid
for i in range(n, 0, -1):
    # print leading spaces
    for j in range(n - i):
        print(" ", end=" ")
    # print stars and hollow spaces
    for k in range(1, 2 * i):
        if i == n or k == 1 or k == 2 * i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#Lower hollow pyramid
for i in range(2, n + 1):
    # print leading spaces
    for j in range(n - i):
        print(" ", end=" ")
    # print stars and hollow spaces
    for k in range(1, 2 * i):
        if i == n or k == 1 or k == 2 * i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()




      


  


