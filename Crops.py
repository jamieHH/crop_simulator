from Wheat_class import *
from Potato_class import *

def display_menu():
    print()
    print('Which crop do you want to create>')
    print('1. Potato')
    print('2. Wheat')
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

def create_crop():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_crop = Potato()
    elif choice == 2:
        new_crop = Wheat()
    return new_crop

def main():
    new_crop = create_crop()
    manage_crop(new_crop)

if __name__ == "__main__":
    main()
