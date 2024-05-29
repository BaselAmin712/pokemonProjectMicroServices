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



    def add_pokemon(self,data):
        pass

    def get_pokemon_by_type(self,type):
        pass

    def get_pokemon_by_trainer(self,trainer):
        pass

    def get_trainers_of_pokemon(self,pokemon):
        pass

    def delete_pokemon(self,pokemon_name, trainer_name):
        my_db = self.connect()
        cursor = my_db.cursor()
        pokemon_id = self.get_pokemon_id_by_name(pokemon_name, cursor)
        trainer_id = self.get_trainer_id_by_name(trainer_name, cursor)
        query = "DELETE FROM team WHERE trainer_id = %s AND pokemon_id = %s;"
        cursor.execute(query, (trainer_id, pokemon_id))

    def get_trainer_id_by_name(self, trainer_name, cursor):
        return cursor.execute("SELECT id FROM trainers WHERE name = '%s';", (trainer_name))

    def get_pokemon_id_by_name(self, pokemon_name, cursor):
        return cursor.execute("SELECT id FROM pokemons WHERE name = '%s';", (pokemon_name))

    def add_pokemon_to_trainer(self, pokemon, trainer):
        pass

    def evolve(self, pokemon):
        pass