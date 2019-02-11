import pygame
import math, random
from pygame.sprite import Sprite
from explosion import Explosion


class Expend(Sprite):
    """烟花爆炸"""

    def __init__(self, ai_settings, screen, theat, color):
        super().__init__()
        self.screen = screen
        self.explosion = Explosion(ai_settings, screen, color)

        # 爆照的位置
        self.rect = pygame.Rect(0, 0, ai_settings.expend_size_width,
                                ai_settings.expend_size_height)
        self.rect.centerx = float(self.explosion.rect.centerx)
        self.rect.centery = float(self.explosion.y_max)

        self.color = color
        self.theat = theat
        self.speed = random.choice(ai_settings.expend_v)

    def update(self, ai_settings):
        """360°发射"""
        self.move_x = math.cos(self.theat * 2 * math.pi / ai_settings.tho) * self.speed
        self.move_y = math.sin(self.theat * 2 * math.pi / ai_settings.tho) * self.speed
        self.rect.centerx += self.move_x
        self.move_y -= ai_settings.GRIVITY
        self.rect.y += self.move_y
        if self.speed > 0:
            self.speed -= 1

    def draw_round_fire(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
