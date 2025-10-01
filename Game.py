from Map import *
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

def get_move():
    allowed_numbers = ['1', '2', '3', '4', '5']
    allowed_chars = ['X', 'Y', 'Z']
    while True:
        move = str(input('Please Enter your move: ')).upper()
        if move[0] not in allowed_numbers:
            print('Please enter a valid move')
        elif move[1] not in allowed_chars:
            print('Please enter a valid move')
        else:
            break
    new_beginning = move[0]
    new_beginning = str(int(new_beginning) - 1)
    return new_beginning + move[1]

def get_moves(possible_moves):
    allowed_numbers = []
    allowed_chars = []
    for item in possible_moves:
        if item[0].upper() not in allowed_numbers:
            allowed_numbers.append(item[0].upper())
        if item[1].upper() not in allowed_chars:
            allowed_chars.append(item[1].upper())
    while True:
        move = str(input('Please Enter your move: ')).upper()
        if move[0] not in allowed_numbers:
            print('Please enter a valid move')
        elif move[1] not in allowed_chars:
            print('Please enter a valid move')
        else:
            break
    return move

def present_possible_moves(map, prev_location):
    person = map[int(prev_location[0])][ord(prev_location[1]) - 88].return_person()
    possible_moves = person.get_pos_moves()
    pos_moves_list = []
    #print('Possible moves:')
    for item in possible_moves:
        new_string = str(int(item[0]) + 1) + str(chr(item[1] + 88)).upper()
        pos_moves_list.append(new_string)
    #pos_moves_list = map.check_qa(pos_moves_list)
    pos_moves_list.sort()
    for string in pos_moves_list:
        print(f'{string} ', end = '')
    print('\n')

def move_player(move, map, prev_location):
    row, col = [int(move[0]), (ord(move[1]) - 88)]
    map.move_person(prev_location, row, col)
    prev_location = str(row) + chr(col + 88)
    return prev_location

def add_qa(map, move_count, qa_count):
    if move_count % 4 == 0 and qa_count < 3:
        map.place_new_qa(map.generate_name())
        qa_count += 1
        print(f'QA added! QA count: {qa_count}')

def main():
    move_count = 0
    qa_count = 1
    prev_location = ['', '']
    map = Map()
    map.map_start()#Map has been generated
    print(INTRO + '\n\n' + INSTRUCTIONS)
    print('Possible Actions:')
    prev_location = "2Y"
    while True:
        present_possible_moves(map, prev_location)
        move = get_move()
        #print(f'Your move was: {move}')
        prev_location = move_player(move, map, prev_location)
        move_count += 1
        add_qa(map, move_count, qa_count)
        map.print_map()





if __name__ == '__main__':
    main()

