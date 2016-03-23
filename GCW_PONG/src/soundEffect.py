#! /usr/bin/env python
__author__ = 'Jack'
import pygame
import os


class soundEffect:
    def __init__(self, sound_path):
        self.sound = pygame.mixer.Sound(os.path.dirname(__file__) + "/../assets/" + sound_path)

    def play_sound(self):
        self.sound.play()
