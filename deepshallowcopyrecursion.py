#deepcopy & shallow copy
#shallow copy
import copy
info={'details':{'name':'divya','age':21,'city':'hyderabad'}}
x=copy.copy(info)   #shallow copy
y=copy.copy(info)   #shallow copy

x['details']['name']='chitti'
print(info)
print(x)
print(y)

score_board={'score':{'runs':135,'wickets':4,'overs':4.4}}
divya=copy.copy(score_board)   #shallow copy
chitti=copy.copy(score_board)   #shallow copy

chitti['score']['runs']+=6
print(score_board)
print(divya)
print(chitti)

#deep copy
score_board={'score':{'runs':135,'wickets':5,'overs':4.4}}
divya=copy.deepcopy(score_board)
chitti=copy.deepcopy(score_board)

divya['score']['wickets']-=1
print(score_board)
print(divya)
print(chitti)

pubg={'score':{'kills':0,'health':100}}
divya=copy.deepcopy(pubg)
chitti=copy.deepcopy(pubg)
cryso=copy.deepcopy(pubg)
cherry=copy.deepcopy(pubg)

chitti['score']['kills']+=4
divya['score']['health']-=25
print(pubg)
print(divya)
print(chitti)
print(cryso)
print(cherry)

#Recursion
def open_giftbox(n):
    if n>1:
        print(f'box {n} is opened')
        open_giftbox(n-1)
    else:
        print(f'gift box found in {n}')
open_giftbox(5)  

def factorial(n):
    fact=1
    if n==1 or n==0:
        return fact
    else:
        factorial_n=n*factorial(n-1)
        return factorial_n
print(factorial(5))    

