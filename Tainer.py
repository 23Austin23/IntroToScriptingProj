from Player import *
class Tainer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.found_items = []
        self.location = '2Y'

    def __str__(self):
        print(f'Tainer: {self.name} Location: {self.location} Tools Found: {self.found_items}')

    def get_name(self):
        return super().get_name()

    def return_items(self):
        return self.found_items

    def set_loc(self, row, col):
        self.location = str(row) + chr(col + 88)

    def get_loc(self):
        return self.location

    def get_pos_moves(self):
        player_location = self.get_loc()
        row = int(player_location[0])
        col = ord(player_location[1]) - 88
        if (row == 1 or row == 2 or row == 3) and col == 1:
            pos_moves = ((row, col + 1), (row, col - 1), (row - 1, col), (row + 1, col))
        else:
            if row == 0 and col == 1:
                pos_moves = ((row, col + 1), (row, col - 1), (row + 1, col))
            elif row == 4 and col == 1:
                pos_moves = ((row, col - 1), (row, col + 1), (row - 1, col))
            elif row == 4 and col == 0:
                pos_moves = ((row, col + 1), (row - 1, col))
            elif row == 4 and col == 2:
                pos_moves = ((row, col - 1), (row - 1, col))
            elif row == 0 and col == 0:
                pos_moves = ((row, col + 1), (row + 1, col))
            elif row == 0 and col == 2:
                pos_moves = ((row, col - 1), (row + 1, col))
            elif (row != 0 or row != 4) and col == 0:
                pos_moves = ((row, col + 1), (row - 1, col), (row + 1, col))
            else:
                pos_moves = ((row, col - 1), (row + 1, col), (row - 1, col))
        return pos_moves

