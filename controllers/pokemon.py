# 1.	Get pokemons by type: returns all pokemons with the specific type
# 2.	Get pokemons by trainer: get all the pokemons of a given owner
# 3.	Get trainers of a pokemon: get all the trainers of a given pokemon
from typing import Optional, List

from fastapi import APIRouter, HTTPException, Query, Depends
from models.schema import Pokemon
from models.mysql_database import Mysql_database, get_db

router = APIRouter(
    prefix='/pokemons',
    tags=['This is all  requests for pokemon resources ']
)


@router.get("/{pokemon_id}")
def get_pokemon_by_id(pokemon_id: int, pokemon_db=Depends(get_db)):
    pokemons = pokemon_db.get_pokemon_by_id(pokemon_id)
    if not pokemons:
        raise HTTPException(status_code=404, detail="No Pokémon found with the given ID")
    return pokemons[0]  # Return the first Pokémon in the list, assuming there's only one.


@router.post("/")
def create_pokemon(pokemon: Pokemon, pokemon_db=Depends(get_db)):
    existing_pokemon = pokemon_db.get_pokemon_by_id(pokemon.id)
    if existing_pokemon:
        raise HTTPException(status_code=409, detail="Pokemon found with the given id")
    existing_pokemon = pokemon_db.get_pokemon_by_name(pokemon.name)
    if existing_pokemon:
        raise HTTPException(status_code=409, detail="Pokemon found with the given name")

    pokemon_data = [pokemon.id, pokemon.name, pokemon.height, pokemon.weight]
    pokemon_added = pokemon_db.add_pokemon(pokemon_data)
    pokemon_db.add_pokemonsTypes(pokemon.id, pokemon.types)

    if pokemon_added:
        ##  update status code 201***********
        print("Pokemon added successfully.")
        return {"message": "Pokemon added successfully."}


@router.delete("/trainer/{trainer_name}/pokemon/{pokemon_name}" )
def delete_pokemon_from_trainer(trainer_name: str, pokemon_name: str, pokemon_db=Depends(get_db)):
    try:
        
        pokemon_db.delete_pokemon( pokemon_name,trainer_name)
        
        return {"message": "Pokemon deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server error")



@router.put("/evolve-pokemon")
def evolve_pokemon(pokemon:str,trainer:str, pokemon_db=Depends(get_db)):
    pokemon_id = pokemon_db.get_pokemon_by_name(pokemon)[0][0]
    if not pokemon_id:
        raise HTTPException(status_code=404, detail="No Pokémon found with the given name")
    trainer_id = pokemon_db.get_trainer_by_name(trainer)[0][0]
    if not trainer_id:
        raise HTTPException(status_code=404, detail="No Trainer found with the given name")
    if not pokemon_db.check_trainer_and_pokemon(pokemon_id,trainer_id):
        raise HTTPException(status_code=404, detail="Pokémon is not in trainer hand")
    evolved_pokemon = pokemon_db.get_next_evolve_pokemon_name(pokemon)
    if not evolved_pokemon:
        raise HTTPException(status_code=404, detail="Pokémon has reach max evoloution")
    evolved_pokemon_id = pokemon_db.get_pokemon_by_name(evolved_pokemon)[0][0]
    pokemon_db.delete_pokemon(pokemon,trainer)
    pokemon_evolved = pokemon_db.add_pokemon_to_trainer(evolved_pokemon_id,trainer_id)
    if pokemon_evolved:
        print("Pokemon evolved successfully.")
        return {"message": "Pokemon evolved successfully."}


@router.get("/")
def get_pokemon_with_filtering(trainer_name:Optional[str]=Query(None), pokemon_type: Optional[str] = Query(None), pokemon_db=Depends(get_db)):

    if trainer_name:
        pokemons=pokemon_db.get_pokemon_by_trainer(trainer_name)
        if not pokemons:
            raise HTTPException(status_code=404, detail="No Pokemon found for the given trainer")
        return pokemons

    if pokemon_type:
        pokemons = pokemon_db.get_pokemon_by_type(pokemon_type)
        if not pokemons:
            raise HTTPException(status_code=404, detail="No Pokemon found for the given type")
        return pokemons

    raise HTTPException(status_code=400, detail="At least one search parameter must be provided")
