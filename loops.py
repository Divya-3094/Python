#print 1 to 20 numbers divisible by 2 &3 and both 
for x in range(1,21):
    if(x%2==0 and x%3==0):
        print(f"{x}-fizzbuzz")
    elif(x%3==0):
        print(f"{x}-buzz") 
    elif(x%2==0):
        print(f"{x}-fizz")

#sum of first 10 numbers
sum=0
for x in range(1,11):
    sum+=x
    print(sum)

num=123890546
cnvrt=str(num)
for x in cnvrt:
    print(x)
for x in range(len(cnvrt)-1,-1,-1):
    print(cnvrt[x])

num=123890546
print(num%10)
print(num//10)

num=123890546
cnvrt=str(num)
while(num>10):
   print()
num//10    

num=125
sum=0
while(num>0):
    ld=num%10
    sum+=ld
    num=num//10
    print(sum)
    
num=125
sum=0
while(num>0):
    ld=num%10
    sum+=ld**2
    num=num//10
    print(sum)

num=12504
count=0
while num>0:
   ld=num%10
   count+=1
   num=num//10
   print(count)

