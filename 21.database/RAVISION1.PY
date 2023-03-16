
import pymysql

mydb=pymysql.connect(host="localhost",user="root",password="")
mycorsor=mydb.cursor()

mycorsor.execute("create database if not exists nilu")
mydb.commit()

mydb=pymysql.connect(host="localhost",user="root",password="",database="nilu")
mycorsor=mydb.cursor()
mydb.commit()

mycorsor.execute("create table if not exists student (id int not null primary key,name varchar(20),email varchar(20),subject varchar(20),address varchar(50))")
mydb.commit()

def adddata():
    id=input("Enter Your id : ")
    name=input("Enter Your name : ")
    email=input("Enter Your email : ")
    subject=input("Enter Your subject : ")
    address=input("Enter Your address : ")

    student=(id,name,email,subject,address)
    query="insert into student (id,name,email,subject,address) values ('%s','%s','%s','%s','%s')"
    mycorsor.execute(query%student)
    mydb.commit()
    print("students add")

# adddata()

def deleteData():
    id=int(input("Enter your id : "))

    student=(id)
    query="DELETE from student where id='%s'"
    mycorsor.execute(query%student)
    mydb.commit()
    print("student deleted")

# deleteData()

def update():
    id=input("Enter your id : ")

    student=(id)
    query="UPDATE student SET name='nilesh' WHERE id='%s'"
    mycorsor.execute(query%student)
    mydb.commit()
    print("student updated")

# update()    

def readdata():
    query="SELECT * FROM student"
    mycorsor.execute(query)
    n=mycorsor.fetchall()
    for i in n:
        print(i)

readdata()        