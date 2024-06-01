from unittest.mock import patch

from fastapi.testclient import TestClient

from models.mysql_database import Mysql_database
from server import server
from models import mysql_database

client = TestClient(server)

def test_cant_evolve():
    response = client.put("pokemons/evolve-pokemon?pokemon=pinsir&trainer=Diantha")
    assert response.status_code == 403

def test_evolve_is_not_in_trainer_hand():
    response = client.put("pokemons/evolve-pokemon?pokemon=spearow&trainer=Archie")
    assert response.status_code == 400

def test_true_evolve():
    response = client.put("pokemons/evolve-pokemon?pokemon=oddish&trainer=Whitney")
    assert response.status_code == 200

def test_check_after_true_evolve():
    response = client.put("pokemons/evolve-pokemon?pokemon=oddish&trainer=Whitney")
    assert response.status_code == 400
    
def test_check_after_evolve_there_is_evolved():
    response = client.get("pokemons/?trainer_name=Whitney").json()

    assert any('gloom' in sublist for sublist in response), "Value 'gloom' not found in returned array"
