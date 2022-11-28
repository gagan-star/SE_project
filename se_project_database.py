import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ya@636156"
)
c=mydb.cursor()
c.execute("CREATE DATABASE IF NOT EXISTS PERISHABLE_MANAGEMENT")

