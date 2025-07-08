from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Literal, Self
import random
import time
import math
from pathlib import Path
from functools import lru_cache
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
    position: tuple[number, number]
    
    @property
    def user_input(self):
        return self.game_state.user_input
    
    def get_draw_details(self) -> consts.DrawDetails:
        return consts.DrawDetails.NONE
    
    @abstractmethod
    def draw(self, canvas: Canvas) -> None:
        pass
    
    @abstractmethod
    def update(self) -> None:
        pass