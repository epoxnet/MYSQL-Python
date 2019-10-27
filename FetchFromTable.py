import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Software2019",
    database="WaterAmerica"
    )

mycursor = mydb.cursor()

#Fetch ONE

#mycursor.execute("Select name from waTable")

#mycursor.execute("Select account from waTable")

#mycursor.execute("Select movingadrr from waTable")

#mycursor.execute("Select phone from waTable")

#mycursor.execute("Select date from waTable")

#mycursor.execute("Select password from waTable")

#mycursor.execute("Select email from waTable")

#myresult = mycursor.fetchone()

#Fetch ALL

mycursor.execute("select * from waTable")

myresult = mycursor.fetchall()

for row in myresult:
    print (row)


