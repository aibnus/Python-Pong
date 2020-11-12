import pygame, sys, random
from src.constant import WIDTH, HEIGHT, light_grey, BG, SPEED
from src.player import Player
from src.opponent import Opponent
from src.ball import Ball
from src.game import Game

#pygame initiation
clock = pygame.time.Clock()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
strip = pygame.Rect(WIDTH//2 - 2, 0, 4, HEIGHT)

#set the game objects
player = Player('assets/Paddle.png', WIDTH - 20, HEIGHT//2, SPEED)
opponent = Opponent('assets/Paddle.png', 20, WIDTH//2, 5)
paddle_group = pygame.sprite.Group()
paddle_group.add(player)
paddle_group.add(opponent)

ball = Ball('assets/Ball.png', WIDTH//2, HEIGHT//2, 4,4, paddle_group)
ball_sprite = pygame.sprite.GroupSingle()
ball_sprite.add(ball)

game = Game(WIN, ball_sprite, paddle_group)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.movement += player.speed
            if event.key == pygame.K_UP:
                player.movement -= player.speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player.movement -= player.speed
            if event.key == pygame.K_UP:
                player.movement += player.speed

    WIN.fill(BG)
    pygame.draw.rect(WIN, light_grey, strip)

    game.run()

    pygame.display.update()
    clock.tick(60)