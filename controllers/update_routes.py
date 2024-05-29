#1.Add new pokemon species: adds a new pokemon species with the following 
#2.	delete pokemon of trainer
#3.	add pokemon to a trainer: when a trainer catches a pokemon and train it the pokemon become his.
#4.	Evolve (pokemon x of trainer y)
from fastapi import APIRouter
from models import mysql_database
pokemon_db = Mysql_database()

#router to students
router = APIRouter(
    prefix = '/update',
    tags = ['This is all update requests to the server ']
)
    


@router.post("/create-pokemon")
def create_pokemon():
    pass


@router.delete("/trainer/{trainer_name}/pokemon/{pokemon_name}", status_code=204)
def delete_pokemon_from_trainer(trainer_name: str, pokemon_name: str):
    try:
        delete_pokemon(trainer_name, pokemon_name)
        return {"message": "Pokemon deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HITPException(status_code=500, detail="Server error")


@router.post("/add-pokemon-to-trainer")
def add_pokemon_to_trainer():
    pass


@router.put("/evolve-pokemon")
def evolve_pokemon():
    #there is need for check if the evolotion can happen
    pass