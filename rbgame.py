# rball.py
from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(n, winsA, winsB)

def printIntro():
    print("This program simulates a game of racquetball\n"
          +"between two players called 'A' and 'B'. The\n"
          +"abilities of each player is indicated by a\n"
          +"probability (between 0 and 1) that the player\n"
          +"wins the point when serving. Player A always\n"
          +"has the first serve.\n")

def getInputs():
    ''' Returns the three simulation parameters '''
    a = eval(input("What's the prob. player A wins a serve?"))
    b = eval(input("What's the prob. player B wins a serve?"))
    n = eval(input("How many games to simulate?"))
    return a, b, n

def simNGames(n, probA, probB):
    '''
    Simulate n games and keeps track of how many wins
    there are for each player
    '''
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB):
    '''
    Simulates a single game. Returns scores for A and B.
    '''
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    '''
    a and b represent scores for a racquetball game.
    Returns True if the game is over, False otherwise.
    '''
    return a==15 or b==15

def printSummary(n, winsA, winsB):
    '''Prints a summary of wins for each player.'''
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == '__main__':
    main()
