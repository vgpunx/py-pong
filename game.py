from scoreboard import *


class Game:
    def __init__(self):
        pygame.init()

        # Set the width and height of the screen [width, height)
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)

        # Title bar text
        pygame.display.set_caption("PyPong")

        # Main game loop conditional
        self.done = False

        # Screen update
        self.clock = pygame.time.Clock()

        # Instantiate objects
        self.playfield = Playfield(PLAYFIELD_SIZE)
        self.scoreboard = Scoreboard(PLAYFIELD_SIZE)

    def run(self):
        # Main game loop
        while not self.done:
            # main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                elif event.type == self.playfield.p1_point_event:
                    self.scoreboard.p1_point()
                elif event.type == self.playfield.p2_point_event:
                    self.scoreboard.p2_point()

            pygame.event.pump()

            # I see a white screen and I want it painted black
            self.screen.fill(BLACK)

            # draw the playfield to the screen
            self.playfield.update()
            self.playfield.draw(self.screen)

            self.scoreboard.draw(self.screen)

            # Input checks
            # Check for player 1 inputs
            key_state = pygame.key.get_pressed()
            if key_state[pygame.K_w]:
                self.playfield.paddle1.move_up()
            if key_state[pygame.K_s]:
                self.playfield.paddle1.move_down()

            # Check for player 2 inputs
            if key_state[pygame.K_UP]:
                self.playfield.paddle2.move_up()
            if key_state[pygame.K_DOWN]:
                self.playfield.paddle2.move_down()

            # Check for space bar to start the round if needed
            if key_state[pygame.K_SPACE] and not self.playfield.ball.in_play:
                self.playfield.ball.start_round()

            # Update the screen with the draw
            pygame.display.flip()

            # Limit to 60 FPS
            self.clock.tick(60)