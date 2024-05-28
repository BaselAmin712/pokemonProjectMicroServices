# 1.Add new pokemon species: adds a new pokemon species with the following
# 2.	delete pokemon of trainer
# 3.	add pokemon to a trainer: when a trainer catches a pokemon and train it the pokemon become his.
# 4.	Evolve (pokemon x of trainer y)
from fastapi import APIRouter, HTTPException

# router to students
from models.mysql_database import Mysql_database
from models.schema import Pokemon

router = APIRouter(
    prefix='/update',
    tags=['This is all update requests to the server ']
)
pokemon_db = Mysql_database()


@router.post("/create-pokemon")
def create_pokemon(pokemon: Pokemon):
    existing_pokemon = pokemon_db.get_pokemon_by_id(pokemon.id)
    if existing_pokemon:
        raise HTTPException(status_code=404, detail="Pokémon found with the given id")
    existing_pokemon = pokemon_db.get_pokemon_by_name(pokemon.name)
    if existing_pokemon:
        print("Pokemon with the same name already exists.")
        return {"error": "Pokemon with the same name already exists."}

    pokemon_data = [pokemon.id, pokemon.name, pokemon.height, pokemon.weight]
    pokemon_added = pokemon_db.add_pokemon(pokemon_data)

    for type in pokemon.types:
        pokemon_db.add_pokemonsTypes(pokemon.id,type)

    if pokemon_added:
        print("Pokemon added successfully.")
        return {"message": "Pokemon added successfully."}


@router.delete("/delete-pokemon")
def delete_pokemon():
    pass


@router.post("/add-pokemon-to-trainer")
def add_pokemon_to_trainer():
    pass


@router.put("/evolve-pokemon")
def evolve_pokemon():
    # there is need for check if the evolotion can happen
    pass
