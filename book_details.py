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
    elif(choice==2):
        print("view book")
    elif(choice==3):
        print("search a book")  
    elif(choice==4):
        print("update book")
    elif(choice==5):
        print("delete employe")  
    elif(choice==6):
        break      
