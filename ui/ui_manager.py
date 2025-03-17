# ui/ui_manager.py
import pygame
from config import WIDTH, HEADER_HEIGHT, WHITE, BLACK, VISUAL_WIDTH

def draw_header(screen, font, mode, num_queens):
    header_rect = pygame.Rect(0, 0, WIDTH, HEADER_HEIGHT)
    pygame.draw.rect(screen, WHITE, header_rect)
    pygame.draw.line(screen, BLACK, (0, HEADER_HEIGHT), (WIDTH, HEADER_HEIGHT), 2)
    title = ""
    if mode == "pathfinding":
        title = "Pathfinding Mode - Left-click: Toggle walls; Right-click: Set Start/End."
    elif mode == "queens":
        title = f"N-Queens Mode - Board Size: {num_queens} x {num_queens}"
    elif mode == "backtracking":
        title = "Backtracking Mode - Knapsack / Subset Sum"
    elif mode == "hanoi":
        title = "Tower of Hanoi Mode"
    title_surface = font.render(title, True, BLACK)
    screen.blit(title_surface, (VISUAL_WIDTH // 2 - title_surface.get_width() // 2, HEADER_HEIGHT - 40))
