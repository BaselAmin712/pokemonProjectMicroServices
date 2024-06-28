# 1.	Get trainers of a pokemon: get all the trainers of a given pokemon
from fastapi import APIRouter, HTTPException, Depends
from models.mysql_database import Mysql_database, get_db

router = APIRouter(
    prefix='/trainers',
    tags=['This is all  requests for trainers resources ']
)


@router.get("/{pokemon_name}")
def get_pokemon_trainer(pokemon_name:str,pokemon_db=Depends(get_db))-> list:
    """
    Retrieves a list of trainers who own a Pokemon with the given name.
    :param pokemon_name: the name of the pokemon to search for.
    :param pokemon_db: Dependency to fetch the db
    :return: A list of trainers who own pokemon
    """
    trainers=pokemon_db.get_trainers_of_pokemon(pokemon_name)
    print(pokemon_name)
    print(trainers)
    if not trainers:
        raise HTTPException(status_code=404, detail="No pokemon found with the given name")
    return trainers



# @router.post("/{trainer_id}/pokemons")
# def add_pokemon_to_trainer(trainer_id: int, pokemon_id: int,pokemon_db=Depends(get_db)):
#     """

#     :param trainer_id: the id of trainer who will own the pokemon
#     :param pokemon_id: the Id of pokemon to be added
#     :param pokemon_db: Dependency to fetch the db
#     :return: None
#     """
#     pokemon=pokemon_db.get_pokemon_by_id(pokemon_id)
#     if not pokemon:
#         raise HTTPException(status_code=404, detail="No pokemon found with the given id")
#     trainer=pokemon_db.get_trainer_by_id(trainer_id)
#     if not trainer:
#         raise HTTPException(status_code=404, detail="No trainer found with the given id")
#     pokemon_db.add_pokemon_to_trainer(trainer_id,pokemon_id)


@router.put("/add-pokemon/{pokemon_id}/-to-trainer/{trainer_id}")
def add_pokemon_to_trainer(pokemon_id: int, trainer_id: int, pokemon_db=Depends(get_db)):
    """
    :param trainer_id: the id of trainer who will own the pokemon
    :param pokemon_id: the Id of pokemon to be added
    :param pokemon_db: Dependency to fetch the db
    :return: None
    """
    pokemons = pokemon_db.get_pokemon_by_id(pokemon_id)
    if not pokemons:
        raise HTTPException(status_code=404, detail="No Pokémon found with the given ID")
    trainer = pokemon_db.get_trainer_by_id(pokemon_id)
    if not trainer:
        raise HTTPException(status_code=404, detail="No trainer found with the given ID")
    if not pokemon_db.check_trainer_and_pokemon(pokemon_id,trainer_id):
        raise HTTPException(status_code=400, detail="Pokémon is not in trainer hand")
    if pokemon_db.add_pokemon_to_trainer(pokemon_id, trainer_id):
        print("Pokemon added successfully to trainer.")
        return {"message": "Pokemon added successfully to trainer."}
