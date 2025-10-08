from Tainer import *
from QA import *
class Spot:
    def __init__(self):
        self.person = None
        self.item = None

    def update_person(self, person):
        self.person = person

    def remove_person(self):
        #print('removing person')
        # print(f'person: {self.person if isinstance(self.person, QA) or isinstance(self.person, Tainer) else "None"}')
        self.person = None
        return self

    def update_item(self, item):
        self.item = item

    def remove_item(self):
        self.item = None

    def return_person(self):
        return self.person

    def return_has_item(self):
        return self.item is not None

    def return_item(self):
        return self.item

    def return_item_name(self):
        return self.item.return_name() if self.item is not None else "nothing here!"

    def get_pos_moves(self):
        return self.person.get_pos_moves()

    def is_player(self):
        is_player = isinstance(self.person, Tainer)
        return is_player

    def is_qa(self):
        is_qa = isinstance(self.person, QA)
        return is_qa