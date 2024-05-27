from fastapi import FastAPI

from models.mysql_database import Mysql_database

mySql=Mysql_database()
server = FastAPI()

#test the server is up
@server.get("/test")
def test():

    x=Mysql_database()
    x.get_pokemon_by_type("fire")
    return "The server is working properly!"