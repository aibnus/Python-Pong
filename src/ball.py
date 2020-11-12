import pygame, random
from .constant import WIDTH, HEIGHT, PONG_SOUND, SCORE_SOUND, FONT, light_grey, BG
from .block import Block

class Ball(Block):
    def __init__(self, path, x, y, speed_x, speed_y, paddles):
        super().__init__(path, x, y)
        self.speed_x = speed_x * random.choice((-1, 1))
        self.speed_y = speed_y * random.choice((-1, 1))
        self.paddles = paddles
        self.active = False
        self.score_time = 0

    def update(self, win):
        self.win = win
        if self.active:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.collision()
        else:
            self.restart_counter()

    def collision(self):
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            pygame.mixer.Sound.play(PONG_SOUND)
            self.speed_y *= -1

        if pygame.sprite.spritecollide(self,self.paddles, False):
            pygame.mixer.Sound.play(PONG_SOUND)
            collission_paddle = pygame.sprite.spritecollide(self, self.paddles, False)[0].rect

            if abs(self.rect.right - collission_paddle.left) < 10 and self.speed_x > 0:
                self.speed_x *= -1
            if abs(self.rect.left - collission_paddle.right) < 10 and self.speed_x < 0:
                self.speed_x *= -1
            if abs(self.rect.bottom - collission_paddle.top) < 10 and self.speed_y > 0:
                self.speed_y *= -1
            if abs(self.rect.top - collission_paddle.bottom) < 10 and self.speed_y < 0:
                self.speed_y *= -1

    def reset(self):
        self.active = False
        self.speed_x *= random.choice((-1,1))
        self.speed_y *= random.choice((-1,1))

        self.score_time = pygame.time.get_ticks()
        self.rect.center = (WIDTH//2, HEIGHT//2)
        pygame.mixer.Sound.play(SCORE_SOUND)

    def restart_counter(self):
        current_time = pygame.time.get_ticks()
        countdown_number = 0

        if current_time - self.score_time < 700:
            countdown_number = 3
        elif current_time - self.score_time < 1400:
            countdown_number = 2
        elif current_time - self.score_time < 2100:
            countdown_number = 1
        else:
            self.active = True

        time_counter = FONT.render(str(countdown_number), True, light_grey)
        time_counter_rect = time_counter.get_rect(center = (WIDTH//2, HEIGHT//2 + 40))

        pygame.draw.rect(self.win, BG, time_counter_rect)
        self.win.blit(time_counter, time_counter_rect)