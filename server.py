from fastapi import FastAPI

from controllers import pokemon, trainer
from models.mysql_database import Mysql_database

server = FastAPI()
server.include_router(pokemon.router)
server.include_router(trainer.router)

