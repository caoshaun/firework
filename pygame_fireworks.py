#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
author:Cao Shawn
一个python3和pygame实现的烟花，
有重力的因素，本来想火花减速上升至鼠标点击点后，烟花爆炸
结果无法实现，希望有一天能做出来吧
2019新年快乐
"""

import pygame
from settings import Settings
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始游戏，创建屏幕
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height), 0, 32)
    pygame.display.set_caption("Fireworks")
    clock = pygame.time.Clock()

    # 设置背景
    background = pygame.image.load(ai_settings.bg_image).convert()
    screen.blit(background, (0, 0))

    # 产生一个上升的火焰
    fire = Group()
    expend = Group()

    while True:
        gf.check_events(ai_settings, screen, fire, expend)
        gf.update_fire(ai_settings, fire, expend)
        # gf.launch_expend(ai_settings, screen, fire, expend)
        # gf.update_expend_fire(ai_settings, screen, fire, expend)
        gf.update_screen(ai_settings, screen, fire, expend)
        clock.tick(24)


run_game()
