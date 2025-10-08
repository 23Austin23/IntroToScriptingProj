from Player import *
import random

class QA(Player):
    def __init__(self, name):
        super().__init__(name)
        self.location = None

    def get_name(self):
        return self.name

    def get_pos_moves(self, map):
        #Calculate possible moves, randomize it
        pass

    def set_location(self, location):
        self.location = location

    def get_loc(self):
        loc = self.location
        loc = str(int(loc[0]) - 1) + loc[1]
        return loc

    def set_loc(self, row, col):
        self.location = str(row + 1) + chr(col + 88)
        #print(f'loc set: {self.location}')

    def move_dont_move(self):
        number = random.randint(1, 6)
        if number == 3:
            return False
        return True

    def get_pos_moves(self):
        player_location = self.get_loc()
        row = int(player_location[0])
        col = ord(player_location[1]) - 88
        if (row == 1 or row == 2 or row == 3) and col == 1:
            pos_moves = [(row, col + 1), (row, col - 1), (row - 1, col), (row + 1, col)]
        else:
            if row == 0 and col == 1:
                pos_moves = [(row, col + 1), (row, col - 1), (row + 1, col)]
            elif row == 4 and col == 1:
                pos_moves = [(row, col - 1), (row, col + 1), (row - 1, col)]
            elif row == 4 and col == 0:
                pos_moves = [(row, col + 1), (row - 1, col)]
            elif row == 4 and col == 2:
                pos_moves = [(row, col - 1), (row - 1, col)]
            elif row == 0 and col == 0:
                pos_moves = [(row, col + 1), (row + 1, col)]
            elif row == 0 and col == 2:
                pos_moves = [(row, col - 1), (row + 1, col)]
            elif (row != 0 or row != 4) and col == 0:
                pos_moves = [(row, col + 1), (row - 1, col), (row + 1, col)]
            else:
                pos_moves = [(row, col - 1), (row + 1, col), (row - 1, col)]
        return pos_moves