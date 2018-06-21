from constants import *
from ball import *
from paddle import *
from pygame.math import Vector2 as vec


class Playfield:
    def __init__(self, size):
        self.size = size
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()

        # Instantiate game objects
        self.ball = Ball(self.rect)
        self.paddle1 = Paddle(20, PLAYFIELD_SIZE[1]/2)
        self.paddle2 = Paddle(PLAYFIELD_SIZE[0]-20, PLAYFIELD_SIZE[1]/2)

        # Position of the playfield based on DISPLAY_SIZE.
        self.position = ((DISPLAY_SIZE[0] - PLAYFIELD_SIZE[0]) / 2, DISPLAY_SIZE[1] - ((DISPLAY_SIZE[0] - PLAYFIELD_SIZE[0]) / 2) - PLAYFIELD_SIZE[1])

        self.paddles = pygame.sprite.Group(self.paddle1, self.paddle2)
        self.all_sprites = pygame.sprite.Group(self.ball, self.paddles)

        self.background = pygame.Surface(size)

        # I see a Playfield and I want it painted black
        self.background.fill(pygame.Color('BLACK'))

        pygame.draw.rect(self.background, pygame.Color('WHITE'), self.rect, 5)
        pygame.draw.line(self.background, pygame.Color('WHITE'), self.rect.midtop, self.rect.midbottom, 1)

        self.image.blit(self.background, self.rect.topleft)

        self.p1_point_event = pygame.USEREVENT + 1
        self.p2_point_event = pygame.USEREVENT + 2

    def process_collision(self):
        # TODO: This method will handle all sprite collision in the game, and use ball.bounce to process bouncing.
        # Top and bottom boundary bouncing
        if self.ball.rect.top <= self.rect.top or self.ball.rect.bottom >= self.rect.bottom:
            self.ball.bounce(vec(1, 0))
            return

        # Left and right boundary handling
        elif self.ball.rect.right >= self.rect.right:
            self.ball.set_start_angle(50)   # Set the start angle
            self.ball.reset_pos()
            pygame.event.post(pygame.event.Event(self.p1_point_event))
            return

        elif self.ball.rect.left <= self.rect.left:
            self.ball.set_start_angle(130)
            self.ball.reset_pos()
            pygame.event.post(pygame.event.Event(self.p2_point_event))
            return

        # Handle collision with paddle
        collision_list = pygame.sprite.spritecollide(self.ball, self.paddles, False)

        if collision_list:
            # Get the location of the ball at the time of collision
            ball_coll_vec = self.ball.get_location()
            # print("Ball collided at: ", ball_coll_vec[0], ", ", ball_coll_vec[1])

            # Get the location of the paddle that was collided with
            if self.paddle1 in collision_list:
                paddle_bounce_angle = 360
                paddle_coll_vec = self.paddle1.get_location()   # Get the location of the paddle (center)
                # print("Paddle1 collision at: ", paddle_coll_vec[0], ", ", paddle_coll_vec[1])   # debug code

            elif self.paddle2 in collision_list:
                paddle_bounce_angle = 180
                paddle_coll_vec = self.paddle2.get_location()
                # print("Paddle2 collision at: ", paddle_coll_vec[0], ", ", paddle_coll_vec[1])

            # Angle is 0 degrees is right, 90 is down, 180 is left and 270 is up
            coll_diff = paddle_coll_vec[1] - ball_coll_vec[1]

            angle_offset = coll_diff * (90 / PADDLE_HEIGHT)
            if paddle_bounce_angle == 360:
                paddle_bounce_angle -= angle_offset
            if paddle_bounce_angle == 180:
                paddle_bounce_angle += angle_offset

            self.ball.set_angle(paddle_bounce_angle)
            self.ball.increase_speed()

            # self.ball.bounce(vec(0, 1))

    def draw(self, surface):
        self.all_sprites.clear(self.image, self.background)

        self.all_sprites.draw(self.image)

        # blit from self.image to self.position
        surface.blit(self.image, self.position)

    def update(self):
        self.process_collision()
        self.all_sprites.update()
