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

        self.paddles = pygame.sprite.Group(self.paddle1, self.paddle2)
        self.all_sprites = pygame.sprite.Group(self.ball, self.paddles)

    def process_collision(self):
        # TODO: This method will handle all sprite collision in the game, and use ball.bounce to process bouncing.
        # Top and bottom boundary bouncing
        if self.ball.rect.top <= self.rect.top or self.ball.rect.bottom >= self.rect.bottom:
            self.ball.bounce(vec(1, 0))
            return

        # This block implements left and right boundary bouncing for test purposes only and should be removed.
        elif self.ball.rect.right >= self.rect.right or self.ball.rect.left <= self.rect.left:
            self.ball.bounce(vec(0, 1))
            return

        # Handle collision with paddle
        collision_list = pygame.sprite.spritecollide(self.ball, self.paddles, False)

        if collision_list:
            # Get the location of the ball at the time of collision
            ball_coll_vec = self.ball.get_location()
            print("Ball collided at: ", ball_coll_vec[0], ", ", ball_coll_vec[1])

            # Get the location of the paddle that was collided with
            if self.paddle1 in collision_list:
                paddle_coll_vec = self.paddle1.get_location()   # Get the location of the paddle (center)
                print("Paddle1 collision at: ", paddle_coll_vec[0], ", ", paddle_coll_vec[1])   # debug code

            elif self.paddle2 in collision_list:
                paddle_coll_vec = self.paddle2.get_location()
                print("Paddle2 collision at: ", paddle_coll_vec[0], ", ", paddle_coll_vec[1])

            # Divide the paddle into 3 pieces and determine where the ball hit on the paddle.
            paddle_top = paddle_coll_vec[1] - (PADDLE_HEIGHT / 2)
            paddle_mid_top = paddle_top - paddle_coll_vec[1]
            paddle_bot = paddle_coll_vec[1] + (PADDLE_HEIGHT / 2)
            paddle_mid_bot = paddle_bot + paddle_coll_vec[1]

            print("top: ", paddle_top)
            print("mid-top: ", paddle_mid_top)
            print("mid_bot: ", paddle_mid_bot)
            print("bot: ", paddle_bot)

            self.ball.bounce(vec(0, 1))
            # for spr in collision_list:
            #     self.ball.bounce(vec(0, 1))
            #     break

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
