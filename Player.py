import pygame

class Player:
    def __init__(self, name, image, character=None, color="BLUE"):
        self.name=name
        self.character=character
        self.color=color
        self.position=0
        self.image=image
        self.image_width=70
        self.image_height=70

    def initialize(self):
        self.image=pygame.image.load(self.image)
        self.resized_image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.image_rect=self.resized_image.get_rect()       # change position using player.topleft
        return self.resized_image, self.image_rect


    def move(self, value):
        self.position+=value
    
