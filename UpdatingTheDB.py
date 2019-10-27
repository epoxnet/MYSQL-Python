#Updating data
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Software2019",
    database="WaterAmerica"
    )

mycursor = mydb.cursor()

#UPDATING
sql = "UPDATE waTable SET MovingAdrr=NULL WHERE Account=3"
#sql = "UPDATE waTable SET Date=NULL WHERE Account=3"
mycursor.execute(sql)

mydb.commit() #Saving the changes


