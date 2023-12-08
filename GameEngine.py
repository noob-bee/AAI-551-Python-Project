import random
from Veggie import Veggie
import os
from Captain import Captain
from Rabit import Rabit

class GameEngine:

    _NUMBEROFVEGGIES = 30
    _NUMBEROFRABBITS = 5
    _HIGHSCOREFILE = "highscore.data"

    def __init__(self):

        self.field = []
        self.rabitsOnFields = []
        self.captain = None
        self.allPossibleVeggies = []
        self.score = 0

    def initVeggies(self):

        fileExists = False

        while fileExists != True:

            fileName = input("Please enter the name of the veggie file: ")

            if os.path.exists(fileName):

                fileExists = True

                print(f"{fileName} located....    PROCEEDING FURTHER ACTIONS....")

                with open(fileName, 'r') as file:  # We have opened the file and created a 2D array of specified size
                    print("\nPrinting the lines of the files:......")
                    line_count = 0
                    for line in file:
                        if line_count == 0:
                            print(line)
                            fieldSize = line.strip().split(",")
                            del fieldSize[0]
                            print(fieldSize)
                            rows = int(fieldSize[0])
                            columns = int(fieldSize[1])
                            for j in range(rows):
                                self.field.append([None] * columns)
                            for i in range(rows):
                                print(self.field[i])
                        else:
                            veggieName, veggieSymbol, veggiePoints = line.strip().split(",")
                            veggie = Veggie(veggieName, veggieSymbol, int(veggiePoints))
                            self.allPossibleVeggies.append(veggie)

                        line_count += 1

            # Field was initialized, veggie objects were created and inserted in the "listofpossible" veggies

        for _ in range(self._NUMBEROFVEGGIES):
            while True:
                x = random.randint(0, len(self.field) - 1)
                y = random.randint(0, len(self.field[0]) - 1)
                if self.field[x][y] is None:
                    self.field[x][y] = random.choice(self.allPossibleVeggies)
                    # print("inserting veggie into the field")
                    # print("initiating break")
                    break

    def initCaptain(self):

        while True:
            x = random.randint(0, len(self.field) - 1)
            y = random.randint(0, len(self.field[0]) - 1)

            if self.field[x][y] is None:
                self.captain = Captain(x, y)
                self.field[x][y] = self.captain
                break

    def initRabbits(self):

        for _ in range(self._NUMBEROFRABBITS):
            while True:
                x = random.randint(0, len(self.field) - 1)
                y = random.randint(0, len(self.field[0]) - 1)
                print(x, y)
                if self.field[x][y] is None:
                    rabbit = Rabit(x, y)
                    self.field[x][y] = rabbit
                    self.rabitsOnFields.append(rabbit)
                    break

    def initializeGame(self):
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()
        # GameEngine.initVeggies()
        # GameEngine.initCaptain()
        # GameEngine.initRabbits()

    def remainingVeggies(self):
        veggieCount = 0
        for row in self.field:
            for column in row:
                if isinstance(column, Veggie):
                    veggieCount += 1
        return veggieCount

    def intro(self):
        print("\n Welcome to Captain Veggie!\n")
        print("The rabbits have invaded your garden and you must harvest"
              "as many vegetables as possible before the rabbits eat them"
              "all! Each vegetable is worth a different number of points"
              "so go for the high score!")
        print("The vegetables are: ")
        for veggies in self.allPossibleVeggies:
            print(veggies)
        print("Captain Veggie is V, and the rabbits are R's"
              "Good luck!")