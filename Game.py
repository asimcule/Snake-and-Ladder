import random
from Board import *
import pygame

class Game:
    def __init__(self, players):
        self.players=players
        self.roll=0
        self.HEIGHT=1280
        self.WIDTH=720
        self.running=True
        self.screen=None
    
    def createGame(self):
        pygame.init()
        self.screen=pygame.display.set_mode((self.HEIGHT, self.WIDTH))


    def startGame(self):
        self.main_board=Board()      # create a board object
        while self.running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
            
            # drawing the board on the screen
            for item in self.main_board.getBoard():
                print(item)

            
            self.screen.fill("white")
            pygame.display.flip()
        pygame.quit()

            
    def endGame(self):
        pass

    def drawBoard(self):
        pass

    

game=Game(2)
game.createGame()
game.startGame()
