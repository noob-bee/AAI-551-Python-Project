from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):

    def __init__(self, x, y, creature_symbol):
        super().__init__(creature_symbol)
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

