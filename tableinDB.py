
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Software2019",
    database="WaterAmerica1"
    )

mycursor = mydb.cursor()


#/creating table
mycursor.execute("Create table waTable(Account int(10),Name varchar(200),Phone int(10),Email varchar(300),MovingAdrr varchar(600),Date int(8),Password varchar(20),Username varchar(20))")

#showing the table
mycursor.execute("Show tables")

for tb in mycursor:
    print(tb)

#CODE FOR MYSQL Workbench : (Show tables;)
