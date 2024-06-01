# 1.	Get trainers of a pokemon: get all the trainers of a given pokemon
from fastapi import APIRouter, HTTPException
from models.mysql_database import Mysql_database

router = APIRouter(
    prefix='/trainers',
    tags=['This is all  requests for trainers resources ']
)
pokemon_db = Mysql_database() ## func return pokemon_db


@router.get("/get-pokemon-trainer")
def get_pokemon_trainer()-> list:
    pass

@router.post("/add-pokemon-to-trainer")
def add_pokemon_to_trainer(pokemon:str, trainer:str):
    pokemon_id = pokemon_db.get_pokemon_by_name(pokemon)[0][0]
    if not pokemon_id:
        raise HTTPException(status_code=404, detail="No Pokémon found with the given name")
    trainer_id = pokemon_db.get_trainer_by_name(trainer)[0][0]
    if not trainer_id:
        raise HTTPException(status_code=404, detail="No Trainer found with the given name")
    if not pokemon_db.check_trainer_and_pokemon(pokemon_id,trainer_id):
        raise HTTPException(status_code=404, detail="Pokémon is not in trainer hand")
    added_pokemon = pokemon_db.add_pokemon_to_trainer(pokemon_id,trainer_id)
    if added_pokemon:
        print("Pokemon evolved successfully.")
        return {"message": "Pokemon evolved successfully."}
