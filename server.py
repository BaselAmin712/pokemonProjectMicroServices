from fastapi import FastAPI

from controllers import info_routes
from models.mysql_database import Mysql_database

mySql=Mysql_database()
server = FastAPI()
server.include_router(info_routes.router)
#test the server is up
@server.get("/test")
def test():

    x=Mysql_database()
    x.get_pokemon_by_type("fire")
    return "The server is working properly!"