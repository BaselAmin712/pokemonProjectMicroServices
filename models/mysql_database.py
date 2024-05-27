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





    def config_db(self):
        pass

    def connetion(self):
        pass

    def add_pokemon(self,data):
        pass

    def get_pokemon_by_type(self,type):
        pass

    def get_pokemon_by_trainer(self,trainer):
        pass

    def get_trainers_of_pokemon(self,pokemon):
        pass

    def delete_pokemon(self,pokemon):
        pass

    def add_pokemon_to_trainer(self, pokemon, trainer):
        pass

    def evolve(self, pokemon):
        pass