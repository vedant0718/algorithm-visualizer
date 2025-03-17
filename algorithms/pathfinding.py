# algorithms/pathfinding.py
import pygame
import time
import heapq
import math
import sys
from ui.drawing import draw_grid
from config import VISUAL_AREA_HEIGHT, PATHFINDING_GRID_SIZE, VISUAL_WIDTH, GREEN, RED, YELLOW, GRID_MARGIN

def dijkstra(screen, clock, grid, start_node, end_node):
    """
    Run Dijkstra's algorithm on a grid that now includes diagonal moves.
    Cardinal moves cost 1; diagonal moves cost sqrt(2).
    The function returns the total cost (distance) from start to end once found.
    """
    # Priority queue: (cost, (row, col))
    queue = [(0, start_node)]
    visited = set()
    costs = {start_node: 0}
    parents = {}

    while queue:
        current_cost, current = heapq.heappop(queue)
        if current in visited:
            continue
        visited.add(current)

        # Check if we've reached the end node
        if current == end_node:
            # Reconstruct the path
            path = []
            node = current
            while node in parents:
                path.append(node)
                node = parents[node]
            path.append(start_node)
            path.reverse()
            # Animate the final path
            for node in path:
                if node != start_node and node != end_node:
                    grid[node[0]][node[1]] = 5  # Mark the path
                draw_grid(screen, grid)
                pygame.display.flip()
                time.sleep(0.05)
            return current_cost  # Return the computed distance

        # Mark current as visited (if not start or end)
        if current != start_node and current != end_node:
            grid[current[0]][current[1]] = 4  # Mark visited
        draw_grid(screen, grid)
        pygame.display.flip()

        # Process quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Check all 8 directions (4 cardinal and 4 diagonal)
        # Diagonal moves cost sqrt(2), cardinal moves cost 1.
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]:
            nx, ny = current[0] + dx, current[1] + dy
            # Determine grid boundaries based on the visualization panel
            rows = VISUAL_AREA_HEIGHT // PATHFINDING_GRID_SIZE
            cols = VISUAL_WIDTH // PATHFINDING_GRID_SIZE
            if 0 <= nx < rows and 0 <= ny < cols:
                # Skip walls (assuming wall cells are marked with 1)
                if grid[nx][ny] != 1:
                    step_cost = math.sqrt(2) if dx != 0 and dy != 0 else 1
                    new_cost = current_cost + step_cost
                    if (nx, ny) not in costs or new_cost < costs[(nx, ny)]:
                        costs[(nx, ny)] = new_cost
                        heapq.heappush(queue, (new_cost, (nx, ny)))
                        parents[(nx, ny)] = current
        time.sleep(0.05)
    return None  # No path found
