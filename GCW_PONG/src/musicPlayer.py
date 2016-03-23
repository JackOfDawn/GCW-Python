#! /usr/bin/env python
__author__ = 'Jack'

import pygame
import os


class musicPlayer:
    def __init__(self, music_path, loops):
        pygame.mixer.music.load(os.path.dirname(__file__) + "/../assets/" + music_path)
        self.loops = loops

    def play(self):
        pygame.mixer.music.play(self.loops)

    def stop(self):
        pygame.mixer.music.stop()


