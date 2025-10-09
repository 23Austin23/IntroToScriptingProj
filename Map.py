from Spot import *
from Tainer import *
from QA import *
from Item import *
import random
import math

class Map:
    def __init__(self):
        self.map = self.generate_map()

    def __getitem__(self, item):
        return self.map[item]


    def generate_map(self):
        self.map = []
        item = []
        for i in range(1, 6):
            self.map.append(item)
        return self.map

    def random_item_list(self):
        return_list = []
        while len(return_list) < 7:
            rand_num = random.randint(0, 14)
            if rand_num in return_list or rand_num == 9:
                continue
            else:
                return_list.append(rand_num)
        return return_list

    def random_items_list2(self):
        return_this = []
        while True:
            rand_num = random.randint(0, len(ITEMS) - 1)
            if len(return_this) == len(ITEMS):
                break
            if ITEMS[rand_num] in return_this:
                continue
            else:
                return_this.append(ITEMS[rand_num])
        return return_this


    def place_spots(self):
        spots = [[Spot(), Spot(), Spot()],[Spot(), Spot(), Spot()],[Spot(), Spot(), Spot()],[Spot(), Spot(), Spot()],[Spot(), Spot(), Spot()]]
        self.map = spots

    def place_items(self):
        spot_list = self.random_item_list()
        item_name_list = self.random_items_list2()
        for item in spot_list:
            row = item / 3
            col = item % 3
            spot = self.map[int(row)][col]
            spot.update_item(Item(item_name_list[0]))
            item_name_list.remove(item_name_list[0])

    def place_player(self):
        name = str(input('Please enter your name (10 Character Limit): '))
        name = name.replace(' ', '')
        while len(name) > 10:
            print('I am sorry, you have entered a name that is too long! Please try again.')
            name = str(input('Please enter your name (10 Character Limit): '))
            name = name.replace(' ', '')
        self.map[2][1].update_person(Tainer(name))

    def generate_name(self):
        names = ['Scott', 'Jacob', 'Daniel', 'Hoffstetter', 'Gary']
        random_num = random.randint(0, len(names) - 1)
        return names[random_num]

    def player_locations_spots(self):
        return_this = []
        return_this2 = []
        for item in self.map:
            for item2 in item:
                person = item2.return_person()
                if item2.is_player() or item2.is_qa():
                    return_this.append(person.get_loc())
                else:
                    continue
        for location in return_this:
            row, col = int(location[0]), int(ord(location[1])) - 88
            return_this2.append((row, col))
        return return_this2

    def player_locations_chr(self):
        return_this = []
        return_this2 = []
        for item in self.map:
            for item2 in item:
                if item2.is_player() or item2.is_qa():
                    return_this.append(item2.return_person().get_loc())
        for location in return_this:
            row, col = int(location[0]), int(ord(location[1])) - 88
            return_this2.append((row, col))
        return return_this2

    def place_qa(self, name):
        #do_not_place = self.player_locations_spots()
        while True:
            random_num = random.randint(0, 14)
            if random_num != 7:
                row = random_num // 3
                col = random_num % 3
                #print(f'QA added at row {row}, col {chr(col + 88)}')
                self.map[row][col].update_person(QA(name))
                self.map[row][col].return_person().set_loc(row, col)
                break

    def place_new_qa(self, name):
        do_not_place = self.player_locations_spots()
        new_list = []
        for item in do_not_place:
            row = item[0]
            col = item[1]
            new_list.append((row * 3) + col)
        do_not_place = new_list
        #print(f'do_not_place in place new qa: {do_not_place}')
        while True:
            random_num = random.randint(0, 14)
            if random_num not in do_not_place:
                row = random_num // 3
                col = random_num % 3
                # print(f'QA added at row {row}, col {chr(col + 88)}')
                self.map[row][col].update_person(QA(name))
                self.map[row][col].return_person().set_loc(row, col)
                break

    def get_qa_positions(self):
        list_of_qa_positions = []
        for line in self.map:
            for spot in line:
                if spot.is_qa():
                    loc = spot.return_person().get_loc()
                    row, col = int(loc[0]), int(ord(loc[1])) - 88
                    list_of_qa_positions.append((row, col))
                    #print(f'added qa position {row} {col} to list of qa')
        return list_of_qa_positions

    def move_qa(self, list_qa, moves, i):
        #print("we're moving!")
       # print(f'list_of_qa_positions: {list_qa}')
        random_num = random.randint(0, len(moves) - 1)
        row = moves[random_num][0]
        col = moves[random_num][1]
        prev_location = self.map[list_qa[i][0]][list_qa[i][1]].return_person().get_loc()
        #print(f'prev_location: {prev_location}')
        #print(f'removing qa from prev_location: {prev_location[0]} {ord(prev_location[1]) - 88}')
        self.map[row][col].update_person(self.map[int(prev_location[0])][ord(prev_location[1]) - 88].return_person())
        self.map[int(prev_location[0])][ord(prev_location[1]) - 88].remove_person()
        #print(f'moved to {row}, {col}')
        self.map[row][col].return_person().set_loc(row, col)
        list_qa = self.get_qa_positions()
        return list_qa

    def qa_movement(self):
        #print('starting qa movement')
        list_of_qa_positions = self.get_qa_positions()
        do_not_place = self.player_locations_chr()
        #print(f'list_of_qa_positions: {list_of_qa_positions} do_not_place: {do_not_place}')
        #print(f'list_of_qa_positions: {list_of_qa_positions} do_not_place: {do_not_place}')
        #get qa moves, remove from do not place
        for i in range(0, len(list_of_qa_positions) - 1):
            moves = self.map[list_of_qa_positions[i][0]][list_of_qa_positions[i][1]].get_pos_moves()
            #print(moves)
            for move in moves:
                #print(f'move in do_not_place: {move} {do_not_place} {move in do_not_place}')
                if move in do_not_place:
                    moves.remove(move)
                    continue
            #print(f'new moves: {moves}')
            random_num = random.randint(0, 10)
            #print(f'random number {random_num}')
            if random_num > 2:
                list_of_qa_positions = self.move_qa(list_of_qa_positions, moves, i)



    def map_start(self):
        self.place_spots()
        self.place_items()
        self.place_player()
        self.place_qa(self.generate_name())

    def move_person(self, prev_location, row, col):
        self.map[int(prev_location[0])][ord(prev_location[1]) - 88].return_person().set_loc(row, col)
        self.map[row][col].update_person(self.map[int(prev_location[0])][ord(prev_location[1]) - 88].return_person())
        self.map[int(prev_location[0])][ord(prev_location[1]) - 88].remove_person()

    def meet_villain(self, move):
        row, col = [int(move[0]), (ord(move[1]) - 88)]
        person = self.map[row][col].is_qa()
        return person

    def print_spaces(self, name, width):
        print(' ' * math.floor((width - len(name)) / 2), end='')
        print(f'{name}', end='')
        print(' ' * math.ceil((width - len(name)) / 2), end='')
        print('*', end='')

    def row_has_player(self, row):
        map_row = self.map[row]
        for item in map_row:
            if item.is_player():
                return True
        return False

    def row_has_qa(self, row):
        map_row = self.map[row]
        for item in map_row:
            if item.is_qa():
                return True
        return False

    def tools_remaining(self):
        counter = 0
        for row in self.map:
            for spot in row:
                if spot.return_has_item():
                    counter += 1
        return counter

    def print_map(self, move_count):
        row = 0
        width = 16
        move = f'Move Counter: {move_count}'
        tool = f'Tools Found: {7 - self.tools_remaining()}'
        print(f'Move Counter: {move_count}' + (' ' * (52 - (len(move) + len(tool)))) + f'Tools Found: {7 - self.tools_remaining()}')
        while row <= 4:
            print('****************************************************')
            #print(f'row has person: {self.row_has_person(row)}')
            if self.row_has_player(row) and self.row_has_qa(row):
                print('*', end='')
                for i in range(0, 3):
                    name = self.map[row][i].return_person().get_name() if self.map[row][i].is_player() else ' '
                    self.print_spaces(name, width)
                print('')
                print('*', end='')
                for i2 in range(0, 3):
                    name = self.map[row][i2].return_person().get_name() if self.map[row][i2].is_qa() else ' '
                    # print('*', end='')
                    self.print_spaces(name, width)
            elif not self.row_has_qa(row) and not self.row_has_player(row):
                print(('*' + ' ' * 16) * 3, end='*' )
            elif self.row_has_player(row) and not self.row_has_qa(row):
                print('*', end='')
                for i in range(0, 3):
                    name = self.map[row][i].return_person().get_name() if self.map[row][i].is_player() else ' '
                    self.print_spaces(name, width)
            elif self.row_has_qa(row) and not self.row_has_player(row):
                if not self.row_has_player(row):
                    print('*', end='')
                for i2 in range(0, 3):
                    name = self.map[row][i2].return_person().get_name() if self.map[row][i2].is_qa() else ' '
                    #print('*', end='')
                    self.print_spaces(name, width)
            print('')
            print(f'*       {str(row + 1) + "X"}       *       {str(row + 1) + "Y"}       *       {str(row + 1) + "Z"}       *')
            print('*', end='')
            for i3 in range(0, 3):
                name = '?' if self.map[row][i3].return_has_item() else ' '
                print(' ' * 7, end='')
                print(f'{name}', end='')
                print(' ' * 8, end='')
                print('*', end='')

            print('')
            row += 1
        print('****************************************************')
