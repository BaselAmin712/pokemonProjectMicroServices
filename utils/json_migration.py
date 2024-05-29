import sys
import os
# Remove these two lines after finishing the development of thid module
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from models import mysql_database
from models.mysql_database import get_db
from utils.json_handler import read_json

mySql = mysql_database.Mysql_database()
cursor = mySql.connetion.cursor()

json_db = read_json()
sql_db=get_db()
""" Pokemons"""
for pokemon in json_db:
    pokemon_data = [pokemon["id"], pokemon["name"], pokemon["height"], pokemon["weight"]]
    pokemon_added = sql_db.add_pokemon(pokemon_data)

""" types"""

types=[]
for pokemon in json_db:
    for t in pokemon["type"]:

        if t not in types:
            sql_db.add_type_to_typesTable(t)
            types.append(t)
    mySql.add_pokemonsTypes(pokemon["id"], pokemon["type"])



names_owners=[]
for pokemon in json_db:
    for owner in pokemon["ownedBy"]:
        if owner["name"]not  in names_owners:
            sql_db.add_trainer_to_TrainerTable(owner["name"],owner["town"])
            names_owners.append(owner["name"])





dict_trainer={}
sql_select_trainers =mySql.get_all_trainers()
for row in sql_select_trainers:
    dict_trainer[row[1]]=row[0]

for pokemon in json_db:
    for trainer in pokemon["ownedBy"]:
        sql_insert_query = """
        INSERT INTO team (trainer_id,pokemon_id)
        VALUES (%s,%s);
        """
        cursor.execute(sql_insert_query, (dict_trainer[trainer["name"]],pokemon["id"]))

mySql.connetion.commit()


cursor.close()
mySql.connetion.close()
