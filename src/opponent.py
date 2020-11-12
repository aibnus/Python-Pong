import pygame
from .constant import HEIGHT
from .block import Block

class Opponent(Block):
    def __init__(self, path, x, y, speed):
        super().__init__(path, x, y)
        self.speed = speed

    def screen_constrain(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

    def update(self, ball_group):
        if self.rect.top < ball_group.sprite.rect.y:
            self.rect.y += self.speed
        if self.rect.bottom > ball_group.sprite.rect.y:
            self.rect.y -= self.speed

        self.screen_constrain()