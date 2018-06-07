import pygame
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

    # Bounce the ball.
    def bounce(self, collision_vector):
        self.vel = self.vel.reflect(collision_vector.rotate(90).normalize())

    def get_location(self):
        return self.pos

    def get_rect(self):
        return self.rect

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
        self.set_speed(5)
        self.set_angle(130)
        self.in_play = True

    def update(self):
        # Check for collision on the upcoming move and branch based on collision
        self.pos = self.move()
        # Update the actual position of the ball based with the stored position data
        self.rect.center = self.pos
