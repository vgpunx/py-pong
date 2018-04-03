from constants import *
vec = pygame.math.Vector2


class Ball(pygame.sprite.Sprite):
    # ball sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(pygame.Color("white"))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

        # Position (start in the middle of the screen)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        # Velocity
        self.vel = vec(0, 0)
        # Acceleration
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, 0)

        started = False
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE] and not started:
            self.acc.x = -0.5
            self.acc.y = 0.5
            started = True

        # check for collision with a wall
        if self.pos.y < 0:
            self.pos.y = 0 + 1
            self.vel.y -= (self.vel.y * 2)
        if self.pos.y > HEIGHT:
            self.pos.y = HEIGHT - 1
            self.vel.y -= (self.vel.y * 2)

        self.vel += self.acc
        self.pos += self.vel + (0.5 * self.acc)

        self.rect.center = self.pos
