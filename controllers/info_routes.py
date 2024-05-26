#1.	Get pokemons by type: returns all pokemons with the specific type
#2.	Get pokemons by trainer: get all the pokemons of a given owner
#3.	Get trainers of a pokemon: get all the trainers of a given pokemon
from fastapi import APIRouter

 
#router to students
router = APIRouter(
    prefix = '/info',
    tags = ['This is all informative requests to the server ']
    
)

@router.get("/get-by-type")
def get_by_type() ->list:
    pass


@router.get("/get-by-trainer")
def get_by_trainer()-> list:
    pass


@router.get("/get-pokemon-trainer")
def get_pokemon_trainer()-> list:
    pass