for x in range(1,5):
    line=""
for y in range(1,x):
    line+=str(y)
    print(line)

for x in range(97,100):
    str=""
    for y in range(97,x+1):
        str+=chr(y)
    print(str)       
    
n=6
sum=0
for x in range(1,n):
    if (n%x==0):
        sum+=x
    if(x==sum):
        print("perfect number")

