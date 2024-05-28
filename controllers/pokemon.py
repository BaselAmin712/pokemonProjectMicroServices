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

# @router.get("/pokemon/type/{type_name}")
# def get_by_type(type_name: str) ->list:
#     pokemons = pokemon_db.get_pokemon_by_type(type_name)
#     if not pokemons:
#         raise HTTPException(status_code=404, detail="No Pokémon found for the given type")
#     return pokemons
#
# @router.get("/pokemon/name/{name}")
# def get_by_name(name: str):
#     pokemons = pokemon_db.get_pokemon_by_name(name)
#     if not pokemons:
#         raise HTTPException(status_code=404, detail="No Pokémon found with the given name")
#     return pokemons[0]
#
# @router.get("/pokemon/{id}")
# def get_by_id(id: str):
#     pokemons = pokemon_db.get_pokemon_by_id(id)
#     if not pokemons:
#         raise HTTPException(status_code=404, detail="No Pokemon found with the given id")
#     return pokemons[0]

@router.post("/")
def create_pokemon(pokemon: Pokemon,pokemon_db=Depends(get_db)):
    existing_pokemon = pokemon_db.get_pokemon_by_id(pokemon.id)
    if existing_pokemon:
        raise HTTPException(status_code=409, detail="Pokemon found with the given id")
    existing_pokemon = pokemon_db.get_pokemon_by_name(pokemon.name)
    if existing_pokemon:
        raise HTTPException(status_code=409, detail="Pokemon found with the given name")

    pokemon_data = [pokemon.id, pokemon.name, pokemon.height, pokemon.weight]
    pokemon_added = pokemon_db.add_pokemon(pokemon_data)
    pokemon_db.add_pokemonsTypes(pokemon.id,pokemon.types)

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
def get_pokemon(pokemon_id: Optional[int] = Query(None,description="ID of Pokemon"),pokemon_name: Optional[str] = Query(None,description="Name of Pokemon")
                ,pokemon_type:Optional[str]=Query(None),pokemon_db=Depends(get_db)):


    if pokemon_id:
        pokemons = pokemon_db.get_pokemon_by_id(pokemon_id)
        if not pokemons:
            raise HTTPException(status_code=404, detail="No Pokemon found with the given id")
        return pokemons[0] ## Return the first Pokemon in the list // There are no more Pokemon in the result.

    if pokemon_name:
        pokemons = pokemon_db.get_pokemon_by_name(pokemon_name)
        if not pokemons:
            raise HTTPException(status_code=404, detail="No Pokemon found with the given name")
        return pokemons[0]

    if pokemon_type:
        pokemons = pokemon_db.get_pokemon_by_type(pokemon_type)
        if not pokemons:
            raise HTTPException(status_code=404, detail="No Pokemon found for the given type")
        return pokemons

    raise HTTPException(status_code=400, detail="At least one search parameter must be provided")

