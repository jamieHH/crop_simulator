#adapted from 'potato_class.py'
from Animal import *

class Sheep(Animal):
    """A Sheep's class"""
    #constructor
    def __init__(self):
        super().__init__(1,4,6)
        self._type = 'Sheep'

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == 'newborn' and water > self._water_need:
                self._weight += self._growth_rate * 1.5
            elif self._status == 'young' and water > self._water_need:
                self._weight += self._growth_rate * 1.25
            else:
                self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()
                    

def main():
    sheep = Sheep()
    print(sheep.report())
    auto_grow(sheep,30)
    print(sheep.report())

if __name__ == '__main__':
    main()
