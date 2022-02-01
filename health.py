import pygame
from config import *


class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp, screen):
        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
