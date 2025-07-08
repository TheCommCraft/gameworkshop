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
        self.vy += 0.5
        keys = pygame.key.get_pressed()
        self.vx += (keys[pygame.K_d] - keys[pygame.K_a])
        self.vx *= 0.8
        self.vy *= 0.999
        self.position = (
            self.position[0] + self.vx,
            self.position[1] + self.vy
        )
        x, y = int(self.position[0]) // consts.TILE_SIZE, int(self.position[1]) // consts.TILE_SIZE
        if self.grid[x, y]:
            self.vy = -1
        if self.position[1] > consts.SCREEN_HEIGHT + consts.TILE_SIZE:
            self.position = (self.position[0], -consts.TILE_SIZE)