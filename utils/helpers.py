# utils/helpers.py
from config import VISUAL_AREA_HEIGHT, VISUAL_WIDTH, PATHFINDING_GRID_SIZE

def init_grid():
    rows = VISUAL_AREA_HEIGHT // PATHFINDING_GRID_SIZE
    cols = VISUAL_WIDTH // PATHFINDING_GRID_SIZE
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    start_node = (1, 1)
    end_node = (rows - 2, cols - 2)
    grid[start_node[0]][start_node[1]] = 2
    grid[end_node[0]][end_node[1]] = 3
    return grid, start_node, end_node

def init_queens(n):
    return [-1] * n
