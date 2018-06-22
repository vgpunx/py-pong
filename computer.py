import pygame
import random
from pygame.locals import *
from constants import *


class ComputerPlayer:

    def __init__(self, playfield):
        # keep track of the ball
        self.__playfield = playfield

        # randomizer
        self.rng = random.Random()

        # timer
        self.limits = (180, 300)
        self.__timer = 0
        self.__limit = self.rng.randint(self.limits[0], self.limits[1])

        # logic
        # 0 is none, 1 is up, 2 is down
        self.__direction = self.rng.randint(0, 1)
        # 0 is false, 1 is true
        self.__playhard = self.rng.randint(0, 1)
        # self.__playhard = 1

    def update(self):
        if self.__timer >= self.__limit:
            self._decide_aggressive()

        self.__direction = self._decide_direction()

        # commit the movement.  we're always moving
        if self.__direction == 1:
            self.__playfield.paddle2.move_down()
        elif self.__direction == 0:
            self.__playfield.paddle2.move_up()

        self.__timer += 1

    def _decide_direction(self):
        direction = self.__direction

        if self.__playhard == 1:
            if self.__playfield.ball.rect.centery > self.__playfield.paddle2.rect.bottom:
                direction = 1
            elif self.__playfield.ball.rect.centery < self.__playfield.paddle2.rect.top:
                direction = 0
            else:
                direction = direction


        else:
        # if we hit the playfield edge
            if self.__playfield.paddle2.rect.top <= self.__playfield.rect.top:
                direction = 1
            elif self.__playfield.paddle2.rect.bottom >= self.__playfield.rect.bottom:
                direction = 0

        return direction

    def _decide_aggressive(self):
        if self.__timer == self.limits[1]:
            self.__timer = 0
            self.__playhard = self.rng.randint(0, 1)
            self.__limit = self.rng.randint(self.limits[0], self.limits[1])
