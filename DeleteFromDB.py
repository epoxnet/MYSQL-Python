#Deleting data
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Software2019",
    database="WaterAmerica"
    )

mycursor = mydb.cursor()

sql= "DELETE FROM waTable WHERE account=3"

mycursor.execute(sql)

mydb.commit()
