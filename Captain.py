from Creature import Creature

class Captain(Creature):

    def __init__(self, x, y):
        super().__init__(x, y ,'V')
        self.__veggieList = []

    def addVeggie(self, Veggie):
        self.__veggieList.append(Veggie)

    def getVeggieList(self):
        return self.__veggieList


