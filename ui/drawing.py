# ui/drawing.py
import pygame
from config import (WIDTH, HEIGHT, HEADER_HEIGHT, VISUAL_WIDTH, VISUAL_AREA_HEIGHT,
                    PATHFINDING_GRID_SIZE, GRID_MARGIN, WHITE, BLACK, GREEN, RED,
                    LIGHT_BLUE, YELLOW, PURPLE, GRAY, INFO_WIDTH)

def draw_array(screen, array, found_index, current_idx=-1, secondary_idx=-1, highlight_left=-1, highlight_right=-1):
    bar_width = WIDTH / len(array)
    for i, height in enumerate(array):
        color = LIGHT_BLUE
        if i == current_idx:
            color = RED
        elif i == secondary_idx:
            color = GREEN
        elif highlight_left <= i <= highlight_right:
            color = YELLOW
        elif i == found_index:
            color = PURPLE
        pygame.draw.rect(screen, color, (i * bar_width, HEIGHT - height, bar_width, height))
        pygame.draw.rect(screen, BLACK, (i * bar_width, HEIGHT - height, bar_width, height), 1)

def draw_grid(screen, grid):
    grid_width = VISUAL_WIDTH // PATHFINDING_GRID_SIZE
    grid_height = VISUAL_AREA_HEIGHT // PATHFINDING_GRID_SIZE
    for row in range(grid_height):
        for col in range(grid_width):
            color = WHITE
            if grid[row][col] == 1:
                color = BLACK
            elif grid[row][col] == 2:
                color = GREEN
            elif grid[row][col] == 3:
                color = RED
            elif grid[row][col] == 4:
                color = LIGHT_BLUE
            elif grid[row][col] == 5:
                color = YELLOW
            pygame.draw.rect(screen, color, (col * PATHFINDING_GRID_SIZE, HEADER_HEIGHT + row * PATHFINDING_GRID_SIZE, 
                                               PATHFINDING_GRID_SIZE - GRID_MARGIN, PATHFINDING_GRID_SIZE - GRID_MARGIN))
            pygame.draw.rect(screen, GRAY, (col * PATHFINDING_GRID_SIZE, HEADER_HEIGHT + row * PATHFINDING_GRID_SIZE, 
                                            PATHFINDING_GRID_SIZE, PATHFINDING_GRID_SIZE), 1)

