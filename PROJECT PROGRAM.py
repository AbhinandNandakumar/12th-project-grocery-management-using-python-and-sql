print('\n'*15)
print('='*111)
print('*'*102)
print()
print("GROCERY MANAGEMENT SYSTEM".center(160))
print('*'*102)
print('='*111)
print('\n'*1)
import mysql.connector as c
cnx=c.connect(host='localhost',user='root',password='12345',database='grocery')
crs=cnx.cursor()

# function containing worker details

def w_ds():
     enter()
     print("|  WORKER DETAILS   |".center(101,'*'))
     print('\n'*4)
     print("\n\t\t\t\t  ",'*'*34)
     print("\t\t\t\t   |  1.SHOW WORKER DETAILS              |\n\t\t\t\t   |  2.EDIT DETAILS                                |\n\t\t\t\t   |  3.DELETE DETAILS                            |\n\t\t\t\t   |  4.ADD NEW WORKER DETAILS        |")
     print("\t\t\t\t   ",'*'*34)
     print('\n'*3)
     cho=int(input("\n\t\t\t\t    ENTER YOUR CHOICE : "))
     if cho==1:
        crs.execute('select * from workers')
        x=crs.fetchall()
        print('\n\t\t    |    WID     |                     WNM                 |      POSITION      |    W_Hrs    |    SALARY    |')
        for i in x:
             print('\n\t\t\t\t    ',i)
     elif cho==2:
          try:
               wid=input("\n\t\t\t\t    ENTER THE WORKER ID : ")
               old=input("\n\t\t\t\t    ENTER WHAT TO BE CHANGED \n\t\t\t\t    ( WID / WNM / POSITION / W_Hrs / SALARY ) : ")
               new=input("\n\t\t\t\t    ENTER THE CHANGE : ")
               if new.isdigit():
                    crs.execute("update workers set {}={} where wid='{}'".format(old,new,wid))
               else:
                    crs.execute("update workers set {}='{}' where wid='{}'".format(old,new,wid))
               cnx.commit()
               print("\n\t\t\t\t    SUCCESSFULLY UPDATED")
          except:
               print("\n\t\t\t\t    GIVEN INFORMATION NOT CORRECT")
     elif cho==3:
          wid=input("\n\t\t\t\t    ENTER THE ID OF WORKER TO BE DELETED : ")
          crs.execute("select * from workers")
          x=crs.fetchall()
          a=0
          for i in x:
               if i[0].lower()==wid.lower():
                    a=1
                    crs.execute("delete from workers where wid='{}'".format(wid))
                    cnx.commit()
          if a==1:
               print("\n\t\t\t\t    WORKER",wid,"DELETED")
          else:
               print("\n\t\t\t\t    INVALID WORKER ID !!")
          
     elif cho==4:
          try:
               wid=input("\n\t\t\t\t    ENTER THE WORKER ID : ")
               wnm=input("\n\t\t\t\t    ENTER THE NAME OF WORKER  : ")
               pos=input("\n\t\t\t\t    ENTER THE POSITION : ")
               w_hr=int(input("\n\t\t\t\t    ENTER THE NUMBER OF WORKING HOURS : "))
               sal=float(input("\n\t\t\t\t    ENTER THE SALARY : "))
               crs.execute("insert into workers values('{}','{}','{}',{},{})".format(wid,wnm,pos,w_hr,sal))
               cnx.commit()
               print("\n\t\t\t\t    WORKER {} ADDED".format(wnm))
          except:
               print("\n\t\t\t\t    FOUND AN ERROR IN DETAILS, PLEASE RECHECK")
     else:
         print("\n\t\t\t\t    INVALID CHOICE !!")
         print("\n\t\t\t\t    PLEASE ENTER YOUR CHOICE ONCE AGAIN ")
         w_ds()
     x=input("\n\t\t\t\t    BACK TO WORKER MENU OR EXIT (m/e)  : ")
     if x in "Mm":
          w_ds()
     else:
          b_m()

# function containing product details

