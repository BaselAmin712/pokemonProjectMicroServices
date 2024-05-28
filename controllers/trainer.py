# 1.	Get trainers of a pokemon: get all the trainers of a given pokemon
from fastapi import APIRouter, HTTPException
from models.mysql_database import Mysql_database

router = APIRouter(
    prefix='/trainers',
    tags=['This is all  requests for trainers resources ']
)
pokemon_db = Mysql_database() ## func return pokemon_db

@router.get("/get-by-trainer")
def get_by_trainer()-> list:
    pass


@router.get("/get-pokemon-trainer")
def get_pokemon_trainer()-> list:
    pass

@router.post("/add-pokemon-to-trainer")
def add_pokemon_to_trainer():
    pass