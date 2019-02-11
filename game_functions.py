import pygame
import sys
from pygame.locals import *
from explosion import Explosion
from expend_fire import Expend
import random


def check_keydown(event, ai_settings, screen):
    """响应按下"""
    Fullscreen = False
    if event.key == pygame.K_f:
        Fullscreen = not Fullscreen
        if Fullscreen:
            screen = pygame.display.set_mode((
                ai_settings.screen_width, ai_settings.screen_height), FULLSCREEN, 32)
        else:
            screen = pygame.display.set_mode((
                ai_settings.screen_width, ai_settings.screen_height), 0, 32)
    if event.key == pygame.K_q:
        sys.exit()


def check_events(ai_settings, screen, fire, expend):
    """响应按键和鼠标"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ai_settings, screen)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_mouse(ai_settings, screen, fire, expend)


def update_screen(ai_settings, screen, fire, expend):
    # 更新图像，刷新屏幕
    screen.fill(ai_settings.bg_color)
    for fir in fire.sprites():
        fir.draw_fire()
    for expends in expend.sprites():
        expends.draw_round_fire()
    pygame.display.flip()


def launch(ai_settings, screen, fire, expend):
    """创建一个火焰，加入编组"""
    color = random.choice(ai_settings.fire_color)
    new_fire = Explosion(ai_settings, screen, color)
    fire.add(new_fire)
    for theat in range(ai_settings.tho):
        new_expend = Expend(ai_settings, screen, theat, color)
        expend.add(new_expend)


def check_mouse(ai_settings, screen, fire, expend):
    """响应鼠标点击"""
    pressed_array = pygame.mouse.get_pressed()
    for index in range(len(pressed_array)):
        if pressed_array[index]:
            if index == 0:
                launch(ai_settings, screen, fire, expend)


def update_fire(ai_settings, fire, expend):
    """更新火焰的位置"""
    fire.update(ai_settings)
    expend.update(ai_settings)
    # 删除到达鼠标点的子弹
    for fir in fire.copy():
        if fir.y <= fir.y_max:
            fire.remove(fir)
    for expen in expend.copy():
        if expen.speed == 0:
            expend.remove(expen)
