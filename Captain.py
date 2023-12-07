from Creature import Creature

class Captain(Creature):

    def __init__(self, x, y):
        super().__init__(x, y ,'V')
        self.veggieList = []

    def addVeggie(self, Veggie):
        self.veggieList.append(Veggie)

    def getVeggieList(self):
        return self.veggieList


