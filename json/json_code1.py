#json crud operations on lists and dictionaries

# import json

# ip=['apple','banana','grapes']

# with open('data.json','w') as f:

#     #using dumps() method
#     f.write(json.dumps(ip))

#     #using dump() method
#     json.dump(ip,f)

# #dumps---->only converts to json
# #dump---->converts to json and stores in file

# with open('data.json','r') as f:

# #    using loads() method
#     data=f.read()
#     cnvrt_data=json.loads(data)  
#     print(cnvrt_data[2])

# #    using load() method
#     data=json.load(f)
#     print(data[1])

# #when the data is in the form of list

# ip1='jackfruit'
# with open('data.json','r') as f:
#     data=json.load(f)   # converts from json str format to python list format
#     if ip1 not in data:
#        data.append(ip1)   #adding new element into the list
#     else:
#         print(f'{ip1} already exists')   
# with open('data.json','w') as f:
#     json.dump(data,f)
#     print('data updated successfully')


# #how to remove an elemnet from the list

# ip1='grapes'
# with open('data.json','r') as f:
#     data=json.load(f)   # converts from json str format to python list format
#     if ip1  in data:
#        data.remove(ip1) 
#        print(f'{ip1} fruit removed successfully')  #removing element into the list
#     else:
#         print(f'{ip1} is not available')   
# with open('data.json','w') as f:
#     json.dump(data,f)
#     print('data updated successfully')

# #when the data is in the form of dictionary

# ip1='pineapple'
# with open('data.json','r') as f:
#     data=json.load(f)   # converts from json str format to python dict format
#     if ip1 not in data["fruits"]:
#        data["fruits"].append(ip1)   #adding new element into the dict
#     else:
#         print(f'{ip1} already exists')   
# with open('data.json','w') as f:
#     json.dump(data,f)
#     print('data updated successfully')

# #how to remove perticular element from dictionary

# ip1='pineapple'
# with open('data.json','r') as f:
#     data1=json.load(f)
#     if ip1 in data1["fruits"]:
#         data1["fruits"].remove(ip1)
#         print(f'{ip1} fruit removed successfully')
#     else:
#         print(f'{ip1} is not available')    
# with open('data.json','w') as f:
#     json.dump(ip1,f)
#     print('data is updated')        

# #removing the element in dictionary 
    
# remove_element="grapes"
# file_name='data.json'
# with open(file_name,'r') as h:
#     data=json.load(h)
#     if remove_element not in data["fruits"]:
#         print(f'{remove_element} is not availabale')
#     else:
#         data["fruits"].remove(remove_element)
#         print(f'{remove_element} is removed successfully')
# with open(file_name,'w') as f:
#      json.dump(data,f,indent=4)      

# #authorised person can remove element otherwise there is no chance for performing operation
# #authorised person can only perform operation

# remove_element=input("enter fruit name : ")
# file_name='data.json'
# user=input("enter user name : ")
# with open(file_name,'r') as h:
#     data=json.load(h)
#     if user in data["users"]:
#         if remove_element not in data["fruits"]:
#            print(f'{remove_element} is not available')
#         else:
#            data["fruits"].remove(remove_element)
#            print(f'{remove_element} is removed successfully')
#     else:
#         print("you are not authorised to perform remove operation")       
# with open(file_name,'w') as f:
#     json.dump(data,f,indent=4)            

# #authorised person can add element otherwise there is no chance for performing operation.
# #authorised person can only perform operation

# add_element=input("enter fruit name : ")
# file_name='data.json'
# user=input("enter user name : ")
# with open(file_name,'r') as h:
#     data=json.load(h)
#     if user in data["users"]:
#         if add_element in data["fruits"]:
#             print(f'{add_element} is already exists')
#         else:
#              data["fruits"].append(add_element)
#              print(f'{add_element} is added successfully')
#     else:
#         print("you are not authorised to perform operation")
# with open(file_name,'w') as f:
#     json.dump(data,f,indent=4)                    

