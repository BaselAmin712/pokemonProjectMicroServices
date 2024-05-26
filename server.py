from fastapi import FastAPI

from models import mysql_database

mySql=mysql_database.Mysql_database()
server = FastAPI()

#test the server is up
@server.get("/test")
def test():

    cursor = mySql.connetion.cursor()
    cursor.execute("SELECT * FROM test")
    result = cursor.fetchall()
    print(result)
    return "The server is working properly!"