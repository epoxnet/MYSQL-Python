 #inserting values inside the table
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Software2019",
    database="WaterAmerica1"
    )

mycursor = mydb.cursor()


sqlform = "Insert into waTable(Account ,Name , Phone, Email, MovingAdrr, Date, Password, Username) values (%s, %s, %s, %s, %s, %s, %s, %s)"

users = [(1 , "test1", 2069109103, "dehghaniSean@gmail.com" , "N/A", 0, "test1", "test1" )]



mycursor.executemany(sqlform, users)

mydb.commit() #Save my changes


#CODE FOR MYSQL Workbench : (SELECT * FROM WaterAmerica.waTable;)
