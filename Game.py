from Map import *
import time
INTRO = """Welcome to The Flightline! This is a Text Based Game that will test your ability to evade
and collect your lost tools before encountering your roaming QA representative. You must 
collect 7 different tools before encountering QA or else you will receive paperwork the 
game will reset from the beginning.\n\n"""

INSTRUCTIONS = """You will have two choices for actions:
1) Move your character from location to location.
2) Collect a tool that is at the location you are on.
You will be informed of the location of QA if they are neighboring your location.
The Game will begin with 1 QA member sharing the map with you, but as you move around
additional QA members will appear around the map. Be careful! You can be surrounded and 
forced to lose the game if you do not plan accordingly!

Good Luck!"""

ENDGAME1 = "Hello!"
ENDGAME2 = "Do you mind if I check your Tool Box real quick?"
MAP_TEXT = """Above is your game map! You can see that your player name is on the starting position.
It will move as you move your player. You will also see a number of names other than yours.
These are QA Members. DO NOT encounter them without intending to do so!"""
#ENDGAME3 = f"Uh oh, looks like you are missing {7 - num_items} tools. This will have to be written up."

def get_move(possible_moves):
    allowed_moves = []
    for item in possible_moves:
        new_item = str(item[0] + 1) + chr(item[1] + 88)
        allowed_moves.append(new_item)
    #print(f'allowed_moves: {allowed_moves}')
    move = str(input('\nPlease Enter Your Move: ')).upper()
    move = move.replace(' ', '')
    #print(f'move: "{move}"')
    #print(f'move no space: "{move}"')
    if move == 'secure' or move == 'SECURE':
        return -1
    else:
        while True:
            #print(f'move in allowable moves: {move in allowed_moves}')
            if len(move) == 0:
                #print(f'Please enter a valid move: {allowed_moves}')
                return get_move(possible_moves)
            elif move not in allowed_moves:
                print(f'Please enter a valid move: {allowed_moves}')
                return get_move(possible_moves)
            else:
                break
        new_beginning = move[0]
        new_beginning = str(int(new_beginning) - 1)
        return new_beginning + move[1]

def present_possible_moves(map, prev_location):
    row, col = int(prev_location[0]), ord(prev_location[1]) - 88
    person = map[row][col].return_person()
    possible_moves = person.get_pos_moves()
    pos_moves_list = []
    spot_has_item = map[row][col].return_has_item()
    print('Possible moves:')
    for item in possible_moves:
        new_string = str(int(item[0]) + 1) + str(chr(item[1] + 88)).upper()
        pos_moves_list.append(new_string)
    #pos_moves_list = map.check_qa(pos_moves_list)
    pos_moves_list.sort()
    for string in pos_moves_list:
        print(f'{string} ', end = '')
    if spot_has_item:
        pos_moves_list.append(map[row][col].return_item_name())
        print(f'*Secure Tool*')
        print(f'This spot has a tool: {map[row][col].return_item_name()}. To secure this tool, input "secure".', end='')

def move_player(move, map, prev_location):
    row, col = [int(move[0]), (ord(move[1]) - 88)]
    map.move_person(prev_location, row, col)
    prev_location = str(row) + chr(col + 88)
    return prev_location

def add_qa(map, move_count, qa_count):
    if move_count == 0:
        pass
    elif move_count % 4 == 0 and qa_count < 3:
        map.place_new_qa(map.generate_name())
        qa_count += 1
        print(f'QA added! QA count: {qa_count}')

def end_game_speech(move, map, prev_location):
    row, col = [int(move[0]), (ord(move[1]) - 88)]
    qa_person = map[row][col].return_person()
    name = qa_person.get_name()
    print(f'You have encountered {name}, they approach you!')
    print(ENDGAME1 + ' ' + ENDGAME2)
    print("...")
    time.sleep(3)
    print("...")
    time.sleep(3)
    row, col = [int(prev_location[0]), (ord(prev_location[1]) - 88)]
    items = map[row][col].return_person().return_items()
    if len(items) < 7:
        print(f"Uh oh, looks like you are missing {7 - len(items)} tools. This will have to be written up.")
        print("******************\n*    Game Over   *\n*    You Lose    *\n******************", end="\n\n\n")
    else:
        print(f"Well, it looks like you have all of your tools accounted for! You passed this inspection.")
        print("******************\n*    Game Over   *\n*    You Won!    *\n******************",end="\n\n\n")
    time.sleep(2)
    continue_game = str(input("Do you want to play again? (Y/N): ")).upper()
    while continue_game[0] != 'Y' or continue_game[0] != 'N':
        continue_game = str(input("Invalid Input, Please Enter 'Y' or 'N'. \n Do you want to play again? (Y/N): ")).upper()
        if continue_game.upper() == 'Y' or continue_game.upper() == 'N':
            break
    return continue_game[0]

def tool_secured(map, move_count, prev_location, qa_count):
    row, col = int(prev_location[0]), ord(prev_location[1]) - 88
    item = map[row][col].return_item()
    if item is None:
        print('Your input was invalid, please try again.')
    else:
        map[row][col].return_person().secure_item(item.return_name())
        map[row][col].remove_item()
        print(f'You have secured a tool! {item.return_name()} has been secured!')
        time.sleep(5)
        map.qa_movement()
        add_qa(map, move_count, qa_count)
        map.print_map(move_count + 1)

def player_moved(map, move, prev_location, move_count, qa_count):
    encounter = map.meet_villain(move)
    print(f'You have encountered qa: {encounter}.')
    if encounter:
        # get QA name, and print end quote
        continue_game = end_game_speech(move, map, prev_location)
        if continue_game == 'Y':
            main()
        else:
            print('Thank you for playing!')
            return -1
    else:
        prev_location = move_player(move, map, prev_location)
        map.qa_movement()
        add_qa(map, move_count, qa_count)
        map.print_map(move_count + 1)
        return prev_location


def main():
    move_count = 0
    qa_count = 1
    prev_location = ['', '']
    map = Map()
    map.map_start()#Map has been generated
    print(INTRO + '\n\n' + INSTRUCTIONS)
    #time.sleep(10)
    map.print_map(move_count)
    print(MAP_TEXT)
    time.sleep(7)
    #print('Possible Actions:')
    prev_location = "2Y"
    while True:
        present_possible_moves(map, prev_location)
        move = get_move(map[int(prev_location[0])][ord(prev_location[1]) - 88].return_person().get_pos_moves())
        print(f'move_count is {move_count}')
        print(f'move: {move}')
        if move == -1:
            tool_secured(map, move_count, prev_location, qa_count)
            move_count += 1
        if move != -1:
            print(f'moving player: {move}')
            prev_location = player_moved(map, move, prev_location, move_count, qa_count)
            move_count += 1
            if prev_location == -1:
                break





if __name__ == '__main__':
    main()

