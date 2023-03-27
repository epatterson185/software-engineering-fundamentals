class Desk:
    def __init__(self, desk_number):
        self._desk_number = desk_number

    def get_desk_number(self):
        return self._desk_number

    def set_desk_number(self, desk_number):
        self._desk_number = desk_number

# Create a list to store the instances of Desk
desks = []

# Create 50 instances of Desk and add them to the list
for i in range(50):
    desk = Desk(desk_number=i+1001)
    desks.append(desk)
