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
        self.rect.center = bounds[2] / 2, bounds[3] / 2
        self.bounds = bounds

        # Flag to let the game know when the ball is in play so a round can be started with SPACE
        self.in_play = False

        # Position (start in the middle of the screen)
        self.pos = vec(self.rect.center[0], self.rect.center[1])
        # Angle (degrees)
        self.angle = 0.0
        # Speed - in pixels
        self.speed = 0
        # Velocity - I believe this is a placeholder for update() method
        self.vel = vec(1, 0).rotate(self.angle) * self.speed

    # TODO: Playfield should call this method to reflect the ball when it collides with a paddle.
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
            # new direction
            self.vel = self.vel.reflect(norm)
            # new angle property
            self.angle = self.vel.angle_to(vec(1, 0))  # Vector2(1, 0) has an angle of 0.0 deg
            # move in the new direction once this frame
            pos += self.vel

        return pos

    def set_speed(self, speed):
        self.speed = speed
        self.vel = vec(1, 0).rotate(self.angle) * speed

    def set_angle(self, angle):
        self.angle = angle
        self.vel = vec(1, 0).rotate(angle) * self.speed

    def move(self):
        # predictive check
        new_pos = self.pos + self.vel
        return new_pos

    def start_round(self):
        # Used to start the round when space is pressed
        self.set_speed(3)
        self.set_angle(135)
        self.in_play = True

    def update(self):
        # Check for collision on the upcoming move and branch based on collision
        self.pos = self.bounce(self.move())
        # Update the actual position of the ball based with the stored position data
        self.rect.center = self.pos