def p_ds():
    enter()
    print("|      PRODUCT DETAILS      |".center(106,'*'))
    print('\n'*4)
    print("\n\t\t\t\t  ",'*'*32)
    print("\t\t\t\t   |  1.SHOW PRODUCT DETAILS          |\n\t\t\t\t   |  2.EDIT DETAILS                             |\n\t\t\t\t   |  3.DELETE DETAILS                         |\n\t\t\t\t   |  4.ADD NEW PRODUCT DETAILS    |")
    print("\t\t\t\t   ",'*'*32)
    print('\n'*3)
    cho=int(input("\n\t\t\t\t    ENTER YOUR CHOICE : "))
    if cho==1:
         crs.execute('select * from products')
         x=crs.fetchall()
         print('\n\t\t \t\t   |  PNO   |     PNM      | QTY  |   COST  |') 
         for i in x:
             print('\n\t\t\t\t    ',i)
    elif cho==2:
          try:
               pno=input("\n\t\t\t\t    ENTER THE PRODUCT NUMBER : ")
               old=input("\n\t\t\t\t    ENTER WHAT TO BE CHANGED \n\t\t\t\t    (PNO / PNM / QTY/ COST) : ")
               new=input("\n\t\t\t\t    ENTER THE CHANGE : ")
               if new.isdigit():
                    crs.execute("update products set {}={} where pno='{}'".format(old,new,pno))
               else:
                    crs.execute("update products set {}='{}' where pno='{}'".format(old,new,pno))
               cnx.commit()
               print("\n\t\t\t\t    SUCCESSFULLY UPDATED")
          except:
               print("\n\t\t\t\t    GIVEN INFORMATION NOT CORRECT")
    elif cho==3:
         pno=input("\n\t\t\t\t    ENTER THE PRODUCT NUMBER TO BE DELETED : ")
         crs.execute("select * from products")
         x=crs.fetchall()
         a=0
         for i in x:
              if i[0].lower()==pno.lower():
                   a=1
                   crs.execute("delete from products where pno='{}'".format(pno))
                   cnx.commit()
         if a==1:
               print("\n\t\t\t\t    PRODUCT",pno,"DELETED")
         else:
               print("\n\t\t\t\t    INVALID PRODUCT NUMBER !!")
          
    elif cho==4:
         try:
               pno=input("\n\t\t\t\t    ENTER THE PRODUCT NUMBER : ")
               pnm=input("\n\t\t\t\t    ENTER THE NAME OF THE PRODUCT : ")
               qty=int(input("\n\t\t\t\t    ENTER THE QUANTITY : "))
               c=int(input("\n\t\t\t\t    ENTER THE COST : "))
               crs.execute("insert into products values('{}','{}',{},{})".format(pno,pnm,qty,c))
               cnx.commit()
               print("\n\t\t\t\t    PRODUCT {} ADDED".format(pnm))
         except:
               print("\n\t\t\t\t    FOUND AN ERROR IN DETAILS, PLEASE RECHECK")
    else:
         print("\n\t\t\t\t    INVALID CHOICE !!")
         print("\n\t\t\t\t    PLEASE ENTER YOUR CHOICE ONCE AGAIN ")
         p_ds()
    x=input("\n\t\t\t\t    BACK TO PRODUCT MENU OR EXIT (m/e)  : ")
    if x in "Mm":
         p_ds()
    else:
         b_m()

# function containing supplier details
          
