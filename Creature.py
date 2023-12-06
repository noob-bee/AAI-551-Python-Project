from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):

    def __init__(self, x, y, creature_symbol):
        super().__init__(creature_symbol)
        self.__x = x
        self.__y = y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

