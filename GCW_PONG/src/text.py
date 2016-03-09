#! /usr/bin/env python

import pygame
from sprite import Sprite


class Text(Sprite):
    def __init__(self, x, y, text, size=30, font_name=None, layer=0):
        self.x = x
        self.y = y
        self.layer = layer
        self.color = (255, 255, 255)
        self.font = pygame.font.Font(font_name, size)
        self.text = self.font.render(text, False, self.color)

    def render(self, display_surf):
        display_surf.blit(self.text, (self.x, self.y))

    def set_text(self, text="Test"):
        self.text = self.font.render(text, False, self.color)

    def update(self, delta_time):
        return
