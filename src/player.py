import pygame
from .block import Block
from .constant import HEIGHT

class Player(Block):
    def __init__(self, path, x, y, speed):
        super().__init__(path, x, y)
        self.speed = speed
        self.movement = 0

    def screen_constrain(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

    def update(self, ball_group):
        self.rect.y += self.movement
        self.screen_constrain()