def s_ds():
     enter()
     print("|  SUPPLIER DETAILS   |".center(103,'*'))
     print('\n'*4)
     print("\n\t\t\t\t  ",'*'*33)
     print("\t\t\t\t   |  1.SHOW SUPPLIER DETAILS          |\n\t\t\t\t   |  2.EDIT DETAILS                              |\n\t\t\t\t   |  3.DELETE DETAILS                          |\n\t\t\t\t   |  4.ADD NEW SUPPLIER DETAILS    |")
     print("\t\t\t\t   ",'*'*33)
     print('\n'*3)
     cho=int(input("\n\t\t\t\t    ENTER YOUR CHOICE : "))
     if cho==1:
         crs.execute('select * from suppliers')
         x=crs.fetchall()
         print('\n\t\t\t\t    |      SNM        |    PNM     |   QTY    |   B_AMT   |')
         for i in x:
             print('\n\t\t\t\t    ',i)
     elif cho==2:
         try:
               snm=input("\n\t\t\t\t    ENTER CORRECT SUPPLIER NAME : ")
               old=input("\n\t\t\t\t    ENTER WHAT TO BE CHANGED \n\t\t\t\t    (SNM / PNM / QTY / B_AMT) : ")
               new=input("\n\t\t\t\t    ENTER THE CHANGE : ")
               if new.isdigit():
                    crs.execute("update suppliers set {}={} where snm='{}'".format(old,new,snm))
               else:
                    crs.execute("update suppliers set {}='{}' where snm='{}'".format(old,new,snm))
               cnx.commit()
               print("\n\t\t\t\t    SUCCESSFULLY UPDATED")
         except:
               print("\n\t\t\t\t    GIVEN INFORMATION NOT CORRECT")
     elif cho==3:
         snm=input("\n\t\t\t\t    ENTER THE SUPPLIER NAME TO BE DELETED : ")
         crs.execute("select * from suppliers")
         x=crs.fetchall()
         a=0
         for i in x:
             if i[0].lower()==snm.lower():
                 a=1
                 crs.execute("delete from suppliers where snm='{}'".format(snm))
                 cnx.commit()
         if a==1:
             print("\n\t\t\t\t    SUPPLIER",snm,"DELETED")
         else:
             print("\n\t\t\t\t    INVALID SUPPLIER NAME !!")
          
          
     elif cho==4:
          try:
               snm=input("\n\t\t\t\t    ENTER THE SUPPLIER NAME : ")
               pnm=input("\n\t\t\t\t    ENTER THE NAME OF THE PRODUCT : ")
               qty=int(input("\n\t\t\t\t    ENTER THE QUANTITY : "))
               bal=float(input("\n\t\t\t\t    ENTER THE BALANCE AMOUNT TO BE PAID : "))
               crs.execute("insert into suppliers values('{}','{}',{},{})".format(snm,pnm,qty,bal))
               cnx.commit()
               print("\n\t\t\t\t    SUPPLIER {} ADDED".format(snm))
          except:
               print("\n\t\t\t\t    FOUND AN ERROR IN DETAILS, PLEASE RECHECK")
     else:
         print("\n\t\t\t\t    INVALID CHOICE !!")
         print("\n\t\t\t\t    PLEASE ENTER YOUR CHOICE ONCE AGAIN ")
         s_ds()
     x=input("\n\t\t\t\t    BACK TO SUPPLIER MENU OR EXIT (m/e)  : ")
     if x in "Mm":
          s_ds()
     else:
          b_m()

# function containing customer details

def c_ds():
     enter()
     print("|  CUSTOMER DETAILS   |".center(101,'*'))
     print('\n'*4)
     print("\n\t\t\t\t  ",'*'*34)
     print("\t\t\t\t   |  1.SHOW CUSTOMER DETAILS          |\n\t\t\t\t   |  2.EDIT DETAILS                                |\n\t\t\t\t   |  3.DELETE DETAILS                            |\n\t\t\t\t   |  4.ADD NEW CUSTOMER DETAILS    |")
     print("\t\t\t\t   ",'*'*34)
     print('\n'*3)
     cho=int(input("\n\t\t\t\t    ENTER YOUR CHOICE : "))
     if cho==1:
         crs.execute('select * from customers')
         x=crs.fetchall()
         print('\n\t\t\t\t    |     CNM      | PURCHASED_AMT|')
         for i in x:
             print('\n\t\t\t\t    ',i)
     elif cho==2:
         try:
               cnm=input("\n\t\t\t\t    ENTER CORRECT CUSTOMER NAME : ")
               old=input("\n\t\t\t\t    ENTER WHAT TO BE CHANGED \n\t\t\t\t    ( CNM / PURCHASED_AMT) : ")
               new=input("\n\t\t\t\t    ENTER THE CHANGE : ")
               if new.isdigit():
                    crs.execute("update customers set {}={} where cnm='{}'".format(old,new,cnm))
               else:
                    crs.execute("update customers set {}='{}' where cnm='{}'".format(old,new,cnm))
               cnx.commit()
               print("\n\t\t\t\t    SUCCESSFULLY UPDATED")
         except:
               print("\n\t\t\t\t    GIVEN INFORMATION NOT CORRECT")
     elif cho==3:
         cnm=input("\n\t\t\t\t    ENTER THE CUSTOMER NAME TO BE DELETED : ")
         crs.execute("select * from customers")
         x=crs.fetchall()
         a=0
         for i in x:
             if i[0].lower()==cnm.lower():
                 a=1
                 crs.execute("delete from customers where cnm='{}'".format(cnm))
                 cnx.commit()
         if a==1:
               print("\n\t\t\t\t    CUSTOMER",cnm,"DELETED")
         else:
               print("\n\t\t\t\t    INVALID CUSTOMER NAME !!")
          
     elif cho==4:
          try:
               cnm=input("\n\t\t\t\t    ENTER THE CUSTOMER NAME : ")
               p_amt=float(input("\n\t\t\t\t    ENTER THE PURCHASED AMOUNT : "))
               crs.execute("insert into customers values('{}',{})".format(cnm,p_amt))
               cnx.commit()
               print("\n\t\t\t\t    CUSTOMER {} ADDED".format(cnm))
          except:
               print("\n\t\t\t\t    FOUND AN ERROR IN DETAILS, PLEASE RECHECK")
     else:
         print("\n\t\t\t\t    INVALID CHOICE !!")
         print("\n\t\t\t\t    PLEASE ENTER YOUR CHOICE ONCE AGAIN ")
         c_ds()
     x=input("\n\t\t\t\t    BACK TO CUSTOMER MENU OR EXIT (m/e)  : ")
     if x in "Mm":
          c_ds()
     else:
          b_m()

