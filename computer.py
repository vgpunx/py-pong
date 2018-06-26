import random


class ComputerPlayer:

    def __init__(self, playfield, difficulty=0.75):
        # keep track of the playfield state
        self._playfield = playfield

        # random.Random().monty_python_quote()
        # "All right, but apart from the sanitation, medicine, education, wine, public order, irrigation, roads, the
        # fresh water system and public health, what have the Romans ever done for us?"
        self.rng = random.Random()

        # timers
        # this is used to govern how long to be in each state
        self.state_timer_minmax = (180, 500)
        self._state_timer = 0
        self._state_timer_limit = self.set_timer_limit(self.state_timer_minmax)

        # this is used to govern the duration of random paddle movements in passive state
        self.move_timer_minmax = (30, 120)
        self._move_timer = 0
        self._move_timer_limit = self.set_timer_limit(self.move_timer_minmax)

        # state
        # True = be a dick; False = fuck about
        self._start_difficulty = difficulty
        self.difficulty = difficulty
        self._aggressive_state = self._decide_state()

        # random movement direction
        # 0 = up; 1 = none; 2 = down
        self._random_move_direction = self._decide_direction()

    def __repr__(self):
        strings = (
            "--CPU Player--",
            "Difficulty level: {0}".format(self.difficulty),
            "Base difficulty level: {0}".format(self._start_difficulty),
            "Aggressive state: {0}".format(self._aggressive_state),
            "State limit: {0}".format(self._state_timer_limit),
            "Direction: {0}".format(self._random_move_direction)
        )

        return "\n".join(strings)

    def update(self):
        if self._state_timer >= self._state_timer_limit:
            self.difficulty = self._adapt_difficulty()
            self._state_timer = 0
            self._state_timer_limit = self.set_timer_limit(self.state_timer_minmax)
            self._aggressive_state = self._decide_state()

        if self._aggressive_state:
            self._move_aggressive(self._playfield.paddle2)
        else:
            self._move_random(self._playfield.paddle2)

        self._state_timer += 1

    def set_timer_limit(self, limits):
        """
        Returns a random integer value between two values supplied as a collection.
        :param limits: Tuple
        :return: Integer
        """
        return self.rng.randint(limits[0], limits[1])

    def _decide_state(self):
        """
        Returns a weighted random Boolean value.
        :return: Boolean
        """
        return random.choices([True, False], weights=[self.difficulty, 1.0 - self.difficulty])[0]

    def _decide_direction(self):
        """
        Returns a random integer between 0 and 2 representing 3 possible directions.
        :return: Integer
        """
        return self.rng.randint(0, 2)

    def _move_aggressive(self, paddle):
        """
        Moves a Paddle object in an aggressive manner to actively try to hit the ball.
        :param paddle: py-pong.paddle.Paddle
        :return: None
        """
        if self._playfield.ball.rect.centery > self._playfield.paddle2.rect.bottom:
            paddle.move_down()
            return None
        elif self._playfield.ball.rect.centery < self._playfield.paddle2.rect.top:
            paddle.move_up()
            return None

    def _move_random(self, paddle):
        """
        Causes a paddle object to move in a random direction for a random period of time within limits.
        :param paddle: py-pong.paddle.Paddle
        :return: None
        """
        # this is the fuckabout function
        self._move_timer += 1

        if self._move_timer >= self._move_timer_limit:
            self._move_timer_limit = self.set_timer_limit(self.move_timer_minmax)
            self._move_timer = 0
            self._random_move_direction = self._decide_direction()

        # turn around if we hit the sides
        if paddle.rect.top <= self._playfield.rect.top:
            self._random_move_direction = 2
        elif paddle.rect.bottom >= self._playfield.rect.bottom:
            self._random_move_direction = 0

        # commit the move
        if self._random_move_direction == 2:
            paddle.move_down()
            return None
        elif self._random_move_direction == 1:
            # this is only here to show that this is explicitly being handled
            return None
        elif self._random_move_direction == 0:
            paddle.move_up()
            return None

    def _adapt_difficulty(self):
        """
        Adjusts the probability weight used to select aggressive mode based on the score difference.
        :return: float
        """

        delta = self._playfield.p1_score - self._playfield.p2_score
        result = self.difficulty

        if delta <= -5:
            result = self._valmap(delta, -10, -5, 0.0, self._start_difficulty)

        elif delta >= 5:
            result = self._valmap(delta, 5, 10, self._start_difficulty, 1.0)

        return result

    def _valmap(self, value, in_min, in_max, out_min, out_max):
        """
        Maps a given value that falls within the input range and scales it to the output range.
        :param value: integer or float
        :param in_min: integer or float
        :param in_max: integer or float
        :param out_min: integer or float
        :param out_max: integer or float
        :return: float
        """
        return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
