# 1.	Get trainers of a pokemon: get all the trainers of a given pokemon
from fastapi import APIRouter, HTTPException, Depends
from models.mysql_database import Mysql_database, get_db

router = APIRouter(
    prefix='/trainers',
    tags=['This is all  requests for trainers resources ']
)
pokemon_db = Mysql_database() ## func return pokemon_db


@router.get("/{pokemon_name}")
def get_pokemon_trainer(pokemon_name:str,pokemon_db=Depends(get_db))-> list:
    trainers=pokemon_db.get_trainers_of_pokemon(pokemon_name)
    if not trainers:
        raise HTTPException(status_code=404, detail="No pokemon found with the given name")
    return trainers
@router.post("/add-pokemon-to-trainer")
def add_pokemon_to_trainer():
    pass