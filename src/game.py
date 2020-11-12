import pygame
from .constant import WIDTH, HEIGHT, FONT, light_grey

class Game:
    def __init__(self, win, ball_group, paddle_group):
        self.player_score = 0
        self.opponent_score = 0
        self.ball_group = ball_group
        self.paddle_group = paddle_group
        self.win = win

    def run(self):
        #draw game objects
        self.paddle_group.draw(self.win)
        self.ball_group.draw(self.win)

        #update game objects
        self.paddle_group.update(self.ball_group)
        self.ball_group.update(self.win)
        self.reset_ball()
        self.draw_score()

    def reset_ball(self):
        if self.ball_group.sprite.rect.right >= WIDTH:
            self.opponent_score += 1
            self.ball_group.sprite.reset()
        if self.ball_group.sprite.rect.left <= 0:
            self.player_score += 1
            self.ball_group.sprite.reset()

    def draw_score(self):
        player_score = FONT.render(str(self.player_score), True, light_grey)
        opponent_score = FONT.render(str(self.opponent_score), True, light_grey)

        player_score_rect = player_score.get_rect(midleft = (WIDTH//2 + 40, HEIGHT//2))
        opponent_score_rect = opponent_score.get_rect(midright = (WIDTH//2 - 40, HEIGHT//2))

        self.win.blit(player_score, player_score_rect)
        self.win.blit(opponent_score, opponent_score_rect)