# algorithms/queens.py
import pygame
import time

def is_safe(queen_positions, row, col):
    for i in range(row):
        if (queen_positions[i] == col or
            queen_positions[i] - i == col - row or
            queen_positions[i] + i == col + row):
            return False
    return True

def solve_queens(screen, queen_positions, row, n, draw_func):
    if row == n:
        return True
    for col in range(n):
        if is_safe(queen_positions, row, col):
            queen_positions[row] = col
            draw_func(screen, queen_positions, queens_solved=False, n=n)
            pygame.display.flip()
            pygame.time.delay(300)
            if solve_queens(screen, queen_positions, row + 1, n, draw_func):
                return True
            queen_positions[row] = -1
            draw_func(screen, queen_positions, queens_solved=False, n=n)
            pygame.display.flip()
            pygame.time.delay(300)
    return False
