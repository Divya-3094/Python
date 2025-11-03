import random
import json

def signUp():
    with open('../data/data.json','r') as f:
       username=input("Enter UserName : ")
       email=input("Enter Email : ")
       password=input("Enter Password : ")
       user_id=generateUserId(username)
       user_info={
                  "user_id":user_id,
                  "username":username,
                  "email":email,
                  "password":password
                  }
       print(f"your userid is {user_id}")
       users=json.load(f)
       users["users"].append(user_info)
    with open("../data/data.json","w") as f:
        json.dump(users,f,indent=4)
        print("signup is done") 
        
          
def generateUserId(username):
    user_id=username[0:3]+str(random.randint(9999,99999))
    return user_id

   
