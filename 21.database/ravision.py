
import pymysql

mydb=pymysql.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()

mycursor.execute("create database if not exists jayram")
mydb.commit()

mydb=pymysql.connect(host="localhost",user="root",password="",database="jayram")
mycursor=mydb.cursor()
mydb.commit()

mycursor.execute("create table if not exists Student (id int not null primary key ,name varchar(20),email varchar(20),subject varchar(20) ) ")
mydb.commit()

def addData():
    id=int(input("Enter your id : "))
    name=input("Enter your name : ")
    email=input("Enter your email : ")
    subject=input("Enter your subject : ")

    student=(id,name,email,subject)
    query="insert into student (id,name,email,subject) values ('%s','%s','%s','%s')"
    mycursor.execute(query%student)
    mydb.commit()
    print("Student add")

addData()

def deleteData():
    id=int(input("Enter your id : "))

    student=(id)
    query="DELETE from Student where id='%s'"
    mycursor.execute(query%student)
    mydb.commit()
    print("student deleted")

# deleteData()