def draw_queens(screen, queen_positions, queens_solved, n):
    cell_size = min(VISUAL_WIDTH, VISUAL_AREA_HEIGHT) // n
    board_size = cell_size * n
    offset_x = (VISUAL_WIDTH - board_size) // 2
    offset_y = HEADER_HEIGHT + (VISUAL_AREA_HEIGHT - board_size) // 2

    for row in range(n):
        for col in range(n):
            color = WHITE if (row + col) % 2 == 0 else GRAY
            pygame.draw.rect(screen, color, (offset_x + col * cell_size, offset_y + row * cell_size, cell_size, cell_size))
            if queen_positions[row] == col:
                pygame.draw.circle(screen, PURPLE, 
                                   (offset_x + col * cell_size + cell_size // 2, offset_y + row * cell_size + cell_size // 2), 
                                   cell_size // 3)
                pygame.draw.rect(screen, BLACK, (offset_x + col * cell_size, offset_y + row * cell_size, cell_size, cell_size), 2)
    pygame.draw.rect(screen, BLACK, (offset_x, offset_y, board_size, board_size), 3)
    font = pygame.font.SysFont('Arial', 20)
    status_text = "Solved!" if queens_solved else "Solving..."
    text_surface = font.render(status_text, True, BLACK)
    screen.blit(text_surface, (VISUAL_WIDTH // 2 - text_surface.get_width() // 2, offset_y + board_size + 10))

def draw_knapsack(screen, items, chosen, capacity, current_weight, current_value):
    # Draw a table for knapsack items.
    pygame.draw.rect(screen, WHITE, (0, HEADER_HEIGHT, VISUAL_WIDTH, VISUAL_AREA_HEIGHT))
    font = pygame.font.SysFont('Arial', 16)
    headers = ["Item", "Weight", "Value", "Selected"]
    x = 20
    y = HEADER_HEIGHT + 10
    col_widths = [80, 80, 80, 100]
    for i, header_text in enumerate(headers):
        header_surface = font.render(header_text, True, BLACK)
        pygame.draw.rect(screen, GRAY, (x, y, col_widths[i], 30))
        pygame.draw.rect(screen, BLACK, (x, y, col_widths[i], 30), 2)
        screen.blit(header_surface, (x + 5, y + 5))
        x += col_widths[i] + 10
    y += 40
    for idx, (weight, value) in enumerate(items):
        x = 20
        selected = "Yes" if idx in chosen else "No"
        row_data = [f"{idx+1}", f"{weight}", f"{value}", selected]
        for i, data in enumerate(row_data):
            cell_surface = font.render(data, True, BLACK)
            cell_color = LIGHT_BLUE if idx in chosen else WHITE
            pygame.draw.rect(screen, cell_color, (x, y, col_widths[i], 30))
            pygame.draw.rect(screen, BLACK, (x, y, col_widths[i], 30), 2)
            screen.blit(cell_surface, (x + 5, y + 5))
            x += col_widths[i] + 10
        y += 40
    status_text = f"Capacity: {capacity} | Current Weight: {current_weight} | Total Value: {current_value}"
    status_surface = font.render(status_text, True, BLACK)
    screen.blit(status_surface, (20, HEADER_HEIGHT + VISUAL_AREA_HEIGHT - 40))


def draw_subset_sum_tree(screen, stack):
    """
    Draw the current recursion stack as a simple tree:
    Each node is a circle with text "i:current_sum".
    Nodes are drawn with increasing indentation.
    """
    # Clear visualization area
    pygame.draw.rect(screen, WHITE, (0, HEADER_HEIGHT, VISUAL_WIDTH, VISUAL_AREA_HEIGHT))
    font = pygame.font.SysFont('Arial', 16)
    x0 = 20
    y0 = HEADER_HEIGHT + 20
    for depth, (i, s) in enumerate(stack):
        x = x0 + depth * 40
        y = y0 + depth * 40
        pygame.draw.circle(screen, LIGHT_BLUE, (x, y), 15)
        text = f"{i}:{s}"
        text_surface = font.render(text, True, BLACK)
        screen.blit(text_surface, (x - 12, y - 8))
        if depth > 0:
            prev_x = x0 + (depth - 1) * 40
            prev_y = y0 + (depth - 1) * 40
            pygame.draw.line(screen, BLACK, (prev_x, prev_y), (x, y), 2)

def draw_subset_sum(screen, numbers, chosen, target, current_sum):
    # Draw numbers as cells in a grid (single row).
    pygame.draw.rect(screen, WHITE, (0, HEADER_HEIGHT, VISUAL_WIDTH, VISUAL_AREA_HEIGHT))
    font = pygame.font.SysFont('Arial', 16)
    header = "Subset Sum: Select numbers that sum to target"
    header_surface = font.render(header, True, BLACK)
    screen.blit(header_surface, (20, HEADER_HEIGHT + 10))
    margin = 20
    cell_width = 60
    cell_height = 60
    x = 20
    y = HEADER_HEIGHT + 50
    for idx, num in enumerate(numbers):
        rect = pygame.Rect(x, y, cell_width, cell_height)
        color = GREEN if chosen and idx in chosen else LIGHT_BLUE
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        num_surface = font.render(str(num), True, BLACK)
        text_rect = num_surface.get_rect(center=rect.center)
        screen.blit(num_surface, text_rect)
        x += cell_width + margin
    status_text = f"Target: {target} | Current Sum: {current_sum}"
    status_surface = font.render(status_text, True, BLACK)
    screen.blit(status_surface, (20, HEADER_HEIGHT + VISUAL_AREA_HEIGHT - 40))

def draw_hanoi(screen, pegs, n):
    pygame.draw.rect(screen, WHITE, (0, HEADER_HEIGHT, VISUAL_WIDTH, VISUAL_AREA_HEIGHT))
    font = pygame.font.SysFont('Arial', 16)
    peg_positions = {'A': VISUAL_WIDTH//4, 'B': VISUAL_WIDTH//2, 'C': 3*VISUAL_WIDTH//4}
    base_y = HEADER_HEIGHT + VISUAL_AREA_HEIGHT - 50
    for peg, x in peg_positions.items():
        pygame.draw.line(screen, BLACK, (x, base_y), (x, base_y - n * 30), 5)
        disks = pegs[peg]
        disk_y = base_y - 30
        for disk in sorted(disks, reverse=True):
            disk_width = disk * 20
            disk_rect = pygame.Rect(x - disk_width // 2, disk_y - 20, disk_width, 20)
            pygame.draw.rect(screen, LIGHT_BLUE, disk_rect)
            pygame.draw.rect(screen, BLACK, disk_rect, 2)
            disk_y -= 25
    for peg, x in peg_positions.items():
        label = font.render(peg, True, BLACK)
        screen.blit(label, (x - 10, base_y + 10))

def draw_pseudocode(screen, mode, back_algo):
    info_y = HEADER_HEIGHT + 80
    font = pygame.font.SysFont('Arial', 14)
    pseudocode = ""
    if mode == "pathfinding":
        pseudocode = (
            "Dijkstra's Algorithm:\n"
            "1. Initialize queue with start node.\n"
            "2. While queue not empty:\n"
            "   a. Pop node with lowest cost.\n"
            "   b. If goal reached, reconstruct path.\n"
            "   c. For each neighbor, update cost.\n"
            "3. End."
        )
    elif mode == "queens":
        pseudocode = (
            "N-Queens Problem:\n"
            "function solveNQueens(row):\n"
            "   if row == n: return True\n"
            "   for col in range(n):\n"
            "       if safe(row, col):\n"
            "           place queen\n"
            "           if solveNQueens(row+1): return True\n"
            "           remove queen\n"
            "   return False"
        )
    elif mode == "backtracking":
        if back_algo == "knapsack":
            pseudocode = (
                "Knapsack Problem:\n"
                "function knapsack(i, weight, value):\n"
                "   if i == len(items): update best\n"
                "   knapsack(i+1, weight, value)\n"
                "   if weight + items[i].w <= capacity:\n"
                "       include item and knapsack(i+1, new_weight, new_value)"
            )
        else:
            pseudocode = (
                "Subset Sum Problem:\n"
                "function subsetSum(i, sum):\n"
                "   if sum == target: return solution\n"
                "   if i == len(numbers) or sum > target: return False\n"
                "   return subsetSum(i+1, sum+numbers[i]) or subsetSum(i+1, sum)"
            )
    elif mode == "hanoi":
        pseudocode = (
            "Tower of Hanoi:\n"
            "function hanoi(n, source, target, aux):\n"
            "   if n > 0:\n"
            "       hanoi(n-1, source, aux, target)\n"
            "       move disk from source to target\n"
            "       hanoi(n-1, aux, target, source)"
        )
    lines = pseudocode.split("\n")
    y = info_y
    for line in lines:
        text_surface = font.render(line, True, BLACK)
        screen.blit(text_surface, (VISUAL_WIDTH + 10, y))
        y += 20

def draw_flowchart(screen, mode, back_algo):
    info_y = HEADER_HEIGHT + 80
    font = pygame.font.SysFont('Arial', 14)
    steps = []
    if mode == "pathfinding":
        steps = ["Start", "Init Queue", "Pop Node", "Update Neighbors", "Goal?", "Reconstruct", "End"]
    elif mode == "queens":
        steps = ["Start", "Place Queen", "Check Safe", "Next Row", "Backtrack", "End"]
    elif mode == "backtracking":
        if back_algo == "knapsack":
            steps = ["Start", "Exclude", "Include", "Update Best", "Backtrack", "End"]
        else:
            steps = ["Start", "Include", "Exclude", "Check Sum", "Backtrack", "End"]
    elif mode == "hanoi":
        steps = ["Start", "Move n-1", "Move Disk", "Move n-1", "End"]
    else:
        steps = []
    box_width = INFO_WIDTH - 20
    box_height = 30
    gap = 15
    y = info_y
    for step in steps:
        rect = pygame.Rect(VISUAL_WIDTH + 10, y, box_width, box_height)
        pygame.draw.rect(screen, LIGHT_BLUE, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        text_surface = font.render(step, True, BLACK)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)
        y += box_height + gap
        if step != steps[-1]:
            pygame.draw.line(screen, BLACK, (VISUAL_WIDTH + 10 + box_width/2, y - gap),
                             (VISUAL_WIDTH + 10 + box_width/2, y - gap/2), 2)

def draw_algorithm_code(screen, mode, path_algo, back_algo):
    info_y = HEADER_HEIGHT + 80
    font = pygame.font.SysFont('Courier New', 12)
    code = ""
    complexity = ""
    if mode == "pathfinding":
        code = (
            "def dijkstra(screen, clock, grid, start, end):\n"
            "    queue = [(0, start)]\n"
            "    while queue:\n"
            "        cost, current = heapq.heappop(queue)\n"
            "        if current == end:\n"
            "            reconstruct_path()\n"
            "        for neighbor in get_neighbors(current):\n"
            "            update_costs()\n"
            "            heapq.heappush(queue, (new_cost, neighbor))\n"
        )
        complexity = "Time: O(E log V) | Space: O(V)"
    elif mode == "queens":
        code = (
            "def solve_queens(queen_positions, row, n):\n"
            "    if row == n: return True\n"
            "    for col in range(n):\n"
            "        if safe(row, col):\n"
            "            queen_positions[row] = col\n"
            "            if solve_queens(queen_positions, row+1, n): return True\n"
            "            queen_positions[row] = -1\n"
            "    return False\n"
        )
        complexity = "Time: Exponential | Space: O(n)"
    elif mode == "backtracking":
        if back_algo == "knapsack":
            code = (
                "def knapsack(i, weight, value):\n"
                "    if i == len(items): update_best()\n"
                "    knapsack(i+1, weight, value)\n"
                "    if weight + items[i].w <= capacity:\n"
                "        include_item(i)\n"
                "        knapsack(i+1, new_weight, new_value)\n"
                "        remove_item(i)\n"
            )
            complexity = "Time: O(2^n) | Space: O(n)"
        else:
            code = (
                "def subset_sum(i, current_sum):\n"
                "    if current_sum == target: return solution\n"
                "    if i == len(numbers) or current_sum > target: return False\n"
                "    return subset_sum(i+1, current_sum+numbers[i]) or subset_sum(i+1, current_sum)\n"
            )
            complexity = "Time: O(2^n) | Space: O(n)"
    elif mode == "hanoi":
        code = (
            "def hanoi(n, source, target, aux):\n"
            "    if n > 0:\n"
            "        hanoi(n-1, source, aux, target)\n"
            "        move_disk(source, target)\n"
            "        hanoi(n-1, aux, target, source)\n"
        )
        complexity = "Time: O(2^n) | Space: O(n)"
    lines = code.split("\n")
    y = info_y
    for line in lines:
        text_surface = font.render(line, True, BLACK)
        screen.blit(text_surface, (VISUAL_WIDTH + 10, y))
        y += 16
    comp_surface = font.render("Complexity:", True, BLACK)
    screen.blit(comp_surface, (VISUAL_WIDTH + 10, y + 10))
    comp_details = font.render(complexity, True, BLACK)
    screen.blit(comp_details, (VISUAL_WIDTH + 10, y + 30))
