from Spot import *
from Tainer import *
from QA import *
from Item import *
import random

class Map:
    def __init__(self):
        self.map = self.generate_map()

    def __str__(self):
        for item in self.map:
            for i in item:
                print(i)

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
        name = str(input('Please enter your name: '))
        self.map[2][1].update_person(Tainer(name))

    def generate_name(self):
        names = ['Scott', 'Jacob', 'Daniel', 'Hoffstetter', 'Gary']
        random_num = random.randint(0, len(names) - 1)
        return names[random_num]

    def place_qa(self, name):
        random_num = random.randint(0, 14)
        if random_num != 8:
            row = random_num // 3
            col = random_num % 3
            #print(f'QA added at row {row}, col {chr(col + 88)}')
            self.map[row][col].update_person(QA(name))

    def place_new_qa(self, name):
        while True:
            random_num = random.randint(0, 14)
            if self.map[random_num // 3][random_num % 3].return_person() is None:
                self.map[random_num // 3][random_num % 3].update_person(QA(name))
                break

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
        person = self.map[row][col].return_person()
        if person is None:
            return False
        else:
            return True

    def print_map(self):
        row = 0
        for item in self.map:
            print('****************************************************')
            print(f'*       {self.map[row][0].return_person().get_name() if self.map[row][0].is_player() else ' '}        *       {self.map[row][1].return_person().get_name() if self.map[row][1].is_player() else ' '}        *       {self.map[row][2].return_person().get_name() if self.map[row][2].is_player() else ' '}        *')
            print(f'*       {self.map[row][0].return_person().get_name() if self.map[row][0].is_qa() else ' '}        *       {self.map[row][1].return_person().get_name() if self.map[row][1].is_qa() else ' '}        *       {self.map[row][2].return_person().get_name() if self.map[row][2].is_qa() else ' '}        *')
            print(f'*       {str(row + 1) + 'X'}       *       {str(row + 1) + 'Y'}       *       {str(row + 1) + 'Z'}       *')
            print(f'*       {'?' if self.map[row][0].return_has_item() else ' '}        *       {'?' if self.map[row][1].return_has_item() else ' '}        *       {'?' if self.map[row][2].return_has_item() else ' '}        *')
            print(f'*                *                *                *')
            row += 1
        print('****************************************************')
