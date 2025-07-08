import pygame
from . import game_object

class Grid(game_object.GameObject):
    render_target: pygame.Surface
    def __init__(self):
        self.render_target = pygame.Surface()
    
    def draw(self, canvas):
        canvas.blit(self.render_target, self.position)
    
    def update(self):
        pass