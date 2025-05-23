import mysql.connector

con = mysql.connector.connect(
    host="giniewicz.it",
    user="student",
    password="75u>3n7",
    database="sakila"
)

if con:
    print("Połączenie udane")
else:
    print("Połączenie nieudane")