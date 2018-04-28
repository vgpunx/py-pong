import pygame
from constants import *
from pygame.math import Vector2 as vec


class Ball(pygame.sprite.Sprite):
    # ball sprite
    def __init__(self, bounds):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(pygame.Color('WHITE'))
        self.rect = self.image.get_rect()
        self.rect.center = PLAYFIELD_SIZE[0]/2, PLAYFIELD_SIZE[1]/2
        self.bounds = bounds

        # Position (start in the middle of the screen)
        self.pos = vec(self.rect.center[0], self.rect.center[1])
        # Angle (degrees)
        self.angle = 0.0
        # Speed - in pixels
        self.speed = 0
        # Velocity - I believe this is a placeholder for update() method
        self.vel = vec(1, 0).rotate(self.angle) * self.speed

    def bounce(self, pos):
        bounce = False

        # create a temporary rect for boundary testing
        test_rect = self.rect
        test_rect.center = pos

        # top and bottom boundary bouncing
        if test_rect.top <= self.bounds.top or test_rect.bottom >= self.bounds.bottom:
            norm = vec(0, 1)
            bounce = True

        # left and right boundary bouncing for test purposes
        elif test_rect.left <= self.bounds.left or test_rect.right >= self.bounds.right:
            norm = vec(1, 0)
            bounce = True

        if bounce:
            pos += self.vel.reflect(norm)

        return pos

    def move(self):
        # predictive check
        new_pos = self.pos + self.vel
        return new_pos

    def update(self):
        # predictive check
        # self.move() returns a new vector based on self.pos + self.vel
        # this method assumes that bounce() is handling the boundary
        # or collision check either internally or by calling another
        # function

        # Check for space bar
        # TODO: Add a flag to check for currently in play before releasing the ball.
        # Probably want to turn this part into its own method.
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            self.angle = 45
            self.speed = 3

        # TODO: Create and implement a read-ahead algorithm that constantly checks for the position on the next cycle
        # (cont'd) and decides if bounce, out-of-bounds, or if collision with paddle occurs based on that logic.

        # check for bounce/collision
        # update the position of the ball based on the velocity
        self.pos = self.bounce(self.move())     # Change to self.bounce(self.move()) after creation
        # update the actual position of the rect based on the stored position
        self.rect.center = self.pos
