# adapted from 'crops.py'
from Sheep_class import *
from Cow_class import *

def display_menu():
    print()
    print('Which animal do you want to manage>')
    print('1. Cow')
    print('2. Sheep')
    print()
    print('Select an option')

def select_option():
    valid = False
    while not valid:
        try:
            choice = int(input('Option select: '))
            if choice in (1,2):
                valid = True
            else:
                print('Enter a valid option')
        except ValueError:
            print('option is an integer, enter a valid option')
    print()
    return choice

def create_animal():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_animal = Cow()
    elif choice == 2:
        new_animal = Sheep()
    return new_animal

def main():
    new_animal = create_animal()
    manage_animal(new_animal)

if __name__ == "__main__":
    main()
