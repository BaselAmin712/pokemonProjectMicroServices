#1.	Get pokemons by type: returns all pokemons with the specific type
#2.	Get pokemons by trainer: get all the pokemons of a given owner
#3.	Get trainers of a pokemon: get all the trainers of a given pokemon
from fastapi import APIRouter, HTTPException

#router to students
from models.mysql_database import Mysql_database

router = APIRouter(
    prefix = '/info',
    tags = ['This is all informative requests to the server ']
    
)
pokemon_db = Mysql_database()
@router.get("/get-by-type/type_name")
def get_by_type(type_name: str) ->list:
    pokemons = pokemon_db.get_pokemon_by_type(type_name)
    if not pokemons:
        raise HTTPException(status_code=404, detail="No Pokémon found for the given type")
    return pokemons

@router.get("/get-by-name/{name}")
def get_by_name(name: str):
    pokemons = pokemon_db.get_pokemon_by_name(name)
    if not pokemons:
        raise HTTPException(status_code=404, detail="No Pokémon found with the given name")
    return pokemons[0]

@router.get("/get-by-id/{id}")
def get_by_id(id: str):
    pokemons = pokemon_db.get_pokemon_by_id(id)
    if not pokemons:
        raise HTTPException(status_code=404, detail="No Pokémon found with the given id")
    return pokemons[0]


@router.get("/get-by-trainer")
def get_by_trainer()-> list:
    pass


@router.get("/get-pokemon-trainer")
def get_pokemon_trainer()-> list:
    pass