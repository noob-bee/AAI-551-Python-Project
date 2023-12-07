import random
from Veggie import Veggie
import os
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
