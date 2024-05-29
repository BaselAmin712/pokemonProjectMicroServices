from unittest.mock import patch

from fastapi.testclient import TestClient

from models.mysql_database import Mysql_database
from server import server
from models import mysql_database

client = TestClient(server)


def test_getPokemon_bad_id():
    response = client.get("pokemons/pokemon/11111111")
    assert response.status_code == 404


def test_pokemon_id_found():
    response = client.get("pokemons/pokemon/15")
    assert response.status_code == 200
    assert response.json() == [15, "beedrill", 10, 295]


###########################################################################


def test_pokemon_type_found():
    db = Mysql_database()
    pokemons = db.get_pokemon_by_type("bug")
    response = client.get("/pokemons/?pokemon_type=bug")

    assert response.status_code == 200
    assert response.json() == pokemons

def test_pokemon_trainer_found():
    db = Mysql_database()
    pokemons = db.get_pokemon_by_trainer("Ash")
    response = client.get("/pokemons/?trainer_name=Ash")

    assert response.status_code == 200
    assert response.json() == pokemons