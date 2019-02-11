import random
import pygame
from pygame.sprite import Sprite
import game_functions as gf


class Explosion(Sprite):
    """管理爆炸和烟花"""

    def __init__(self, ai_settings, screen, color):
        """在鼠标点击的x位置创建上升的火花"""
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_settings

        # 在（0.0）处创建矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.fire_width, ai_settings.fire_height)
        self.rect.centerx, self.y_max = find_mouse()
        self.rect.top = screen.get_rect().bottom
        self.y = float(self.rect.y)

        # 初速度
        self.vo = (2*(screen.get_rect().bottom-self.y_max)*ai_settings.GRIVITY)**(1/2)

        # 随机的火焰颜色
        self.color = color
        # self.speed_factor = ai_settings.fire_speed

    def update(self, ai_settings):
        """上升的火焰"""
        if self.y > self.y_max:
            self.y -= self.vo
            self.vo -= ai_settings.GRIVITY
            self.rect.y = self.y

    def draw_fire(self):
        """画出火焰"""
        pygame.draw.rect(self.screen, self.color, self.rect)


def find_mouse():
    global xo, yo
    pressed_array = pygame.mouse.get_pressed()
    for index in range(len(pressed_array)):
        if pressed_array[index]:
            if index == 0:
                xo, yo = pygame.mouse.get_pos()
    return xo, yo
