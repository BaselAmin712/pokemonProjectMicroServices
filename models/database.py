from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def config_db(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def add_pokemon(self,pokemon):
        pass

    @abstractmethod
    def get_pokemon_by_type(self,type):
        pass

    @abstractmethod
    def get_pokemon_by_trainer(self,trainer):
        pass

    @abstractmethod
    def get_trainers_of_pokemon(self,pokemon):
        pass

    @abstractmethod
    def delete_pokemon(self,pokemon):
        pass

    @abstractmethod
    def add_pokemon_to_trainer(self, pokemon, trainer):
        pass

    @abstractmethod
    def evolve(self, pokemon):
        pass