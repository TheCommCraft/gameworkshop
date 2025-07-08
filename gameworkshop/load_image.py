from functools import cache
from pygame import Surface
from pygame.image import load

@cache
def load_image(path: str) -> Surface:
    return load(path)
