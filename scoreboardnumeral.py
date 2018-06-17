import pygame

class ScoreboardNumeral(pygame.sprite.Sprite):
    def __init__(self, height, fg_color, bg_color, *groups, value=0):
        """
        :param height: int
        :param fg_color: string
        :param bg_color: string
        :param groups: pygame.sprite.Group
        :param value: int
        """

        super().__init__(*groups)

        self.image = pygame.Surface((int(height / 2), height)).convert()
        self.background = pygame.Surface((int(height / 2), height)).convert()

        self.rect = self.image.get_rect()
        self._layer = 0
        self.size = height

        self.fg_color = pygame.Color(fg_color)
        self.bg_color = pygame.Color(bg_color)
        self.value = value

        self._digit_shapes = self._init_digit_shapes()
        self._digit_strokewidth = int(self.size / 8)

        self.background.fill(self.bg_color)

    def set_value(self, value):
        self.value = value
        self.image.blit(self.background, (0, 0))
        pygame.draw.lines(self.image, self.fg_color, False, self._digit_shapes[self.value], self._digit_strokewidth)

    def get_value(self):
        return self.value

    def set_size(self, height):
        self.size = height
        self.image = pygame.Surface((int(self.size / 2), self.size)).convert()
        self.background = pygame.Surface((int(self.size / 2), self.size)).convert()
        self.rect = self.image.get_rect()
        self.background.fill(self.bg_color)
        self._digit_strokewidth = int(self.size / 8)
        self._digit_shapes = self._init_digit_shapes()
        self.set_value(self.value)

    def get_size(self):
        return self.rect.size

    def get_width(self):
        return self.size / 2

    def get_stroke_width(self):
        return int(self.size / 8)

    def _init_digit_shapes(self):
        return (
            (self.rect.topleft, self.rect.topright, self.rect.bottomright, self.rect.bottomleft, self.rect.topleft),
            (self.rect.topright, self.rect.bottomright),
            (self.rect.topleft, self.rect.topright, self.rect.midright, self.rect.midleft, self.rect.bottomleft,
             self.rect.bottomright),
            (self.rect.topleft, self.rect.topright, self.rect.midright, self.rect.midleft, self.rect.midright,
             self.rect.bottomright, self.rect.bottomleft),
            (self.rect.topleft, self.rect.midleft, self.rect.midright, self.rect.topright, self.rect.bottomright),
            (self.rect.topright, self.rect.topleft, self.rect.midleft, self.rect.midright, self.rect.bottomright,
             self.rect.bottomleft),
            (self.rect.topleft, self.rect.bottomleft, self.rect.bottomright, self.rect.midright, self.rect.midleft),
            (self.rect.topleft, self.rect.topright, self.rect.bottomright),
            (self.rect.topleft, self.rect.topright, self.rect.bottomright, self.rect.bottomleft, self.rect.topleft,
             self.rect.midleft, self.rect.midright),
            (self.rect.midright, self.rect.midleft, self.rect.topleft, self.rect.topright, self.rect.bottomright)
        )

    def update(self):
        super().update()

    def draw(self, surface):
        return surface.blit(self.image, self.rect.topleft)
