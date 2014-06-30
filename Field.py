from Potato_class import *
from Wheat_class import *
from Sheep_class import *
from Cow_class import *
import random

class Field:
    """simulate the field that can contain crops and animals"""

    #constructor
    def __init__(self,max_animals,max_crops):
        self._crops = []
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_crops

    def plant_crop(self,crop):
        if len(self._crops) < self._max_crops:
            self._crops.append(crop)
            return True
        else:
            return False

    def add_animal(self,animal):
        if len(self._animals) < self._max_animals:
            self._animals.append(animal)
            return True
        else:
            return False

    def harvest_crop(self,position):
        return self._crops.pop(position)

    def remove_animal(self,position):
        return self._animals.pop(position)

    def report_contents(self):
        crop_report = []
        animal_report = []
        for crop in self._crops:
            crop_report.append(crop.report())
        for animal in self._animals:
            animal_report.append(animal.report())
        return {'crops': crop_report, 'animals': animal_report}

    def report_needs(self):
        food = 0
        light = 0
        water = 0
        for crop in self._crops:
            needs = crop.needs()
            if needs['light need'] > light:
                light = needs['light need']
            if needs['water need'] > water:
                water = needs['water need']
        for animal in self._animals:
            needs = animal.needs()
            food += needs['food need']
            if needs['water need'] > water:
                water = needs['water need']
        return {'food': food,'light': light,'water': water}

    def grow(self,):
        pass

def display_crops(crop_list):
    print()
    print('the folowing crops are in this field:')
    pos = 1
    for crop in crop_list:
        print('{0:2}. {1}'.format(pos,crop.report()))
        pos +=1

def display_animals(animal_list):
    print()
    print('The folowing animals are in this field:')
    for pos in range(len(animal_list)):
        print('{0:>2}. {1}.'.format(pos +1,animal_list[pos].report()))

def select_crop(length_list):
    valid = False
    while not valid:
        selected = int(input('Select a crop: '))
        if selected in range(1,length_list +1):
            valid = True
        else:
            print('Enter a valid option')
    return selected -1

def select_animal(length_list):
    selected = 0
    while selected not in range(1,length_list +1):
        selected = int(input('Select an animal: '))
        if selected not in range(1,length_list +1):
            print('Enter a valid option')
    return selected -1

def harvest_crop_from_field(field):
    display_crops(field._crops)
    selected_crop = select_crop(len(field._crops))
    return field.harvest_crop(selected_crop)

def remove_animal_from_field(field):
    display_animals(field._animals)
    selected_animal = select_animal(len(field._animals))
    return field.remove_animal(selected_animal)

def main():
    new_field = Field(5,2)
    new_field.plant_crop(Wheat())
    new_field.plant_crop(Potato())    
    new_field.add_animal(Sheep()) #animal names??
    new_field.add_animal(Cow())
    report = new_field.report_contents()
    print(report)
    report = new_field.report_needs()
    print(report)


if __name__ == "__main__":
    main()
