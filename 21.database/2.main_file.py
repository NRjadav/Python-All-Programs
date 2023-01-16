
# pip install pymysql

import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="",database="12_sep_python")
mycursor = mydb.cursor()

def addData():
    name=input("Enter your name : ")
    email=input("Enter your email : ")

    student=(name,email)
    query="insert into student (name,email) values ('%s','%s')"
    mycursor.execute(query%student)
    mydb.commit()
    print("Student add")

addData()



