# Defining colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Constants
DISPLAY_SIZE = (1024, 576)  # Size of the entire window
PLAYFIELD_SIZE = (DISPLAY_SIZE[0] * 0.98, DISPLAY_SIZE[1] * 0.85)   # Size of the playfield relative to window size
PADDLE_HEIGHT = int(DISPLAY_SIZE[1] / 8)    # Paddle height
PADDLE_WIDTH = int(DISPLAY_SIZE[0] / 102.4)   # Paddle width
