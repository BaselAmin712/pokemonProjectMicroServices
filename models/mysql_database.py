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
        self.connetion= self.connect()


    def connect(self):
        mydb = mysql.connector.connect(**self.config)
        return mydb



    #private function to execute query to the database
    def __execute_query(self, query):
        mydb=self.connect()
        cursor = mydb.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    #private function to execute query to the database
    def __execute_query(self, query):
        mydb=self.connect()
        cursor = mydb.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def add_pokemon(self,data):
        pass

    def get_pokemon_by_type(self,type:str):
        query = f"SELECT p.name FROM pokemons p join pokemonstypes pt on  p.id = pt.pokemon_id where pt.type_name = '{type}'"
        self.__execute_query(query)


    def get_pokemon_by_trainer(self,trainer: str):
        query = f"SELECT p.name FROM pokemons p join team on  p.id = team.pokemon_id join trainers t on t.id = team.trainer_id where t.name = '{trainer}'"
        self.__execute_query(query)

    def get_trainers_of_pokemon(self,pokemon:str):
        query = f"SELECT t.name FROM trainers t join team on  t.id = team.trainer_id join pokemons p on p.id = team.pokemon_id  where p.name = '{pokemon}'"
        self.__execute_query(query)

    def delete_pokemon(self,pokemon):
        pass

    def add_pokemon_to_trainer(self, pokemon, trainer):
        pass

    #need to continue
    def evolve(self, pokemon):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
        response = requests.get(url).json()
        species_url = response["species"]["url"]
        response = requests.get(species_url).json()
        evolution_chain = response["evolution_chain"]["url"]
        response = requests.get(evolution_chain).json()
        x=response["chain"]

        while(True):
            print(x["species"]["name"])
            if x["species"]["name"] == pokemon:
                print(x["species"]["name"])
                break
            else : 
                x=x["evolves_to"][0]
    
