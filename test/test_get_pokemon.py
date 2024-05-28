from unittest.mock import patch

from fastapi.testclient import TestClient

from models.mysql_database import Mysql_database
from server import server
from models import mysql_database

client = TestClient(server)


def test_getPokemon_bad_id():
    response = client.get("/pokemons/?pokemon_id=99999999")
    assert response.status_code == 404


def test_getPokemon_bad_name():
    response = client.get("/pokemons/?pokemon_name=aaaaaaa")
    assert response.status_code == 404


def test_getPokemon_bad_type():
    response = client.get("/pokemons/?pokemon_type=aaaaaaa")
    assert response.status_code == 404


def test_getPokemon_no_params():
    response = client.get("/pokemons/")
    assert response.status_code == 400


###########################################################################


def test_pokemon_id_found():
    response = client.get("/pokemons/?pokemon_id=1")
    assert response.status_code == 200
    assert response.json() == [1, "bulbasaur", 7, 69]


def test_pokemon_name_found():
    response = client.get("/pokemons/?pokemon_name=bulbasaur")
    assert response.status_code == 200
    assert response.json() == [1, "bulbasaur", 7, 69]


def test_pokemon_type_found():
    db=Mysql_database()
    pokemons=db.get_pokemon_by_type("bug")
    response = client.get("/pokemons/?pokemon_type=bug")

    assert response.status_code == 200
    assert response.json()==pokemons
