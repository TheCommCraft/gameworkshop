from __future__ import annotations
from dataclasses import dataclass, field
import pygame
from . import consts
from . import data_structures
from . import game_object

@dataclass
class GameState:
    canvas: pygame.Surface = field(init=False)
    running: bool = False
    objects: data_structures.ObjectContainer = field(default_factory=data_structures.ObjectContainer)
    clock: pygame.time.Clock = field(default_factory=pygame.time.Clock)
    
    def add_obj(self, obj: game_object.GameObject):
        self.objects.add_object(obj)
    
    def remove_obj(self, obj: game_object.GameObject):
        self.objects.remove_object(obj)
    
    def remove_all(self):
        self.objects.remove_all()
    
    def init(self):
        self.canvas = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
    
    def start(self):
        self.running = True
        while self.running:
            self.canvas.fill((255, 255, 255))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            for obj in self.objects:
                obj.update()
            for obj in self.objects:
                obj.draw(self.canvas)
            pygame.display.flip()
            self.clock.tick(60)