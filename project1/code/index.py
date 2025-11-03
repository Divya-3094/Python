import json
from auth import signUp


def start():
    ip=int(input("Enter Choice : "))
    if ip==1:
        signUp()
    # elif ip==2:
    #     login()
    else:
        print("Invalid input") 
start()
      

