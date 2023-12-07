import random
from Veggie import Veggie
import os
from Captain import Captain
from Rabit import Rabit
import pickle

class GameEngine:
    """Game engine  class this has all the gaming functions"""

    _NUMBEROFVEGGIES = 30
    _NUMBEROFRABBITS = 5
    _HIGHSCOREFILE = "highscore.data"

    def __init__(self): # This the constructor for the Game Engine class

        self.field = []
        self.rabitsOnFields = []
        self.captain = None
        self.allPossibleVeggies = []
        self.score = 0

    def initVeggies(self): #This one is responsible for reading the csv, plotting the field by placing veggies in it

        fileExists = False

        while fileExists != True:

            fileName = input("Please enter the name of the veggie file: ")

            if os.path.exists(fileName):

                fileExists = True

                # print(f"{fileName} located....    PROCEEDING FURTHER ACTIONS....")

                with open(fileName, 'r') as file:  # We have opened the file and created a 2D array of specified size
                    # print("\nPrinting the lines of the files:......")
                    line_count = 0
                    for line in file:
                        if line_count == 0:
                            # print(line)
                            fieldSize = line.strip().split(",")
                            del fieldSize[0]
                            # print(fieldSize)
                            rows = int(fieldSize[0])
                            columns = int(fieldSize[1])
                            for j in range(rows):
                                self.field.append([None] * columns)
                            # for i in range(rows):
                            #     print(self.field[i])
                        else:
                            veggieName, veggieSymbol, veggiePoints = line.strip().split(",")
                            veggie = Veggie(veggieName, veggieSymbol, int(veggiePoints))
                            self.allPossibleVeggies.append(veggie)

                        line_count += 1

            # Field was initialized, veggie objects were created and inserted in the "listofpossible" veggies

        for _ in range(self._NUMBEROFVEGGIES): #This one randomly inserts the veggies throughout the field
            while True:
                x = random.randint(0, len(self.field) - 1)
                y = random.randint(0, len(self.field[0]) - 1)
                if self.field[x][y] is None:
                    self.field[x][y] = random.choice(self.allPossibleVeggies)
                    # print("inserting veggie into the field")
                    # print("initiating break")
                    break

    def initCaptain(self): # This one is responsible for placing the captain into a random empty location on field

        while True:
            x = random.randint(0, len(self.field) - 1)
            y = random.randint(0, len(self.field[0]) - 1)

            if self.field[x][y] is None:
                self.captain = Captain(x, y)
                self.field[x][y] = self.captain
                break

    def initRabbits(self): # This places 5 rabbits on the random empty locations on the field

        for _ in range(self._NUMBEROFRABBITS):
            while True:
                x = random.randint(0, len(self.field) - 1)
                y = random.randint(0, len(self.field[0]) - 1)
                # print(x, y)
                if self.field[x][y] is None:
                    rabbit = Rabit(x, y)
                    self.field[x][y] = rabbit
                    self.rabitsOnFields.append(rabbit)
                    break

    def initializeGame(self): #This one calls three of the below functions and completly prepares the field
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()
        # GameEngine.initVeggies()
        # GameEngine.initCaptain()
        # GameEngine.initRabbits()

    def remainingVeggies(self): # This one returns the remaining veggies on the field
        veggieCount = 0
        for row in self.field:
            for column in row:
                if isinstance(column, Veggie):
                    veggieCount += 1
        return veggieCount

    def intro(self): # This one just gives the introduction to the player
        print("\n Welcome to Captain Veggie!\n")
        print("The rabbits have invaded your garden and you must harvest "
              "as many vegetables as possible before the rabbits eat them "
              "all! Each vegetable is worth a different number of points "
              "so go for the high score!")
        print("The vegetables are: ")
        print("\n")
        for veggies in self.allPossibleVeggies:
            print(veggies)
        print("\n")
        print("Captain Veggie is V, and the rabbits are R's "
              "Good luck!")

    def printField(self): # This prints the Field whenever required
        maxRowLength = 0
        rowLengthList = []
        for row in self.field:
            for column in row:
                if column is None:
                    maxRowLength += 3
                if column is not None:
                    maxRowLength += 3
            rowLengthList.append(maxRowLength)
            maxRowLength = 0
        # print(max(rowLengthList))
        maxRowLength = max(rowLengthList)

        print("-" * (maxRowLength + 4))

        for row in self.field:
            print("|", end='')
            occupiedColumns = 0
            for column in row:

                if column is None:
                    print("   ", end='')
                    # print(column)
                    occupiedColumns += 3

                else:
                    print(f" {column.getSymbol()} ", end='')
                    occupiedColumns += 3

            remainingcColumns = (maxRowLength + 2) - occupiedColumns
            print(" " * remainingcColumns + "|")

        print("-" * (maxRowLength + 4))
        # print("###########################################################################")

    def getScore(self): #This one returns the score for the player
        return self.score

    def moveRabits(self): # This one moves the rabbits to random locations each time the function is called

        rabitMoves = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]
        maxX = len(self.field)
        maxY = len(self.field[0])
        for rabit in self.rabitsOnFields:
            validMove = False
            while not validMove:
                x_move, y_move = random.choice(rabitMoves)
                newX = rabit.x + x_move
                newY = rabit.y + y_move
                # print(f"newX,newY: {newX},{newY}| oldx,oldy: {rabit.x},{rabit.y}")
                if 0 <= newX < maxX and 0 <= newY < maxY:
                    if self.field[newX][newY] is None or isinstance(self.field[newX][newY], Veggie):
                        self.field[rabit.x][rabit.y] = None
                        rabit.x = newX
                        rabit.y = newY
                        self.field[newX][newY] = rabit
                        validMove = True

    def moveCptVertical(self, verticalMove): #This one handles vertical movements of the captain (up/down)

        column = self.captain.y
        row = self.captain.x
        # print(column, row)
        newRow = self.captain.x + verticalMove
        maxRow = len(self.field)
        # print(f"oldRow,oldColumn: {row},{column} | newRow,newColumn: {newRow},{column}")
        if 0 == newRow or newRow == maxRow:
            print("You can't move that way")

        if 0 <= newRow < maxRow:
            # newPos = self.field[self.captain.x][newY]
            if self.field[newRow][column] is None:
                self.captain.x = newRow
                self.field[newRow][column] = self.captain
                self.field[row][column] = None

            elif isinstance(self.field[newRow][column], Veggie):
                print(f"Yummy! A delicious {self.field[newRow][column].getVegName()}")
                self.captain.addVeggie(self.field[newRow][column])
                self.score += self.field[newRow][column].getVegPoints()
                self.field[row][column] = None
                self.captain.x = newRow
                self.field[newRow][column] = self.captain

            elif isinstance(self.field[newRow][column], Rabit):
                print("Don't step on the bunnies!")

    def moveCptHorizontal(self, horizontalMove): #This one deals with left/right movement of the captain

        column = self.captain.y  # here column and row are captains existing positions
        row = self.captain.x
        # print(row, column)
        newColumn = column + horizontalMove
        maxColumn = len(self.field[0])

        if 0 == newColumn or newColumn == maxColumn:
            print("You can't move that way!")

        if 0 <= newColumn < maxColumn:
            if self.field[row][newColumn] is None:
                self.captain.y = newColumn
                self.field[row][newColumn] = self.captain
                self.field[row][column] = None

            elif isinstance(self.field[row][newColumn], Veggie):
                print(f"Yummy! A delicious {self.field[row][newColumn].getVegName()}")
                self.captain.addVeggie(self.field[row][newColumn])
                self.score += self.field[row][newColumn].getVegPoints()
                self.field[row][column] = None
                self.captain.y = newColumn
                self.field[row][newColumn] = self.captain

            elif isinstance(self.field[row][newColumn], Rabit):
                print("Don't step on the bunnies!")

    def moveCaptain(self): #This one calls the appropriate move function as per the user input to move the captain

        userInput = input("Would you like to move up(W), down(S), left(A), or right(D): ")
        userInput = userInput.lower()
        # print(f"printing user input: {userInput}")

        if userInput == "w":
            self.moveCptVertical(-1)
        elif userInput == "s":
            self.moveCptVertical(1)
        elif userInput == "a":
            self.moveCptHorizontal(-1)
        elif userInput == "d":
            self.moveCptHorizontal(1)
        else:
            print(f"{userInput} is not a valid option")

    def gameOver(self): #This is the game over function :-(
        print("GAME OVER!\n You managed to harvest the following vegetables: ")

        for veggie in self.captain.getVeggieList():
            print(veggie.getVegName())

        print(f"Your score was: {self.getScore()}")

    def highScore(self): #This one reads and writes the highscore to the highscore file

        playerInfo = []

        if os.path.exists(self._HIGHSCOREFILE):
            with open(self._HIGHSCOREFILE, "rb") as file:
                playerInfo = pickle.load(file)

        playerInitials = input("Please enter your three initials to go on the scoreboard: ")[:3].upper()
        playerScore = self.getScore()

        currentScore = (playerInitials, playerScore)

        playerInfo.append(currentScore)

        def sortScore(score):
            return score[1]

        playerInfo.sort(key=sortScore, reverse=True)

        print("HIGH SCORES")

        for score in playerInfo:
            print(f"{score[0]}\t{score[1]}")

        with open(self._HIGHSCOREFILE, "wb") as file:
            pickle.dump(playerInfo, file)




