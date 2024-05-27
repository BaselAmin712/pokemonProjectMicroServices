import json
import threading
import requests

def correct_pokemon_data(pokemon,memo):
    """

    :param pokemon:
    :param memo:
    :return:
    """
    name = pokemon["name"]
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url).json()
    tmp=[]
    for type in response["types"]:
        tmp.append(type["type"]["name"])
    pokemon["type"]=tmp
    memo.append(pokemon)



def read_json():
    with open("../Db_Json/pokemons_data (1).json", 'r') as file:
        data = json.load(file)
    return data
def write_to_json(data):
    with open("../Db_Json/pokemons_data (1).json", 'w') as file:
        json.dump(data, file)


def create_threads_for_updating_json():
    json_db=read_json()
    memo=[]
    threads=[]
    for pokemon in json_db:
        thread = threading.Thread(target=correct_pokemon_data, args=(pokemon, memo))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

    write_to_json(json_db)
    return json_db
json_db=create_threads_for_updating_json()

