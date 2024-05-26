#1.Add new pokemon species: adds a new pokemon species with the following 
#2.	delete pokemon of trainer
#3.	add pokemon to a trainer: when a trainer catches a pokemon and train it the pokemon become his.
#4.	Evolve (pokemon x of trainer y)
from fastapi import APIRouter

 
#router to students
router = APIRouter(
    prefix = '/update',
    tags = ['This is all update requests to the server ']
)
    


@router.post("/create-pokemon")
def create_pokemon():
    pass


@router.delete("/delete-pokemon")
def delete_pokemon():
    pass


@router.post("/add-pokemon-to-trainer")
def add_pokemon_to_trainer():
    pass


@router.put("/evolve-pokemon")
def evolve_pokemon():
    #there is need for check if the evolotion can happen
    pass