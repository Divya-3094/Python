# req = res life cycle
#front-end to backend
#prompt--> request
#data--> res

#API--->Application Programming Interface
#an api call allows your pythin program to communicate with external services(like websites and databases)
#www.amazon.com/mobiles/s25----->URL(Uniform Resourse Locator)/end point/API

#front-end----->HTML,CSS,JS/REACT.JS
#backend--->Python/java/c/c++

#built in module/ user defined module / third party module

#HTTP METHODS:- Hyper text transfer protocol /secured
#instagram
#signup--->phno, email, name,dob---> POST Method
#login
#reels-->GET method
#forgot password-->Updation
#delete-->delete

#CRUD--> create   read/retrive  update delete
#Method      POST        GET        PUT/PATCH           DELETE
#
#http responce code
#1xx-->information
#2xx-->success message
#3xx-->redirection message
#4xx-->client side errors
#5xx-->server side errors

#requests--> post get put/patch delete
#json dumps() method-->converts python objects to json strings format
#post-->
#get-->
#put-->replaces entire dictionary
#patch-->replaces specific key value
#JSON--> java script object notation
#requests
#.get(api).json()
# import requests

# import json

# data=requests.get("https://fakestoreapi.com/products")
# print(data.json())

# for pro in data.json():
#     print(pro["title"])

# # api='http://127.0.0.1:8000/students'
# # stu_data=requests.get(api)
# # print(stu_data.json())

# details={
#     "name":"divya",
#     "email":"divya@gmail.com",
#     "batch":"53r",
#     "mobileno":"6305078330"
# }

# res=requests.post()

#28/10/2025
#requset module--used to interact with server/to communicate with server through API'S
#there are some  http methods post get put/patch delete these are all methods called CRUD Operations

#http response code 
#5-types
#1 2 3 4 5

import requests

import json

# data=requests.get("https://fakestoreapi.com/products")
# print(data.json())

# new_user={
#     "id":10,
#     "name":"Divya",
#     "email":"divya@gmail.com",
    
# }
# new_user=json.dumps(new_user)
# send_data=requests.post("",data=new_user)
# print(send_data)
# api=""
# add_data=requests.post(api,json=new_user)
# print(send_data)

#head-->every time your browser or script sends a request to a webserver, headers accompany that request. 
# they inform the server abhout who is making the request, what type of data is being sort
#body-->the data we are sending

#authentication-->it defines who u are --it checks whether we are the user or not.
#authorization-->what you can do--gives permission for what we have to do
#  perticular facility 

#api ninjas---website

# head={
#     "key":"value"
# }
# requests.post("url",headers=head)

api="https://api.api-ninjas.com/v1/dogs?name=golden retriever"
head={
    "x-Api-Key":"Z1zDx22kLFxWBbEjf0okWQ==TQ0McZZBZdFMOaGj"
}
dog_data=requests.get(api,headers=head,timeout=1)
print(requests.options(api))
print(dog_data.json())

#data= requests body
#info about api=requests.headers

