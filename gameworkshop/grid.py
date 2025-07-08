import pygame
from . import game_object

class Grid(game_object.GameObject):
    render_target: pygame.Surface
    width: int
    height: int
    tiles: list[list[bool]]
    tile_size: int = 32
    def __init__(self, width: int, height: int):
        self.render_target = pygame.Surface((self.tile_size * width, self.tile_size * height))
        self.width = width
        self.height = height
        self.tiles = [[False]*height]*width
    
    def __setitem__(self, item: tuple[int, int], value: bool):
        x, y = item
        self.tiles[x][y] = value
        pygame.draw.rect(self.render_target, (0, 0, 255 * value), (x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))
    
    def __getitem__(self, item: tuple[int, int]) -> bool:
        x, y = item
        return self.tiles[x][y]
    
    def draw(self, canvas):
        canvas.blit(self.render_target, self.position)
    
    def update(self):
        pass