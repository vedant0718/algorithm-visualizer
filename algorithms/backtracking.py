# algorithms/backtracking.py
# algorithms/backtracking.py
import pygame
import time

def subset_sum_tree(screen, clock, numbers, target, draw_func):
    found_solution = [None]
    recursion_stack = []
    def backtrack(i, current_sum):
        recursion_stack.append((i, current_sum))
        # Draw the current recursion stack as a tree.
        from ui.drawing import draw_subset_sum_tree
        draw_subset_sum_tree(screen, recursion_stack)
        pygame.display.flip()
        pygame.time.delay(200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
        if current_sum == target:
            found_solution[0] = list(recursion_stack)
            recursion_stack.pop()
            return True
        if i == len(numbers) or current_sum > target:
            recursion_stack.pop()
            return False
        if backtrack(i+1, current_sum+numbers[i]):
            return True
        if backtrack(i+1, current_sum):
            return True
        recursion_stack.pop()
        return False
    backtrack(0, 0)
    return found_solution[0]

# Existing knapsack_backtracking and subset_sum_backtracking remain unchanged.

def knapsack_backtracking(screen, clock, items, capacity, draw_func):
    best_value = [0]
    best_selection = [[]]
    current_selection = []

    def backtrack(i, current_weight, current_value):
        draw_func(screen, items, current_selection, capacity, current_weight, current_value)
        pygame.display.flip()
        pygame.time.delay(200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if i == len(items):
            if current_value > best_value[0]:
                best_value[0] = current_value
                best_selection[0] = current_selection.copy()
            return
        backtrack(i + 1, current_weight, current_value)
        weight, value = items[i]
        if current_weight + weight <= capacity:
            current_selection.append(i)
            backtrack(i + 1, current_weight + weight, current_value + value)
            current_selection.pop()

    backtrack(0, 0, 0)
    final_weight = sum(items[i][0] for i in best_selection[0])
    draw_func(screen, items, best_selection[0], capacity, final_weight, best_value[0])
    pygame.display.flip()
    return best_value[0], best_selection[0]

def subset_sum_backtracking(screen, clock, numbers, target, draw_func):
    found_solution = [None]
    current_selection = []

    def backtrack(i, current_sum):
        draw_func(screen, numbers, current_selection, target, current_sum)
        pygame.display.flip()
        pygame.time.delay(200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if current_sum == target:
            found_solution[0] = current_selection.copy()
            return True
        if i == len(numbers) or current_sum > target:
            return False
        current_selection.append(i)
        if backtrack(i + 1, current_sum + numbers[i]):
            return True
        current_selection.pop()
        if backtrack(i + 1, current_sum):
            return True
        return False

    backtrack(0, 0)
    final_sum = sum(numbers[i] for i in (found_solution[0] if found_solution[0] is not None else []))
    draw_func(screen, numbers, found_solution[0] if found_solution[0] is not None else [], target, final_sum)
    pygame.display.flip()
    return found_solution[0]
