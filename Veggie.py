from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):

    def __init__(self, veg_name, veg_symbol, veg_points):
        super().__init__(veg_symbol)
        self.__veg_name = veg_name
        self.__veg_points = veg_points

    def setVegName(self, veg_name):
        self.__veg_name = veg_name

    def setVegPoints(self, veg_points):
        self.__veg_points = veg_points

    def getVegName(self):
        return self.__veg_name

    def getVegPoints(self):
        return self.__veg_points

    def __str__(self):
        print(f"Vegetable Symbol: {self.getSymbol()}, Vegetable Points: {self.getVegPoints()}, Vegetable Name: {self.getVegName()}")

