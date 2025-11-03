#Python DataBase Connection/Connectivity (PDBC)
#method1
import mysql.connector

from db import info
try:
    mysql.connector.connect(**info)
    print('connection successful')
except:
    print('not able to connect')

#method2
import mysql.connector
info={
    'user':'root',
    'password':'Divyav@2004',
    'host':'localhost',
    'port':3306
}
try:
    mysql.connector.connect(**info)
    print('connection successful')
except:
    print('not able to connect')

#method3
import mysql.connector

try:
    mysql.connector.connect(
    user='root',
    password='Divyav@2004',
    host='localhost',
    port=3306
)
    print('connection successful')
except:
    print('not able to connect')


# import mysql.connector 
# from db import info
# from getRecords import getRecords
# from getRecords import getStudentsByCourse
# from getRecords import getLimitedRecords

try:
    conn=mysql.connector.connect(**info)
    print('connection successful')
except:
    print('not able to connect')
cursor=conn.cursor()


#to create database
query='CREATE DATABASE if not exists 10000CODERS_new'
cursor.execute(query)
#using/selecting database
cursor.execute("use 10000coders")


#creating a table with id,name,email,course,joined_date
try:
    create_table="""create table if not exists students_new_1(
    id INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(100),EMAIL VARCHAR(100),
    COURSE VARCHAR(100),JOINED_DATE DATE);"""
    cursor.execute(create_table)
    print('table created successfully')
except mysql.connector.errors.ProgrammingError as e :
    print(e)



#insert single row of data
# def insertSingleRow(data):
#     try:
#         insertdata="""insert into students (name,email,course,joined_date) values(%s,%s,%s,%s)"""
#         cursor.execute(insertdata,data)
#         print('data inserted ')
#     except:
#         print('something went wrong')

# insertSingleRow(('suresh','suresh@gmail.com','PFS','2025-02-06'))
# insertSingleRow(('akhil','akhil@gmail,com','PFS','2025-06-06'))
# insertSingleRow((input('enter name:'),input('enter email:'),input('enter course'),input('enter joined date')))

# insert multiple rows at a time
# def insertMultipleRows(data):
#     try:
#         insertquery="""insert into students (name,email,course,joined_date) values (%s,%s,%s,%s)"""
#         cursor.executemany(insertquery,data)
#     except:
#         print('something went wrong')

# insertMultipleRows([('shanmukh','shanmukh@gmail.com','PFS','2025-05-06'),
#             ('tharun','tharun@gmail.com','PFS','2025-05-06'),
#             ('saranya','saranya@gmail.com','PFS','2025-05-06')])




# getRecords()



# getStudentsByCourse('PFS')


# getLimitedRecords(2)

def updateCourseByEmail(course,email):
    try:
        query="""update students set course = %s where email = %s"""
        cursor.execute(query,(course,email))
        print("data updated successfully")
    except:
        print("something went wrong")
# updateCourseByEmail('PFS','harish@gmail.com')

def updateNameAndCourseByEmail(new_name,new_course,email):
    try:
        query="""update students set name=%s,course=%s where email=%s"""
        cursor.execute(query,(new_name,new_course,email))
        print('record is updated')
    except:
        print("something went wrong")
        
# updateNameAndCourseByEmail('rishi','DS','harish@gmail.com')

# getRecords()

def deleteRecordById(id):
    try:
        query="""delete from students where id= %s"""
        cursor.execute(query,(id,))
        print("record deleted successfully")
    except:
        print("something went wrong")
deleteRecordById(int(input('enter id')))
conn.commit()
cursor.close()
conn.close()

import mysql.connector 
from db import info

try:
    conn=mysql.connector.connect(**info)
    print('connection successful')
except:
    print('not able to connect')
cursor=conn.cursor()

def getRecords():
    try:
        cursor.execute('use 10000coders')
        query='select * from students'
        cursor.execute(query)
        results=cursor.fetchall()
        for row in results:
            print(row)        
    except:
        print('error occurred')
def getStudentsByCourse(course_name):
    try:
        query="""select * from students where course= %s"""
        print(query)
        cursor.execute(query,(course_name,))
        results=cursor.fetchall()
        for x in results:
            print(x)
        # print(results)
    except:
        print('something went wrong')
def getLimitedRecords(limit):
    try:
        query="""select * from students  order by name asc limit %s"""
        cursor.execute(query,(limit,))
        result=cursor.fetchall()
        print(result)
    except:
        print("something went wrong")
    finally:
        print("task completed")