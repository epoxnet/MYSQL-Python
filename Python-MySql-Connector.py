#Python & MySql Connector

import mysql.connector

mydb = mysql.connector.connect(
                               host="localhost",
                               user="root",
                               passwd="Software2019"
                               )


if (mydb): # test to make sure that connection works!
    print("Connection Successful")

else:
    print("Connection Unsuccessful")


mycursor = mydb.cursor() #cursor is the controler , like a pointer


#create a database
mycursor.execute("Create database WaterAmerica1")# nameofdatabase ex. WaterAmerica


#show database
mycursor.execute("Show databases")

for db in mycursor: #loop through all the databases
    print(db) #printing all the databases 
