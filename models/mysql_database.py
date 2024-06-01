import requests
from models.database import Database
import mysql.connector

POKEMON_DETAILS_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_db():
    db = Mysql_database()
    return db


class Mysql_database(Database):
    def __init__(self):
        self.config = {
            'user': 'root',
            'password': '',
            'host': 'localhost',
            'port': '3307',
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
    
    def __get_evolve_chain(self, pokemon):
        response = requests.get(POKEMON_DETAILS_URL+pokemon).json()
        species_url = response["species"]["url"]
        response = requests.get(species_url).json()
        evolution_chain = response["evolution_chain"]["url"]
        response = requests.get(evolution_chain).json()
        return response["chain"]
    
    def get_next_evolve_pokemon_name(self, pokemon):
        evolve_chain = self.__get_evolve_chain(pokemon)
        while(evolve_chain["species"]["name"] != pokemon):
                evolve_chain=evolve_chain["evolves_to"][0]
        try:
            result = evolve_chain["evolves_to"][0]["species"]["name"]
        except IndexError:
            return None
        return result

    def add_pokemon(self, data):
        query = f"INSERT INTO pokemons (id, name, height, weight) VALUES ({data[0]},'{data[1]}', {data[2]}, {data[3]});"
        try:

            self.__execute_query(query, commit=True)
            return True
        except Exception as e:
            print(f"Error occurred: {e}")
            return False

    def get_pokemon_by_type(self, type: str):
        query = f"SELECT p.name FROM pokemons p join pokemonstypes pt on  p.id = pt.pokemon_id where pt.type_name = '{type}'"
        pokemons = self.__execute_query(query)
        pokemons = [list(inner_list) for inner_list in pokemons]

        return pokemons

    def get_pokemon_by_name(self, name: str):
        query = f"""SELECT * FROM pokemons WHERE name = '{name}'"""
        return self.__execute_query(query)
    
    def get_trainer_by_name(self, name: str):
        query = f"""SELECT * FROM trainers WHERE name = '{name}'"""
        return self.__execute_query(query)


    def get_pokemon_by_id(self, id: int):
        query = f"""SELECT * FROM pokemons WHERE id = '{id}'"""
        return self.__execute_query(query)

    def add_pokemonsTypes(self, pokemon_id: int, types: list):
        for type in types:
            query = f"""INSERT INTO pokemonsTypes (type_name, pokemon_id) VALUES ('{type}', {pokemon_id})"""
            self.__execute_query(query, commit=True)
        return True

    def add_type_to_typesTable(self, type: str):
        query = f"""INSERT INTO types (name) VALUES ('{type}')"""
        self.__execute_query(query, commit=True)
        return True

    def add_trainer_to_TrainerTable(self, name: str, town: str):
        query = f"""INSERT INTO trainers (name,town) VALUES ('{name}','{town}')"""
        self.__execute_query(query, commit=True)
        return True

    def get_all_trainers(self):
        query = "SELECT * FROM trainers "

        return self.__execute_query(query)

    def get_pokemon_by_trainer(self, trainer: str):
        query = f"""
        SELECT p.name
        FROM pokemons p
        JOIN team ON p.id = team.pokemon_id
        JOIN trainers t ON t.id = team.trainer_id
        WHERE t.name = '{trainer}';
        """
        pokemons=self.__execute_query(query)
        pokemons = [list(inner_list) for inner_list in pokemons]
        return pokemons

    def get_trainers_of_pokemon(self, pokemon: str):
        query = f"SELECT t.name FROM trainers t join team on  t.id = team.trainer_id join pokemons p on p.id = team.pokemon_id  where p.name = '{pokemon}'"
        self.__execute_query(query)

    def check_trainer_and_pokemon(self, pokemon_id: int, trainer_id:int):
        query = f"SELECT * from team where trainer_id={trainer_id} and pokemon_id={pokemon_id}"
        if self.__execute_query(query):
            return True
        return False

    def delete_pokemon(self,pokemon_name, trainer_name):
        pokemon_id = self.__execute_query(f"SELECT id FROM pokemons WHERE name = '{pokemon_name}';")[0][0]
        trainer_id = self.__execute_query(f"SELECT id FROM trainers WHERE name = '{trainer_name}';")[0][0]
        query = f"DELETE FROM team WHERE trainer_id = {trainer_id} AND pokemon_id = {pokemon_id};"
        self.__execute_query(query,True)
        


    def add_pokemon_to_trainer(self, pokemon_id, trainer_id):
        query = f"""INSERT INTO team (trainer_id,pokemon_id) VALUES ('{trainer_id}', {pokemon_id})"""
        self.__execute_query(query, commit=True)
        return True