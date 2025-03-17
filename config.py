# config.py
WIDTH, HEIGHT = 1000, 800
HEADER_HEIGHT = 200   # <--- Increased for three rows
VISUAL_WIDTH = 600
INFO_WIDTH = 400
VISUAL_AREA_HEIGHT = HEIGHT - HEADER_HEIGHT - 20         # Left visualization panel
# INFO_WIDTH = WIDTH - VISUAL_WIDTH  # Right info panel (300px)# 480px height for visualization
PATHFINDING_GRID_SIZE = 20
DEFAULT_QUEENS = 8              # Default board size for N-Queens
GRID_MARGIN = 1

# Colors
WHITE      = (255, 255, 255)
BLACK      = (0, 0, 0)
RED        = (255, 0, 0)
GREEN      = (0, 255, 0)
BLUE       = (0, 0, 255)
YELLOW     = (255, 255, 0)
PURPLE     = (128, 0, 128)
GRAY       = (200, 200, 200)
LIGHT_BLUE = (173, 216, 230)
