import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='',database='librarymanagementdb')
mycursor=mydb.cursor()
while True:
    print("select an option from the menu")
    print("1. add book:-")
    print("2.view book:-")
    print("3.search book:-")
    print("4.upadte book:-")
    print("5. delete book:-")
    print("6.exit")

    choice=int(input("enter your choice:-"))
    if(choice==1):
        print("add book:")
        title=input("enter a book name:")
        author=input("enter author name:-")
        catagory=input("enter catagory:-")
        chargeperday=input("enter chargeperday:-")
        copies=input("enter copies:- ")
        sql="INSERT INTO `books`(`title`, `author`, `catagory`, `chargeperday`, `copies`) VALUES (%s,%s,%s,%s,%s)"
        data=(title,author,catagory,chargeperday,copies)
        mycursor.execute(sql,data)
        mydb.commit()
        print("insert successfully.......")
    elif(choice==2):
        print("view book")
        sql="SELECT * FROM `books` "
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==3):
        print("search a book") 
        title=input("enter a book title:-")
        sql="SELECT * FROM `books` WHERE `title`='"+title+"'"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        print(result) 
    elif(choice==4):
        print("update book")
        title=input("enter a book name:")
        author=input("enter author name to be updated:-")
        catagory=input("enter catagory to be updated:-")
        chargeperday=input("enter chargeperday to be updated:-")
        copies=input("enter copies to be updated:- ")
        sql="UPDATE `books` SET `author`='"+author+"',`catagory`='"+catagory+"',`chargeperday`='"+chargeperday+"',`copies`='"+copies+"' WHERE `title`='"+title+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("Data updated successfully....")
    elif(choice==5):
        print("delete employe")  
    elif(choice==6):
        break      
