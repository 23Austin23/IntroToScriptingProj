from Player import *
class Tainer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.found_items = []
        self.location = '2Y'

    def get_name(self):
        return super().get_name()

    def return_items(self):
        return self.found_items

    def secure_item(self, item_name):
        self.found_items.append(item_name)

    def set_loc(self, row, col):
        self.location = str(row) + chr(col + 88)

    def get_loc(self):
        return self.location

    def get_pos_moves(self):
        player_location = self.get_loc()
        row = int(player_location[0])
        col = ord(player_location[1]) - 88
        if (row == 1 or row == 2 or row == 3) and col == 1:
            pos_moves = ((row, col + 1, 'W'), (row, col - 1, 'E'), (row - 1, col, 'S'), (row + 1, col, 'N'))
        else:
            if row == 0 and col == 1:
                pos_moves = ((row, col + 1, 'W'), (row, col - 1, 'E'), (row + 1, col, 'N'))
            elif row == 4 and col == 1:
                pos_moves = ((row, col - 1, 'E'), (row, col + 1, 'W'), (row - 1, col, 'S'))
            elif row == 4 and col == 0:
                pos_moves = ((row, col + 1, 'W'), (row - 1, col, 'S'))
            elif row == 4 and col == 2:
                pos_moves = ((row, col - 1, 'E'), (row - 1, col, 'S'))
            elif row == 0 and col == 0:
                pos_moves = ((row, col + 1, 'W'), (row + 1, col, 'N'))
            elif row == 0 and col == 2:
                pos_moves = ((row, col - 1, 'E'), (row + 1, col, 'N'))
            elif (row != 0 or row != 4) and col == 0:
                pos_moves = ((row, col + 1, 'W'), (row - 1, col, 'S'), (row + 1, col, 'N'))
            else:
                pos_moves = ((row, col - 1, 'E'), (row + 1, col, 'N'), (row - 1, col, 'S'))
        return pos_moves

