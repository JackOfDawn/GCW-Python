#! /usr/bin/env python
__author__ = 'Jack'
from sprite import Sprite


class Paddle(Sprite):
    def __init__(self, x, y, image_path):
        Sprite.__init__(self, x, y, image_path)
        self.vel = [0.0, 0.0]

    def update(self, delta_time):
        self.x += self.vel[0] * delta_time
        self.y += self.vel[1] * delta_time

        if self.rect.top + self. y - self.halfHeight < 0:
            self.y = self.halfHeight
        if self.rect.bottom + self.y - self.halfHeight > 240:
            self.y = 240 - self.halfHeight

    def setVelocity(self, newVel):
        self.vel = newVel
