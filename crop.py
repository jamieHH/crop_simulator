import random

class Crop:
    """Generic food crop"""
    #constructor
    def __init__(self,growth_rate,light_need,water_need):
        #set atributes with initial values
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "seed"
        self._type = "generic"
        # underscores indicate private attrubutes

    #method to indicate needs of the crop    
    def needs(self):
        #return a dictionary containing light and water needs
        return {'light need':self._light_need,'water need':self._water_need}

    #method to report the provide information about the crop state
    def report(self):
        return {'type':self._type,'status':self._status,'growth':self._growth,'days growing':self._days_growing}

    #private method used by grow() to update status of the crop
    def _update_status(self):
        if self._growth > 15:
            self._status = 'old'
        elif self._growth > 10:
            self._status = 'mature'
        elif self._growth > 5:
            self._status = 'young'
        elif self._growth > 0:
            self._status = 'seedling'
        elif self._growth == 0:
            self._status = 'seed'
    
    #method to grow the crop based on water and light values
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()

#function to grow crops with user friendly interface
def auto_grow(crop,days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)

def manual_grow(crop):
    valid = False
    while not valid:
        try:
            light = int(input('Enter a light value (1-10): '))
            if 1 <= light <= 10:
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
    crop.grow(light,water)

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

def manage_crop(crop):
    print('This is the crop management program')
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(crop)
            print()
        elif option == 2:
            auto_grow(crop,30)
            print()
        elif option == 3:
            print(crop.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print('Exiting crop management')
        
def main():
    #instantiate class
    new_crop = Crop(1,4,3)
    manage_crop(new_crop)

if __name__ == "__main__":
    main()
