# 1.	Get trainers of a pokemon: get all the trainers of a given pokemon
from fastapi import APIRouter, HTTPException, Depends
from models.mysql_database import Mysql_database, get_db

router = APIRouter(
    prefix='/trainers',
    tags=['This is all  requests for trainers resources ']
)
pokemon_db = Mysql_database() ## func return pokemon_db


@router.get("/get-pokemon-trainer")
def get_pokemon_trainer()-> list:
    pass

@router.put("/add-pokemon/{pokemon_id}/-to-trainer/{trainer_id}")
def add_pokemon_to_trainer(pokemon_id: int, trainer_id: int, pokemon_db=Depends(get_db)):
    pokemons = pokemon_db.get_pokemon_by_id(pokemon_id)
    if not pokemons:
        raise HTTPException(status_code=404, detail="No Pokémon found with the given ID")
    pokemons = pokemon_db.get_trainer_by_id(pokemon_id)
    if not pokemons:
        raise HTTPException(status_code=404, detail="No trainer found with the given ID")
    if pokemon_db.add_pokemon_to_trainer(pokemon_id, trainer_id):
        print("Pokemon added successfully to trainer.")
        return {"message": "Pokemon added successfully to trainer."}