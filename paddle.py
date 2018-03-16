import pygame

# This is the paddle class.

GREEN = (0, 255, 0)

def draw_paddle(screen, x, y):
    pygame.draw.rect(screen, GREEN, [1 + x, y, 10, 50], 0)