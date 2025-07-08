from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
from pygame import SurfaceType
import pygame
from . import consts
from . import game_state as module_game_state
from . import collider as module_collider

class ProjectileOwner(Enum):
    PLAYER = 0
    ENEMY = 1

Canvas = SurfaceType

number = float | int

class GameObject(ABC):
    game_state: module_game_state.GameStateType
    collider: module_collider.Collider
    position: tuple[number, number] = (0, 0)
    
    @property
    def user_input(self):
        return self.game_state.user_input
    
    @abstractmethod
    def draw(self, canvas: Canvas) -> None:
        pass
    
    @abstractmethod
    def update(self) -> None:
        pass