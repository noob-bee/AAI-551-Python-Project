from GameEngine import GameEngine

def main():

    gameEngine = GameEngine()

    gameEngine.initializeGame()
    gameEngine.intro()
    remainingVeggies = gameEngine.remainingVeggies()

    while remainingVeggies != 0:

        print(f"{remainingVeggies} veggies remaining. Current score: {gameEngine.getScore()}")
        gameEngine.printField()
        gameEngine.moveRabits()

        gameEngine.moveCaptain()

        remainingVeggies = gameEngine.remainingVeggies()

    gameEngine.gameOver()
    gameEngine.highScore()

main()