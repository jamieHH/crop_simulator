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

    def Needs(self):
        

    def Report(self):
        

def main():
    #instantiate class
    

if __name__ == "__main__":
    main()
