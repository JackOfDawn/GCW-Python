#! /usr/bin/env python
__author__ = 'Jack Storm'
import sys
import pygame
from engine import Engine
from text import Text
from ball import Ball


class Pong(Engine):
    def __init__(self):
        Engine.__init__(self, 320, 240, (00, 150, 150))
        self.fps_text = None
        self.scoreP1_text = None
        self.scoreP2_text = None
        self.ball = None
        self.fps_update = 0
        self.fps_count = 0

    def on_init(self):
        Engine.on_init(self)
        self.fps_text = Text(280, 220, "30")
        self.add(self.fps_text)
        self.ball = Ball(self.width/2, self.height/2, "ball.png")
        self.add(self.ball)

    def update(self, delta_time):
        self.fps_update += 1
        self.fps_count += self.delta_time
        if self.fps_update >= 20:
            self.fps_count /= 20
            self.fps_text.set_text(str(int(1.0/(float(self.fps_count)/1000))))
            self.fps_count = 0
            self.fps_update = 0
        if pygame.key.get_pressed()[pygame.K_LALT] != 0:
            sys.exit()


Pong().execute()


# pygame.init()
#
# size = width, height = 320, 240
# speed = [1, 1]
# screenColor = 0, 0, 0
#
# screen = pygame.display.set_mode(size)
#
# ball = pygame.image.load("../assets/ball.png")
# ballrect = ball.get_rect()
#
# pygame.mouse.set_visible(False)
#
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#     if pygame.key.get_pressed()[pygame.K_LALT] != 0:
#         sys.exit()
#     if pygame.key.get_pressed()[pygame.K_LCTRL] != 0:
#         screenColor = 0, 255, 0
#     if pygame.key.get_pressed()[pygame.K_LSHIFT] != 0:
#         screenColor = 0, 0, 255
#     if pygame.key.get_pressed()[pygame.K_SPACE] != 0:
#         screenColor = 0, 0, 0
#
#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#         speed[1] = -speed[1]
#
#     screen.fill(screenColor)
#     screen.blit(ball, ballrect)
#     pygame.display.flip()
