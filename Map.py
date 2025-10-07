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

    def return_map(self):
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
            spot = ((row - 1) * 3) + col
            return_this2.append(spot)
        return return_this2

    def player_locations_chr(self):
        return_this = []
        for item in self.map:
            for item2 in item:
                if item2.is_player() or item2.is_qa():
                    return_this.append(item2.return_person().get_loc())
        return return_this

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
        while True:
            random_num = random.randint(0, 14)
            if random_num not in do_not_place:
                row = random_num // 3
                col = random_num % 3
                # print(f'QA added at row {row}, col {chr(col + 88)}')
                self.map[row][col].update_person(QA(name))
                self.map[row][col].return_person().set_loc(row, col)
                break

    def qa_movement(self):
        print('starting qa movement')
        list_of_qa = []
        do_not_place = self.player_locations_chr()
        for row in range(0, 4):
            for col in range(0, 2):
                if self.map[row][col].is_qa():
                    list_of_qa.append(self.map[row][col].return_person())
                    print('added qa to list of qa')
        for qa in list_of_qa:
            moves = qa.get_pos_moves()
            print('got moves for qa')
            for move in moves:
                if move in do_not_place:
                    moves.remove(move)
                    print(f'removed move {move}')
            random_num = random.randint(0, 10)
            print(f'random number {random_num}')
            if random_num > 4:
                print("we're moving!")
                random_num = random.randint(0, len(moves) - 1)
                row = moves[random_num][0]
                col = moves[random_num][1]
                prev_location = qa.get_loc()
                print(f'prev_location: {prev_location}')
                print(f'removing qa from prev_location: {prev_location[0]} {ord(prev_location[1]) - 88}')
                self.map[int(prev_location[0])][ord(prev_location[1]) - 88].remove_person()
                print(f'moved to {row}, {col}')
                self.map[row][col].update_person(qa)
                qa.set_loc(row, col)



    def map_start(self):
        self.place_spots()
        self.place_items()
        self.place_player()
        self.place_qa(self.generate_name())

    def move_person(self, prev_location, row, col):
        self.map[int(prev_location[0])][ord(prev_location[1]) - 88].return_person().set_loc(row, col)
        self.map[row][col].update_person(self.map[int(prev_location[0])][ord(prev_location[1]) - 88].return_person())
        self.map[int(prev_location[0])][ord(prev_location[1]) - 88].remove_person()

    '''def check_qa(self, pos_moves):
        real_moves = []
        for item in pos_moves:
            row, col = int(item[0]), ord(item[1]) - 88
            if self.map[row][col].return_person() is QA:
                continue
            else:
                real_moves.append(item)
        return real_moves'''

    def meet_villain(self, move):
        row, col = [int(move[0]), (ord(move[1]) - 88)]
        person = self.map[row][col].is_qa()
        return person

    def print_map(self):
        row = 0
        width = 16
        for item in self.map:
            print('****************************************************')
            print('*', end='')
            for i in range(0, 3):
                name = self.map[row][i].return_person().get_name() if self.map[row][i].is_player() else ' '
                #print(f'name: {name}')
                #print('*', end='')
                for space in range(0, math.floor((width - len(name)) / 2)):
                    print(' ', end='')
                print(f'{name}', end='')
                for space in range(0, math.ceil((width - len(name)) / 2)):
                    print(' ', end='')
                print('*', end = '')
            print('')
            print('*', end='')
            for i in range(0, 3):
                name = self.map[row][i].return_person().get_name() if self.map[row][i].is_qa() else ' '
                #print('*', end='')
                for space in range(0, math.floor((width - len(name)) / 2)):
                    print(' ', end='')
                print(f'{name}', end='')
                for space in range(0, math.ceil((width - len(name)) / 2)):
                    print(' ', end='')
                print('*', end='')
            print('')
            print(f'*       {str(row + 1) + 'X'}       *       {str(row + 1) + 'Y'}       *       {str(row + 1) + 'Z'}       *')
            print('*', end='')
            for i in range(0, 3):
                name = '?' if self.map[row][0].return_has_item() else ' '
                #print('*', end='')
                for space in range(0, 7):
                    print(' ', end='')
                print(f'{name}', end='')
                for space in range(0, 8):
                    print(' ', end='')
                print('*', end='')
            print('')
            print(f'*                *                *                *')
            row += 1
        print('****************************************************')
