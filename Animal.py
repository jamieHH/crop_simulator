#program overwriten from 'crop.py'
import random

class Animal:
    """Generic animal"""
    #constructor
    def __init__(self,growth_rate,food_need,water_need):
        #set atributes with initial values
        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "newborn"
        self._type = "generic"
        # underscores indicate private attrubutes

    #method to indicate needs of the crop    
    def needs(self):
        #return a dictionary containing light and water needs
        return {'food need':self._food_need,'water need':self._water_need}

    #method to report the provide information about the crop state
    def report(self):
        return {'type':self._type,'status':self._status,'weight':self._weight,'days growing':self._days_growing}

    #private method used by grow() to update status of the crop
    def _update_status(self):
        if self._weight > 15:
            self._status = 'old'
        elif self._weight > 10:
            self._status = 'mature'
        elif self._weight > 5:
            self._status = 'young'
        elif self._weight > 0:
            self._status = 'child'
        elif self._weight == 0:
            self._status = 'newborn'
    
    #method to grow the crop based on water and light values
    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()

#function to grow crops with user friendly interface
def auto_grow(animal,days):
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food,water)

def manual_grow(animal):
    valid = False
    while not valid:
        try:
            food = int(input('Enter a food amount (1-10): '))
            if 1 <= food <= 10:
                valid = True
            else:
                print('Not valid, enter between 1-10')
        except ValueError:
            print('Not valid, enter between 1-10')
    valid = False
    while not valid:
        try:
            water = int(input('Enter a water value (1-10): '))
            if 1 <= water <= 10:
                valid = True
            else:
                print('Not valid, enter between 1-10')
        except ValueError:
            print('Not valid, enter between 1-10')
    #grow the crop
    animal.grow(food,water)

def display_menu():
    print('1. Grow manually over 1 day')
    print('2. Auto grow over 30 days')
    print('3. Report status')
    print('0. Exit test program')
    print()
    print('Select an option from above')

def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input('Option select: '))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print('Please enter a valid option')
        except ValueError:
            print('Options are integers, enter a valid option.')
    return choice

def manage_animal(animal):
    print('This is the animal management program')
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(animal)
            print()
        elif option == 2:
            auto_grow(animal,30)
            print()
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print('Exiting crop management')
        
def main():
    #instantiate class
    new_animal = Animal(1,4,3)
    manage_animal(new_animal)

if __name__ == "__main__":
    main()
