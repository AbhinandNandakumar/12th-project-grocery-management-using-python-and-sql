import mysql.connector as c
cnx=c.connect(host='localhost',user='root',password='12345')
crs=cnx.cursor()

crs.execute("create database grocerry")
crs.execute('use grocerry')
crs.execute("create table user(UID varchar(5),PWD varchar(20))")
crs.execute("create table workers(WID char(5),WNM char(20), POSITION  char(15), W_Hrs int,SALARY float)")
crs.execute("create table products(PNO varchar(5),PNM  varchar(15),QTY  int,COST float)")
crs.execute("create table suppliers(SNM  varchar(20),PNM  varchar(20),QTY  int,B_AMT float)")
crs.execute("create table customers(CNM  varchar(15),PURCHASED_AMT float)")
cnx.commit()
cnx.close()
