class Spot:
    def __init__(self):
        self.person = None
        self.item = None

    def __str__(self):
        print(self.person if self.person is not None else "None")
        print(self.item if self.item is not None else "None")

    def return_num_stuff(self):
        count = 0
        if self.person is not None:
            count += 1
        if self.item is not None:
            count += 1
        return count

    def update_person(self, person):
        self.person = person

    def remove_person(self):
        self.person = None

    def update_item(self, item):
        self.item = item

    def remove_item(self):
        self.item = None

    def return_person(self):
        return self.person

    def return_has_item(self):
        return self.item is not None

    def return_item_name(self):
        return self.item.return_name() if self.item is not None else "nothing here!"

    def get_pos_moves(self):
        return self.person.get_pos_moves()