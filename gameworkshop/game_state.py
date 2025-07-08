from __future__ import annotations
from dataclasses import dataclass, field
import pygame
from . import consts

@dataclass
class GameState:
    canvas: pygame.Surface
    running: bool
    
    def start(self):
        self.canvas = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
        self.running = True
        while self.running:
            pass