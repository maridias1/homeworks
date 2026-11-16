import json
import os

chess_players = [
    {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
    {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
    {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
    {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
    {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
    {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
    {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
    {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
    {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

new_players = [
    {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
    {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]

file_name = "players.json"


1.
def get_file_path(filename):
    with open(filename, "w") as f:
        pass
    full_path = os.path.abspath(filename)
    return full_path


with open(file_name, "w") as file:
    json.dump(chess_players, file)


2.
def read_file_content(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data


3.
def add_to_file(filename, new_player_dict):
    with open(filename, "r") as file:
        current_data = json.load(file)
    
    current_data.append(new_player_dict)
        
    with open(filename, "w") as file:
        json.dump(current_data, file)


4.
def update_file_content(filename, updated_data):
    with open(filename, "w") as file:
        json.dump(updated_data, file)
