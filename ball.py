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

    def bounce(self, vel):
        bounce = False

        # top and bottom boundary bouncing
        if self.rect.top <= self.bounds.top or self.rect.bottom >= self.bounds.bottom:
            norm = vec(0, 1)
            bounce = True

        # left and right boundary bouncing for test purposes
        elif self.rect.left <= self.bounds.left or self.rect.right >= self.bounds.right:
            norm = vec(1, 0)
            bounce = True

        if bounce:
            vel = vel.reflect(norm)
            return vel
        else:
            return vel

    def move(self):
        # predictive check
        return self.pos + self.vel

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
            self.vel = vec(-2, 2)

        # TODO: Create and implement a read-ahead algorithm that constantly checks for the position on the next cycle
        # (cont'd) and decides if bounce, out-of-bounds, or if collision with paddle occurs based on that logic.

        # check for bounce/collision
        # update the position of the ball based on the velocity
        self.pos += self.bounce(self.move())     # Change to self.bounce(self.move()) after creation
        # update the actual position of the rect based on the stored position
        self.rect.center = self.pos
