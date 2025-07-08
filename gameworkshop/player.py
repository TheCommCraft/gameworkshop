import pygame
from . import game_object
from . import consts
from .grid import Grid

class Player(game_object.GameObject):
    width: int
    height: int
    grid: Grid
    vx: game_object.number
    vy: game_object.number
    def __init__(self, width: int, height: int, grid: Grid):
        self.width = width
        self.height = height
        self.grid = grid
        self.vx = 0
        self.vy = 0
    
    def draw(self, canvas):
        pygame.draw.rect(canvas, (255, 0, 0), (self.position[0], self.position[1], self.width, self.height))
    
    def update(self):
        self.vy += 1
        keys = pygame.key.get_pressed()
        self.vx += (keys[pygame.K_d] - keys[pygame.K_a])
        self.vx *= 0.8
        self.vy *= 0.8
        self.position = (
            self.position[0] + self.vx,
            self.position[1] + self.vy
        )
        x, y = self.position[0] // consts.TILE_SIZE, self.position[1] // consts.TILE_SIZE
        self.vy = self.grid[x, y]