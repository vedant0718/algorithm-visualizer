# algorithms/hanoi.py
import pygame
import time

def hanoi_visualizer(screen, clock, n, pegs, draw_func):
    moves = []
    def hanoi(n, source, target, auxiliary):
        if n > 0:
            hanoi(n - 1, source, auxiliary, target)
            moves.append((source, target))
            hanoi(n - 1, auxiliary, target, source)
    hanoi(n, 'A', 'C', 'B')
    for move in moves:
        src, tgt = move
        if pegs[src]:
            disk = pegs[src].pop()
            pegs[tgt].append(disk)
        draw_func(screen, pegs, n)
        pygame.display.flip()
        pygame.time.delay(500)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    return moves
