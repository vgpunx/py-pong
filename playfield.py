import os
from ball import *
from paddle import *
from pygame.math import Vector2 as vec


class Playfield:
    def __init__(self, size):
        """
        :param size: tuple
        """
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

        # Track player score
        self.p1_score = 0
        self.p2_score = 0

        # Sound
        self._sound_wall = pygame.mixer.Sound(os.path.join(os.path.curdir, 'sfx', 'ping_pong_8bit_plop.wav'))
        self._sound_padl = pygame.mixer.Sound(os.path.join(os.path.curdir, 'sfx', 'ping_pong_8bit_beeep.wav'))
        self._sound_goal = pygame.mixer.Sound(os.path.join(os.path.curdir, 'sfx', 'ping_pong_8bit_peeeeeep.wav'))

    def process_collision(self):
        # Top and bottom boundary bouncing
        if self.ball.rect.top <= self.rect.top or self.ball.rect.bottom >= self.rect.bottom:
            self._sound_wall.play()
            self.ball.bounce(vec(1, 0))
            return

        # Left and right boundary handling
        elif self.ball.rect.right >= self.rect.right:
            self.ball.set_start_angle(50)   # Set the start angle for p2 to serve
            self.ball.reset_pos()
            self.p1_score += 1
            pygame.event.post(pygame.event.Event(self.p1_point_event))
            self._sound_goal.play()
            return

        elif self.ball.rect.left <= self.rect.left:
            self.ball.set_start_angle(130)  # Set the start angle for p1 to serve
            self.ball.reset_pos()
            self.p2_score += 1
            pygame.event.post(pygame.event.Event(self.p2_point_event))
            self._sound_goal.play()
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

            # Set the angle of the ball and increment its speed
            self.ball.set_angle(paddle_bounce_angle)
            self.ball.increase_speed()
            self._sound_padl.play()

    def draw(self, surface):
        self.all_sprites.clear(self.image, self.background)
        self.all_sprites.draw(self.image)
        surface.blit(self.image, self.position)

    def update(self):
        # reset player score if it advances beyond 99
        if self.p1_score > 99:
            self.p1_score = 0
        elif self.p2_score > 99:
            self.p2_score = 0

        self.process_collision()
        self.all_sprites.update()
