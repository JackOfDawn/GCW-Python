#! /usr/bin/env python
__author__ = 'Jack'
import pygame
from sprite import Sprite


class Ball(Sprite):
    def __init__(self, x, y, image_path):
        Sprite.__init__(self, x, y, image_path)
        self.vel = [.05, .1]

    def update(self, delta_time):
        self.x += self.vel[0] * delta_time
        self.y += self.vel[1] * delta_time

        if self.rect.top + self.y - self.halfHeight< 0 or self.rect.bottom + self.y - self.halfWidth > 240:
            self.vel[1] = -self.vel[1]
        if self.rect.left - self.halfWidth + self.x < 0 or self.rect.right - self.halfWidth + self.x > 320:
            self.vel[0] = -self.vel[0]
        return

