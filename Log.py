import datetime
import os

def write_to_log(file, map):
    file = open(file, 'a')
    locations = {
        "items": {
            #item_name and location (tuple)
        },
        "player": {
            #player name and prev_location and new location
        },
        "qa": {
            #qa name and prev location and new location
        }

    }
    row = 0
    for row in map:
        col = 0
        for spot in row:
            item_name = spot.return_has_item()
            location = (row, col)
            if item_name:
                #location = (row, col)
                locations["items"][spot.return_item_name()] = location
            player = spot.is_player()
            if player:
                locations["player"][spot.return_person.get_name()] = location
            qa = spot.is_qa()
            if qa:
                locations["qa"][spot.return_person.get_name()] = location
            col += 1
        row += 1
    file.write(locations)
    file.close()


def create_log_file():
    date = datetime.datetime.today()
    file_name = 'GameLog' + f'{date.year}-{date.month}-{date.day}-{date.hour}-{date.minute}'
    open(os.path.join("\\Logs\\" + file_name), 'w').close()
    return file_name