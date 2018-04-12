from constants import *


# This is the paddle class.
class Player1(pygame.sprite.Sprite):
    # paddle sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))  # What the sprite looks like
        self.image.fill(pygame.Color("green"))  # fill the Surface with the color Green
        self.rect = self.image.get_rect()   # The rectangle that encloses the sprite
        self.rect.center = (20, HEIGHT/2)
        self.speedy = 0

    def update(self):
        # Set speed to 0
        self.speedy = 0

        # main controls code
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:    # player1 up
            self.speedy = -5
        if keystate[pygame.K_s]:    # player1 down
            self.speedy = 5

        # set speed on each update
        self.rect.y += self.speedy

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
