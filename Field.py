from Potato_class import *
from Wheat_class import *
from Cow_class import *
from Sheep_class import *
import random

class Field:
    """simulate the field that can contain crops and animals"""
    #constructor
    def __init__(self,max_crops,max_animals):
        self._crops = []
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_crops

    def plant_crop(self,crop):
        pass

    def add_animal(self,animal):
        pass
