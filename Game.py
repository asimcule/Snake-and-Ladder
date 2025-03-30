import random
from Board import *
from Player import *
from Die import *
import pygame

class Game:
    def __init__(self, players):
        self.players=players
        self.roll=0
        self.HEIGHT=800
        self.WIDTH=800
        self.running=True
        self.screen=None
    
    def createGame(self):
        pygame.init()
        self.screen=pygame.display.set_mode((self.HEIGHT, self.WIDTH))
        self.rect_width=self.WIDTH//10
        self.rect_height=self.HEIGHT//10
        pygame.font.init()
        self.font=pygame.font.Font(None, 36)


    def startGame(self):
        self.main_board=Board()      # create a board object
        self.player1=Player("Asim", "asset.png")
        player_image, player_rect=self.player1.initialize()
        self.die=Die()

        while self.running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
                
                if event.type==pygame.MOUSEBUTTONUP:
                    die.rollDie()
                    print(die.roll)
                    self.player1.move(die.roll)
            
            # Rendering the game objects on the screen
            self.screen.fill("white")
            # drawing the board on the screen
            for i in self.main_board.getBoard():
                center_x=(i%10)*self.rect_width        # changing the x coordinate 
                center_y=(i//10)*self.rect_height        # changing the y coordinate
                rect=pygame.Rect(center_x, center_y, self.rect_width, self.rect_height) # creating the rectangle object
                pygame.draw.rect(self.screen, (0,0,255), rect, 5)
                if (i//10)!=9: # alternate number sides
                    text_surface = self.font.render(f"{100-i}", True, (0,0,0))
                else:
                    text_surface = self.font.render(f"{abs((89-i))}", True, (0,0,0))
                text_rect = text_surface.get_rect(center=rect.center)  # Center text inside rectangle
                self.screen.blit(text_surface, text_rect)

                # place the player on the screen
                player_rect.topleft=((self.player1.position%10)*self.rect_width, (self.player1.position//10)*self.rect_height)
                self.screen.blit(player_image, player_rect)

            pygame.display.flip()
        pygame.quit()

            
    def endGame(self):
        pass

    def drawBoard(self):
        pass

    

game=Game(2)
game.createGame()
game.startGame()
