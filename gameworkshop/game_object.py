from __future__ import annotations # Das sorgt dafür, dass Typannotationen besser funktionieren.
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
from . import game_state as module_game_state # Das "." sorgt für einen relativen Import also einen aus dem derzeitigen Modul.
from . import sound as module_sound
from . import collider as module_collider
from . import consts
from . import data_structures
from .images import load_image, Image
# Das ist ein Kommentar, er wird nicht als Code interpretiert.


class ProjectileOwner(Enum):
    PLAYER = 0
    ENEMY = 1

Canvas = SurfaceType

number = float | int #Wenn der Typ sowohl float, als auch int sein kann, wird number angegeben.

class GameObject(ABC):
    """
    Die Basisklasse für gemalte Objekte.
    """
    """
    Das (ABC) bedeutet, dass diese Klasse eine abstrakte Klasse ist. Eine abstrakte Klasse ist eine Klasse, 
    bei der bestimmte Methoden nicht implementiert sind. Eine solche Klasse kann nicht instanziiert werden. 
    Von ihr muss geerbt werden und in der geerbten Klasse müssen die nicht implementierten Methoden 
    implementiert werden, damit man sie instanziieren kann. Abstrakte Klassen werden verwendet, um quasi
    grundlegende Bausteine zu definieren, ohne zu beschreiben, wie genau diese im Inneren funktionieren.
    """
    game_state: module_game_state.GameStateType
    collider: module_collider.Collider
    
    @property
    def user_input(self):
        return self.game_state.user_input
    
    def get_draw_details(self) -> consts.DrawDetails:
        return consts.DrawDetails.NONE
    
    @abstractmethod # Das ist eine abstrakte Methode, also eine von den erwähnten, nicht implementierten Methoden.
    def draw(self, canvas: Canvas) -> None:
        pass
    
    @abstractmethod
    def update(self) -> None:
        pass