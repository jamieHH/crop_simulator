from crop import *

class Wheat(Crop):
    """A potato class"""
    #constructor
    def __init__(self):
        super().__init__(1,3,6)
        self._type = 'wheat'

    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == 'seedling':
                self._growth += self._growth_rate * 1.5
            elif self._status == 'young':
                self._growth += self._growth_rate * 1.25
            elif self._status == 'old':
                self._growth += self._growth_rate / 2
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()
                    

def main():
    wheat = Wheat()
    print(wheat.report())
    auto_grow(wheat,30)
    print(wheat.report())

if __name__ == '__main__':
    main()
