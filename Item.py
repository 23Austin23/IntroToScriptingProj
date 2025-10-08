ITEMS = ['socket wrench', 'socket wrench extension',
'socket', 'screw driver', 'pair of safety glasses', 'mirror', 'torque wrench']

class Item:
    def __init__(self, name):
        self.name = name.upper()

    def return_name(self):
        return self.name