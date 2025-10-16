import datetime
import os
import json
from Map import *
from Spot import *
from QA import *
from Tainer import *

def write_to_log(file_name, map, prev_location):
    path = os.getcwd() + '/Logs/' + file_name
    file = open(path, 'a')
    locations = {
        "items": {
            #item_name and location (tuple)
        },
        "player": {
            #player name,
            #Player location,
            #player prev_location
        },
        "qa": {
            #qa name,
            #qa location
        }

    }
    for row in range(0, 5):
        for col in range(0, 3):
            spot = map[row][col]
            item_exists = map[row][col].return_has_item()
            location = (row, col)
            if item_exists:
                item_name = spot.return_item_name()
                locations["items"][item_name] = [location]
            player = spot.is_player()
            if player:
                player_name = spot.return_person().get_name()
                locations["player"][player_name] = []
                locations["player"][player_name].append(location)
                locations["player"][player_name].append(prev_location)
            qa = spot.is_qa()
            if qa:
                qa_name = spot.return_person().get_name()
                locations["qa"][qa_name] = []
                locations["qa"][qa_name].append(location)
    json.dump(locations, file)
    file.write("\n")
    file.close()

def read_from_log(file_name):
    path = os.getcwd() + '/Logs/' + file_name
    file = open(path, 'a')
    contents = file.readlines() #maybe json.load?
    for line in contents:
        #parse through file

def create_log_file():
    date = datetime.datetime.today()
    #os.makedirs("\\Logs\\", exist_ok=True)
    file_name = 'GameLog' + f'{date.year}-{date.month}-{date.day}-{date.hour}-{date.minute}.json'
    path = os.getcwd() + '/Logs/' + file_name + '.json'
    open(path, 'w+').close()
    return file_name