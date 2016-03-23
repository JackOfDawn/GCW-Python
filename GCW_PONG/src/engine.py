#! /usr/bin/env python
__author__ = 'Joshua'
import pygame
import sys

ENGINE = None


def get_current():
    return ENGINE


class Engine:
    def __init__(self, width, height, color=(255, 192, 192)):
        global ENGINE
        ENGINE = self
        print ENGINE

        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = width, height
        self.game_color = color
        self.sprites = []
        self.listeners = []
        self.clock = pygame.time.Clock()
        self.frame_rate = 60
        self._cur_ticks = 0
        self.delta_time = 0

    def on_init(self):
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=256)
        pygame.init()
        pygame.display.set_caption('Pyng')
        self._display_surf = pygame.display.set_mode(self.size)
        pygame.draw.rect(self._display_surf, (255, 0, 0), (0, 0, 320, 240))
        pygame.mouse.set_visible(False)

    def handle_event(self, event):
        for listener in self.listeners:
            if event.type == listener[0]:
                listener[1](event)
        if event.type == pygame.QUIT:
            self._running = False

    def execute(self):
        """Core game loop"""
        self.on_init()
        while self._running:
            self.delta_time = self.clock.tick(self.frame_rate)
            self.update(self.delta_time)
            self._display_surf.fill(self.game_color)
            for event in pygame.event.get():
                self.handle_event(event)
            for spr in self.sprites:
                if spr.get_active() == True:
                    spr.update(self.delta_time)
                    spr.render(self._display_surf)
            pygame.display.update()

        pygame.quit()
        sys.exit()

    def update(self, delta_time):
        return

    def add(self, sprite):
        """ Adds sprite to render list, sorts list """
        self.sprites.append(sprite)
        self.sprites = sorted(self.sprites, key=lambda spr: spr.layer)

    def register_listener(self, event_type, listener_function):
        self.listeners.append((event_type, listener_function))


