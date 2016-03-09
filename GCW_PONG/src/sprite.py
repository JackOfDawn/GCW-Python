#! /usr/bin/env python
__author__ = 'Joshua'
import pygame
import os

class Sprite:
    def __init__(self, x, y, image_path, layer=0):
        self.x = x
        self.y = y
        self.rot = 0
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

