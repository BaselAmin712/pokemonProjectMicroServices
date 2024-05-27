import requests
from models.database import Database
import mysql.connector


class Mysql_database(Database):
    def __init__(self):
        self.config = {
            'user': 'root',
            'password': '',
            'host': 'localhost',
            'port': '3306',
            'database': 'db_pokemon'
        }

        self.connetion = self.connect()

    def connect(self):
        mydb = mysql.connector.connect(**self.config)
        return mydb

    # private function to execute query to the database
    def __execute_query(self, query, commit=False):
        mydb = self.connect()
        cursor = mydb.cursor()
        cursor.execute(query)
        if commit:
            mydb.commit()
        return cursor.fetchall()

    def add_pokemon(self, data):
        query = f"""INSERT INTO pokemons (id, name, height, weight) VALUES ({data[0]}, {data[1]}, {data[2]}, {data[3]})"""
        try:
            self.__execute_query(query, commit=True)
            return True
        except Exception as e:
            print(f"Error occurred: {e}")
            return False

    def get_pokemon_by_type(self, type: str):
        query = f"SELECT p.name FROM pokemons p join pokemonstypes pt on  p.id = pt.pokemon_id where pt.type_name = '{type}'"
        return self.__execute_query(query)

    def get_pokemon_by_name(self, name: str):
        query = f"""SELECT * FROM pokemons WHERE name = '{name}'"""
        return self.__execute_query(query)

    def get_pokemon_by_id(self, id: int):
        query = f"""SELECT * FROM pokemons WHERE id = '{id}'"""
        return self.__execute_query(query)

    def add_pokemonsTypes(self, pokemon_id: int, type: str):
        type_query = """INSERT INTO pokemonsTypes (type_name, pokemon_id) VALUES (%s, %s)"""
        mydb = self.connect()
        cursor = mydb.cursor()
        cursor.execute(type_query, (type,pokemon_id))
        mydb.commit()






    def get_pokemon_by_trainer(self, trainer: str):
        query = f"SELECT p.name FROM pokemons p join team on  p.id = team.pokemon_id join trainers t on t.id = team.trainer_id where t.name = '{trainer}'"
        self.__execute_query(query)

    def get_trainers_of_pokemon(self, pokemon: str):
        query = f"SELECT t.name FROM trainers t join team on  t.id = team.trainer_id join pokemons p on p.id = team.pokemon_id  where p.name = '{pokemon}'"
        self.__execute_query(query)

    def delete_pokemon(self, pokemon):
        pass

    def add_pokemon_to_trainer(self, pokemon, trainer):
        pass

    # need to continue
    def evolve(self, pokemon):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
        response = requests.get(url).json()
        species_url = response["species"]["url"]
        response = requests.get(species_url).json()
        evolution_chain = response["evolution_chain"]["url"]
        response = requests.get(evolution_chain).json()
        x = response["chain"]

        while (True):
            print(x["species"]["name"])
            if x["species"]["name"] == pokemon:
                print(x["species"]["name"])
                break
            else:
                x = x["evolves_to"][0]
