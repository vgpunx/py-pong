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
        self.rect.center = (PLAYFIELD_SIZE[0]/2, PLAYFIELD_SIZE[1]/2)
        self.bounds = bounds

        # Position (start in the middle of the screen)
        self.pos = self.rect.center
        # Angle (degrees)
        self.angle = 0.0
        # Speed - in pixels
        self.speed = 0
        # Velocity - I believe this is a placeholder for update() method
        self.vel = vec(1, 0).rotate(self.angle) * self.speed

    def bounce(self, pos, vel):
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
            self.vel = self.vel.reflect(norm)
            # self.move(self.vel)

    def update(self):
        # Check for spacebar
        # TODO: Add a flag to check for currently in play before releasing the ball.
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            self.vel = (-2, 2)

        # TODO: Implement ball.bounce() using Vector2
        # if self.pos.y < 0:
        #    self.pos.y = 0 + 1
        #    self.vel.y -= (self.vel.y * 2)
        # if self.pos.y > PLAYFIELD_SIZE[1]:
        #    self.pos.y = PLAYFIELD_SIZE[1] - 1
        #    self.vel.y -= (self.vel.y * 2)

        # TODO: Implement bounce() here to check for collision with walls
        self.pos += self.vel

        self.rect.center = self.pos
