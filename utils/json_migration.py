from models import mysql_database
from utils.json_handler import read_json

mySql = mysql_database.Mysql_database()
cursor = mySql.connetion.cursor()

db = read_json()
# """ Pokemons"""
# for pokemon in db:
#     sql_insert_query = """
#     INSERT INTO pokemons (id, name, height, weight)
#     VALUES (%s, %s, %s, %s);
#     """
#     pokemons_data = (pokemon["id"], pokemon["name"], pokemon["height"], pokemon["weight"])
#     cursor.execute(sql_insert_query, pokemons_data)
#
# mySql.connetion.commit()

""" types"""

# types=[]
# for pokemon in db:
#     for t in pokemon["type"]:
#         if t not in types:
#             sql_insert_query = """
#             INSERT INTO types (name)
#             VALUES (%s);
#             """
#             types.append(t)
#             cursor.execute(sql_insert_query, (t,))
#
# mySql.connetion.commit()


# names_owners=[]
# for pokemon in db:
#     for owner in pokemon["ownedBy"]:
#         if owner["name"]not  in names_owners:
#             sql_insert_query = """
#                          INSERT INTO trainers (name,town)
#                          VALUES (%s,%s);
#                          """
#             names_owners.append(owner["name"])
#             cursor.execute(sql_insert_query, (owner["name"], owner["town"]))
# mySql.connetion.commit()



# for pokemon in db:
#     for type in pokemon["type"]:
#         sql_insert_query = """
#         INSERT INTO pokemonstypes (type_name,pokemon_id)
#         VALUES (%s,%s);
#         """
#         cursor.execute(sql_insert_query, (type,pokemon["id"]))
#
# mySql.connetion.commit()

dict_trainer={}
sql_select_trainers = """
        select * from trainers
        """
cursor.execute(sql_select_trainers)

rows = cursor.fetchall()
for row in rows:
    dict_trainer[row[1]]=row[0]

for pokemon in db:
    for trainer in pokemon["ownedBy"]:
        sql_insert_query = """
        INSERT INTO team (trainer_id,pokemon_id)
        VALUES (%s,%s);
        """
        cursor.execute(sql_insert_query, (dict_trainer[trainer["name"]],pokemon["id"]))

mySql.connetion.commit()

cursor.close()
mySql.connetion.close()
