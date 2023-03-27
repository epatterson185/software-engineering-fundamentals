from Managers import manager_list
from Desk import desks
from Floor import floors

class Menu:
    def __init__(self):
        self.logged_in = False
        self.manager = None

    def login(self):
        while not self.logged_in:
            first_name = input("Please enter your first name: ")
            last_name = input("Please enter your last name: ")
            for manager in manager_list:
                if manager.get_first_name() == first_name and manager.get_last_name() == last_name:
                    self.logged_in = True
                    self.manager = manager
                    print("Logged in as {} {}.".format(first_name, last_name))
                    break
            if not self.logged_in:
                print("Invalid login credentials. Please try again. This is case-sensitive")

def book_desk(self):
    while True:
        desk_number = input("Please enter the desk number you would like to book (1001-1050): ")
        if not desk_number.isdigit():
            print("Invalid input. Desk number must be a number.")
            continue
        desk_number = int(desk_number)
        if not (1001 <= desk_number <= 1050):
            print("Invalid input. Desk number must be between 1001 and 1050.")
            continue
        desk = self.desks[desk_number - 1001]
        if desk.get_manager():
            print("This desk is already booked.")
            continue
        desk.set_manager(self.manager)
        print("Desk {} has been booked by {} {}.".format(desk_number, self.manager.get_first_name(), self.manager.get_last_name()))
        break

def unbook_desk(self):
    while True:
        desk_number = input("Please enter the desk number you would like to unbook (1001-1050): ")
        if not desk_number.isdigit():
            print("Invalid input. Desk number must be a number.")
            continue
        desk_number = int(desk_number)
        if not (1001 <= desk_number <= 1050):
            print("Invalid input. Desk number must be between 1001 and 1050.")
            continue
        desk = self.desks[desk_number - 1001]
        if not desk.get_manager():
            print("This desk is already unbooked.")
            continue
        if desk.get_manager() != self.manager:
            print("You are not authorized to unbook this desk.")
            continue
        desk.set_manager(None)
        print("Desk {} has been unbooked by {} {}.".format(desk_number, self.manager.get_first_name(), self.manager.get_last_name()))
        break

def run(self):
    self.login()
    while True:
        print("1. Book a desk")
        print("2. Unbook a desk")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.book_desk()
        elif choice == "2":
            self.unbook_desk()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

menu = Menu()
menu.login()
menu.book_desk()

while True:
    print("1. Book a desk")
    print("2. Unbook a desk")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        menu.book_desk()
    elif choice == "2":
        menu.unbook_desk()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")