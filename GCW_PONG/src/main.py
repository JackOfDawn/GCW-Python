#! /usr/bin/env python

import sys
import pygame

pygame.init()

size = width, height = 320, 240
speed = [1, 1]
screenColor = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("../assets/ball.png")
ballrect = ball.get_rect()

pygame.mouse.set_visible(False)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if pygame.key.get_pressed()[pygame.K_LALT] != 0:
        sys.exit()
    if pygame.key.get_pressed()[pygame.K_LCTRL] != 0:
        screenColor = 0, 255, 0
    if pygame.key.get_pressed()[pygame.K_LSHIFT] != 0:
        screenColor = 0, 0, 255
    if pygame.key.get_pressed()[pygame.K_SPACE] != 0:
        screenColor = 0, 0, 0

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(screenColor)
    screen.blit(ball, ballrect)
    pygame.display.flip()
