from constants import *
from ball import *
from paddle import *
from pygame.math import Vector2 as vec


class Playfield:
    def __init__(self, size):
        self.size = size
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.ball = Ball(self.rect)
        self.paddle1 = Paddle(20, PLAYFIELD_SIZE[1]/2)
        self.paddle2 = Paddle(PLAYFIELD_SIZE[0]-20, PLAYFIELD_SIZE[1]/2)

        # Position of the playfield based on DISPLAY_SIZE.
        self.position = ((DISPLAY_SIZE[0] - PLAYFIELD_SIZE[0]) / 2, DISPLAY_SIZE[1] - ((DISPLAY_SIZE[0] - PLAYFIELD_SIZE[0]) / 2) - PLAYFIELD_SIZE[1])

        self.all_sprites = pygame.sprite.Group(self.ball, self.paddle1, self.paddle2)

    def process_collision(self):
        # TODO: This method will handle all sprite collision in the game, and use ball.bounce to process bouncing.
        if self.ball.rect.top <= self.rect.top or self.ball.rect.bottom >= self.rect.bottom:
            self.ball.bounce(vec(1, 0))
            return
        elif self.ball.rect.right >= self.rect.right or self.ball.rect.left <= self.rect.left:
            self.ball.bounce(vec(0, 1))
            return

    def draw(self, surface):
        # TODO: Draw a green line around the play field to visually show the play field boundaries
        self.image.fill(pygame.Color('BLACK'))
        self.update()
        self.all_sprites.draw(self.image)

        # blit from self.image to self.position
        surface.blit(self.image, self.position)

    def update(self):
        self.process_collision()
        self.all_sprites.update()
