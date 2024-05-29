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


@router.delete("/delete-pokemon")
def delete_pokemon():
    pass


@router.put("/evolve-pokemon")
def evolve_pokemon():
    # there is need for check if the evolotion can happen
    pass


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