# menu provided after login or sign in

def mgnt():
    print('\n'*3)
    print("|   WELCOME     |".center(104,"*"))
    print('\n'*3)
    print("\n\t\t\t\t  ",'*'*34)
    print("\t\t\t\t   |  1.WORKER DETAILS                           |\n\t\t\t\t   |  2.PRODUCT DETAILS                         |\n\t\t\t\t   |  3.SUPPLIER DETAILS                        |\n\t\t\t\t   |  4.CUSTOMER DETAILS                      |")
    print("\t\t\t\t   ",'*'*34)
    print('\n'*3)
    ch=int(input("\n\t\t\t\t    ENTER YOUR CHOICE : "))
    if ch==1:
        w_ds()
    elif ch==2:
        p_ds()
    elif ch==3:
         s_ds()
    elif ch==4:
         c_ds()
    else:
        print("\n\t\t\t\t    INVALID CHOICE !!")
        print("\n\t\t\t\t    PLEASE ENTER YOUR CHOICE ONCE AGAIN ")
        mgnt()

def b_m():
     while True:
          x=input("\n\t\t\t\t    BACK TO MAIN MENU OR SIGN OUT (m/e) : ")
          if x in 'eE':
               break
          elif x in'Mm':
               mgnt()
          else:
               print("\n\t\t\t\t    INVALID CHOICE !!! ")
        
# function to login to the database

def login():
    lgid=input("\n\t\t\t\t    ENTER YOUR USER ID : ")
    crs.execute("select uid from user where uid='{}'".format(lgid))
    x=crs.fetchall()
    if len(x)==0:
        print("\n\t\t\t\t    NO SUCH  USER ID FOUND")
    else:
        pwd=input("\n\t\t\t\t    ENTER YOUR PASSWORD : ")
        crs.execute("select pwd from user where pwd='{}'".format(pwd))
        a=crs.fetchall()
        if len(a)==0:
            print("\n\t\t\t\t    PASSWORD DOESN'T MATCH")
        else:
            print()
            print('\n'*9)
            mgnt()

# function to sign in to the database
            
def signin():
    snid=input("\n\t\t\t\t    ENTER THE USER ID PROVIDED BY COMPANY : ")
    pwd=input("\n\t\t\t\t    ENTER THE PASSWORD : ")
    
    crs.execute("insert into user values('{}','{}')".format(snid,pwd))
    cnx.commit()
    mgnt()

def enter():
     print('\n'*8)


while True:
    print('\n\t\t\t\t    1.LOG IN\n\t\t\t\t    2.SIGN UP\n\t\t\t\t    3.EXIT\n')
    print()
    ch=int(input("\t\t\t\t    ENTER YOUR CHOICE : "))
    if ch==1:
        login()
    elif ch==2:
        signin()
    elif ch==3:
        break
    else:
        print("\n\t\t\t\t    INVALID CHOICE !!! ")
    cho=input("\n\t\t\t\t    BACK TO LOGIN MENU OR EXIT (m/e) : ")
    if cho in 'eE':
        break
    elif cho in'Mm':
        continue
    else:
        print("\n\t\t\t\t    INVALID CHOICE !!! ")
        print("\n\t\t\t\t    SORRY !! \nYOU SHOULD TRY TO LOGIN AGAIN")
    
    
