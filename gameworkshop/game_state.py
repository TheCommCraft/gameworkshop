from __future__ import annotations
from dataclasses import dataclass, field
import pygame
from . import consts

@dataclass
class GameState:
    canvas: pygame.Surface = field(init=False)
    running: bool = False
    
    def start(self):
        self.canvas = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
        self.running = True
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False