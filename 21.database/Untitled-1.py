 
import pymysql

mydb=pymysql.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()

mycursor.execute("create database if not exists nrjadav")
mydb.commit()

mydb=pymysql.connect(host="localhost",user="root",password="",database="nrjadav")
mycursor=mydb.cursor()
mydb.commit()

mycursor.execute("create table if not exists student(firstname varchar(20),lastname varchar(20),email varchar(20))")
mydb.commit()
