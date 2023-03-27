class Managers:
    def __init__(self, first_name, last_name, department, location, building):
        self._first_name = first_name
        self._last_name = last_name
        self._department = department
        self._location = location
        self._building = building

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_department(self):
        return self._department

    def set_department(self, department):
        self._department = department

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def get_building(self):
        return self._building

    def set_building(self, building):
        self._building = building
        
manager1 = Managers("Mark", "Rankin", "Digital", "Belfast", "Riverside")
manager2 = Managers("John", "Copes", "Consumer", "Birmingham", "Snowhill")
manager3 = Managers("Abigail", "Spratt", "Wholesale", "London", "One Braham")
manager4 = Managers("Jeremy", "Hammond", "Digital", "Manchester", "New Bailey")
manager5 = Managers("Lucy", "Dale", "Digital", "Belfast", "Riverside")
manager_list = [manager1, manager2, manager3, manager4, manager5]