#! /usr/bin/env python
__author__ = 'Jack Storm'
import sys
import pygame
from engine import Engine
from text import Text
from ball import Ball
from Paddle import Paddle
from soundEffect import soundEffect
from musicPlayer import musicPlayer


class Pong(Engine):
    def __init__(self):
        Engine.__init__(self, 320, 240, (00, 150, 150))
        self.fps_text = None
        self.scoreP1_text = None
        self.scoreP1 = 0
        self.scoreP2_text = None
        self.scoreP2 = 0
        self.ball = None
        self.playerOne = None
        self.playerTwo = None
        self.fps_update = 0
        self.fps_count = 0

        self.sfx_beep = None
        self.sfx_padOne = None
        self.sfx_padTwo = None
        self.music_bg = None

        self.winner_text = None
        self.start_game_text = None
        self.max_score = 7

    def on_init(self):
        Engine.on_init(self)

        self.winner_text = Text(self.width/4, 80, str(""), 30)
        self.add(self.winner_text)
        self.start_game_text = Text(self.width/3, 120, str("Press START"), 30)
        self.add(self.start_game_text)

        self.scoreP1_text = Text(self.width/4, 30, str(self.scoreP1), 50)
        self.scoreP2_text = Text(self.width - self.width/4, 30, str(self.scoreP2), 50)
        self.add(self.scoreP1_text)
        self.add(self.scoreP2_text)

        self.fps_text = Text(280, 220, "30")
        self.add(self.fps_text)
        self.ball = Ball(self.width/2, self.height/2, "ball.png")
        self.add(self.ball)
        self.playerOne = Paddle(20, self.height/2, "paddle.png")
        self.add(self.playerOne)
        self.playerTwo = Paddle(320 - 20, self.height/2, "paddle.png")
        self.add(self.playerTwo)

        self.sfx_padOne = soundEffect("blip1.wav")
        self.sfx_padTwo = soundEffect("blip2.wav")
        self.music_bg = musicPlayer("UGH1.wav", -1)
        self.music_bg.play()

        self.start_game(False)

    def start_game(self, active):
        self.fps_text.set_active(active)
        self.scoreP1_text.set_active(active)
        self.scoreP1 = 0
        self.scoreP2_text.set_active(active)
        self.scoreP2 = 0
        self.ball.set_active(active)
        self.playerOne.set_active(active)
        self.playerTwo.set_active(active)
        self.fps_update = 0
        self.fps_count = 0
        self.start_game_text.set_active(not active)
        self.winner_text.set_active(not active)

    def show_end_game(self):
        self.ball.set_active(False)
        self.playerOne.set_active(True)
        self.playerTwo.set_active(True)
        self.fps_update = 0
        self.fps_count = 0
        self.winner_text.set_active(True)
        self.start_game_text.set_active(True)
        if self.scoreP1 > self.scoreP2:
            self.winner_text.set_text("Player 1 Wins")
        else:
            self.winner_text.set_text("Player 2 Wins")

    def update(self, delta_time):
        self.fps_update += 1
        self.fps_count += self.delta_time
        if self.fps_update >= 20:
            self.fps_count /= 20
            self.fps_text.set_text(str(int(1.0/(float(self.fps_count)/1000))))
            self.fps_count = 0
            self.fps_update = 0
        self.handleInput()

        if self.scoreP1 == self.max_score or self.scoreP2 == self.max_score:
            self.show_end_game()
        else:
            self.checkCollision()

    def checkCollision(self):
        if self.ball.checkCollision(self.playerOne.getRect()):
            self.sfx_padOne.play_sound()
            self.ball.negateXVel()
        if self.ball.checkCollision(self.playerTwo.getRect()):
            self.sfx_padTwo.play_sound()
            self.ball.negateXVel()
        # p2 scores
        if self.ball.getX() < 0:
            self.ball.setPosition([self.width/2, self.height/2])
            self.ball.negateXVel()
            self.scoreP2 += 1
            self.scoreP2_text.set_text(str(self.scoreP2))

        # p1 scores
        if self.ball.getX() > self.width:
            self.ball.setPosition([self.width/2, self.height/2])
            self.ball.negateXVel()
            self.scoreP1 += 1
            self.scoreP1_text.set_text(str(self.scoreP1))

    def handleInput(self):
        # quitting
        if pygame.key.get_pressed()[pygame.K_ESCAPE] != 0:
            sys.exit()

        if pygame.key.get_pressed()[pygame.K_RETURN] != 0:
            self.start_game(True)
        # playerone
        if pygame.key.get_pressed()[pygame.K_UP] != 0:
            self.playerOne.setVelocity([0, -.2])
        elif pygame.key.get_pressed()[pygame.K_DOWN] != 0:
            self.playerOne.setVelocity([0, .2])
        else:
            self.playerOne.setVelocity([0, 0])

        # playertwo
        if pygame.key.get_pressed()[pygame.K_SPACE] != 0:
            self.playerTwo.setVelocity([0, -.2])
        elif pygame.key.get_pressed()[pygame.K_LALT] != 0:
            self.playerTwo.setVelocity([0, .2])
        else:
            self.playerTwo.setVelocity([0, 0])
        # resetgame
        # startball




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
