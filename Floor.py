class Floor:
    def __init__(self, floor_number):
        self._floor_number = floor_number

    def get_floor_number(self):
        return self._floor_number

    def set_floor_number(self, floor_number):
        self._floor_number = floor_number

# Create a list to store the instances of Floor
floors = []

# Create seven instances of Floor and add them to the list
for i in range(1, 8):
    floor = Floor(floor_number=i)
    floors.append(floor)
