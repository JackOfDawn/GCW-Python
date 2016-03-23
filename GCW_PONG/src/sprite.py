#! /usr/bin/env python
__author__ = 'Joshua'
import pygame
import os


class Sprite:
    def __init__(self, x, y, image_path, layer=0):
        self.x = x
        self.y = y
        self.rot = 0
        self.active = True
        self.image_path = image_path
        self.layer = layer
        self.image = pygame.image.load(os.path.dirname(__file__) + "/../assets/" + image_path)
        self.rect = self.image.get_rect()
        self.width = self.rect.size[0]
        self.height = self.rect.size[1]
        self.halfWidth = self.width/2
        self.halfHeight = self.height/2

    def __str__(self):
        return "Sprite at " + str(self.x) + " " + str(self.y)

    # noinspection PyMethodMayBeStatic
    def update(self, delta_time):
        return

    def render(self, display_surf):
        self.image = pygame.transform.rotate(self.image, self.rot)
        display_surf.blit(self.image, (self.x - self.width/2, self.y - self.height/2))

    def getRect(self):
        return pygame.Rect(self.x - self.halfWidth, self.y - self.halfHeight, self.width, self.height)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getPosition(self):
        return [self.x, self.y]

    def setPosition(self, newPos):
        self.x = newPos[0]
        self.y = newPos[1]

    def set_active(self, active):
        self.active = active

    def get_active(self):
        return  self.active
