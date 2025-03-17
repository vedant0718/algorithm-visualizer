# main.py
import pygame
import sys
from config import *
from ui.buttons import Button
from ui.input_box import InputBox
from ui.drawing import (
    draw_grid, draw_queens, draw_knapsack, draw_subset_sum, draw_hanoi,
    draw_subset_sum_tree, draw_pseudocode, draw_flowchart, draw_algorithm_code
)
from ui.ui_manager import draw_header
from algorithms import pathfinding, queens, backtracking, hanoi
from utils.helpers import init_grid, init_queens

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algorithm Visualizer")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)
small_font = pygame.font.SysFont("Arial", 15)

# ----------------------------
#  GLOBAL STATE
# ----------------------------
algorithm_mode = "pathfinding"   # or "queens", "backtracking", "hanoi"
pathfinding_algorithm = "dijkstra"
backtracking_algorithm = "knapsack"
info_mode = "pseudocode"         # "pseudocode", "flowchart", "code"

# This variable holds the final result/answer for each section
result_message = ""

# Pathfinding
grid, start_node, end_node = init_grid()
pathfinding_set_mode = "start"   # toggles between "start" and "end"

# N-Queens
num_queens = DEFAULT_QUEENS
queen_positions = init_queens(num_queens)
queens_solved = False

# Backtracking
knapsack_items = [(2, 3), (3, 4), (4, 5), (5, 8)]
knapsack_capacity = 7
subset_numbers = [3, 34, 4, 12, 5, 2]
subset_target = 9

# Hanoi
hanoi_n = 3
pegs = {"A": list(range(hanoi_n, 0, -1)), "B": [], "C": []}

# ----------------------------
#  HEADER BUTTONS (ROW 1)
# ----------------------------
PATHFINDING_BTN  = Button(  20, 10, 110, 30, "Pathfinding")
QUEENS_BTN       = Button( 140, 10, 110, 30, "N-Queens")
BACKTRACKING_BTN = Button( 260, 10, 110, 30, "Backtracking")
HANOI_BTN        = Button( 380, 10, 110, 30, "Hanoi")
RESET_BTN        = Button( WIDTH-270, 10, 110, 30, "Reset")
START_BTN        = Button( WIDTH-140, 10, 110, 30, "Start", color=GREEN)

# ----------------------------
#  HEADER: ROW 2 + ROW 3
# ----------------------------
# 1) N-Queens
queens_input_box     = InputBox(20, 60,  80, 30, text=str(num_queens))
queens_update_button = Button(110, 60, 110, 30, "Update Board")

# 2) Pathfinding
dijkstra_button      = Button(20, 60, 110, 30, "Dijkstra")

# 3) Backtracking sub-mode selection (Row 2):
back_knapsack_button = Button(20, 60, 110, 30, "Knapsack")
back_subset_button   = Button(140, 60, 110, 30, "Subset Sum")

#   - Knapsack inputs (Row 3):
knapsack_items_input    = InputBox(20, 110, 200, 30, text="2:3,3:4,4:5,5:8")
knapsack_capacity_input = InputBox(230, 110,  80, 30, text="7")
knapsack_update_button  = Button(320, 110, 120, 30, "Update Knap.")

#   - Subset Sum inputs (Row 3):
subset_numbers_input = InputBox(20, 110, 200, 30, text="3,34,4,12,5,2")
subset_target_input  = InputBox(230, 110,  80, 30, text="9")
subset_update_button = Button(320, 110, 120, 30, "Update Subset")

# 4) Hanoi
hanoi_input_box    = InputBox(20, 60,  80, 30, text="3")
hanoi_update_button= Button(110, 60, 110, 30, "Update Disks")

# Info panel
pseudocode_button = Button(VISUAL_WIDTH + 10, HEADER_HEIGHT + 10,  100, 30, "Pseudocode")
flowchart_button  = Button(VISUAL_WIDTH +120, HEADER_HEIGHT + 10,   80, 30, "Flowchart")
code_button       = Button(VISUAL_WIDTH + 10, HEADER_HEIGHT + 50,  100, 30, "Code")

# ----------------------------
#  RESET FUNCTION
# ----------------------------
def reset():
    global grid, start_node, end_node, pathfinding_set_mode
    global queen_positions, queens_solved, num_queens
    global knapsack_items, knapsack_capacity, subset_numbers, subset_target
    global hanoi_n, pegs
    global result_message

    grid, start_node, end_node = init_grid()
    pathfinding_set_mode = "start"

    queen_positions = init_queens(num_queens)
    queens_solved   = False

    knapsack_items     = [(2, 3), (3, 4), (4, 5), (5, 8)]
    knapsack_capacity  = 7
    subset_numbers     = [3, 34, 4, 12, 5, 2]
    subset_target      = 9

    hanoi_n = 3
    pegs = {"A": list(range(hanoi_n, 0, -1)), "B": [], "C": []}

    queens_input_box.text = str(num_queens)
    queens_input_box.txt_surface = queens_input_box.font.render(queens_input_box.text, True, queens_input_box.color)

    result_message = ""  # Clear final result

# ----------------------------
#  MAIN LOOP
# ----------------------------
def main():
    global algorithm_mode, pathfinding_algorithm, backtracking_algorithm, info_mode
    global grid, start_node, end_node, pathfinding_set_mode
    global queen_positions, queens_solved, num_queens
    global knapsack_items, knapsack_capacity, subset_numbers, subset_target
    global hanoi_n, pegs
    global result_message

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            mouse_pos = pygame.mouse.get_pos()

            # ROW 1 (Mode selection, Reset/Start)
            PATHFINDING_BTN.check_hover(mouse_pos)
            QUEENS_BTN.check_hover(mouse_pos)
            BACKTRACKING_BTN.check_hover(mouse_pos)
            HANOI_BTN.check_hover(mouse_pos)
            RESET_BTN.check_hover(mouse_pos)
            START_BTN.check_hover(mouse_pos)

            # ROW 2/3 (Algorithm-specific)
            if algorithm_mode == "pathfinding":
                dijkstra_button.check_hover(mouse_pos)
            elif algorithm_mode == "queens":
                queens_input_box.check_hover(mouse_pos)
                queens_update_button.check_hover(mouse_pos)
            elif algorithm_mode == "backtracking":
                back_knapsack_button.check_hover(mouse_pos)
                back_subset_button.check_hover(mouse_pos)
                if backtracking_algorithm == "knapsack":
                    knapsack_items_input.check_hover(mouse_pos)
                    knapsack_capacity_input.check_hover(mouse_pos)
                    knapsack_update_button.check_hover(mouse_pos)
                else:
                    subset_numbers_input.check_hover(mouse_pos)
                    subset_target_input.check_hover(mouse_pos)
                    subset_update_button.check_hover(mouse_pos)
            elif algorithm_mode == "hanoi":
                hanoi_input_box.check_hover(mouse_pos)
                hanoi_update_button.check_hover(mouse_pos)

            # Info panel
            pseudocode_button.check_hover(mouse_pos)
            flowchart_button.check_hover(mouse_pos)
            code_button.check_hover(mouse_pos)

            # Pathfinding: right-click to set start/end
            if algorithm_mode == "pathfinding" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                mx, my = event.pos
                if my >= HEADER_HEIGHT and mx < VISUAL_WIDTH:
                    row = (my - HEADER_HEIGHT) // PATHFINDING_GRID_SIZE
                    col = mx // PATHFINDING_GRID_SIZE
                    if grid[row][col] == 1:
                        grid[row][col] = 0
                    else:
                        if pathfinding_set_mode == "start":
                            for r in range(len(grid)):
                                for c in range(len(grid[0])):
                                    if grid[r][c] == 2:
                                        grid[r][c] = 0
                            grid[row][col] = 2
                            start_node = (row, col)
                            pathfinding_set_mode = "end"
                        else:
                            for r in range(len(grid)):
                                for c in range(len(grid[0])):
                                    if grid[r][c] == 3:
                                        grid[r][c] = 0
                            grid[row][col] = 3
                            end_node = (row, col)
                            pathfinding_set_mode = "start"

            # Input box typing
            if algorithm_mode == "queens":
                queens_input_box.handle_event(event)
            elif algorithm_mode == "backtracking":
                if backtracking_algorithm == "knapsack":
                    knapsack_items_input.handle_event(event)
                    knapsack_capacity_input.handle_event(event)
                else:
                    subset_numbers_input.handle_event(event)
                    subset_target_input.handle_event(event)
            elif algorithm_mode == "hanoi":
                hanoi_input_box.handle_event(event)

            # CLICK handling
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Row 1
                if PATHFINDING_BTN.is_clicked(mouse_pos, event):
                    algorithm_mode = "pathfinding"
                    reset()
                elif QUEENS_BTN.is_clicked(mouse_pos, event):
                    algorithm_mode = "queens"
                    reset()
                elif BACKTRACKING_BTN.is_clicked(mouse_pos, event):
                    algorithm_mode = "backtracking"
                    reset()
                elif HANOI_BTN.is_clicked(mouse_pos, event):
                    algorithm_mode = "hanoi"
                    reset()
                elif RESET_BTN.is_clicked(mouse_pos, event):
                    reset()
                elif START_BTN.is_clicked(mouse_pos, event):
                    result_message = ""  # Clear old result

                    if algorithm_mode == "pathfinding":
                        path_found = pathfinding.dijkstra(screen, clock, grid, start_node, end_node)
                        result_message = f"Path found! Distance: {path_found:.2f}" if path_found else "No path found."
                    elif algorithm_mode == "queens":
                        solved = queens.solve_queens(screen, queen_positions, 0, num_queens, draw_queens)
                        result_message = (f"Solved for {num_queens}x{num_queens}." 
                                          if solved else "No solution found.")
                    elif algorithm_mode == "backtracking":
                        if backtracking_algorithm == "knapsack":
                            best_val, _ = backtracking.knapsack_backtracking(screen, clock, knapsack_items, knapsack_capacity, draw_knapsack)
                            result_message = f"Knapsack best value = {best_val}"
                        else:
                            solution_tree = backtracking.subset_sum_tree(screen, clock, subset_numbers, subset_target, draw_subset_sum_tree)
                            if solution_tree:
                                result_message = "Subset Sum: Found a valid subset!"
                            else:
                                result_message = "Subset Sum: No valid subset."
                    elif algorithm_mode == "hanoi":
                        moves = hanoi.hanoi_visualizer(screen, clock, hanoi_n, pegs, draw_hanoi)
                        result_message = f"Hanoi done in {len(moves)} moves."

                # Row 2/3
                if algorithm_mode == "pathfinding":
                    if dijkstra_button.is_clicked(mouse_pos, event):
                        pathfinding_algorithm = "dijkstra"
                elif algorithm_mode == "queens":
                    if queens_update_button.is_clicked(mouse_pos, event):
                        txt = queens_input_box.text.strip()
                        try:
                            new_n = int(txt)
                            if new_n > 0 and new_n != num_queens:
                                num_queens = new_n
                                queen_positions = init_queens(num_queens)
                                result_message = f"Board updated to {num_queens}x{num_queens}"
                        except ValueError:
                            pass
                elif algorithm_mode == "backtracking":
                    if back_knapsack_button.is_clicked(mouse_pos, event):
                        backtracking_algorithm = "knapsack"
                        result_message = "Knapsack selected."
                    elif back_subset_button.is_clicked(mouse_pos, event):
                        backtracking_algorithm = "subset"
                        result_message = "Subset Sum selected."
                    if backtracking_algorithm == "knapsack":
                        if knapsack_update_button.is_clicked(mouse_pos, event):
                            try:
                                txt_items = knapsack_items_input.text.strip()
                                txt_cap = knapsack_capacity_input.text.strip()
                                items = []
                                for pair in txt_items.split(","):
                                    w, v = pair.split(":")
                                    items.append((int(w.strip()), int(v.strip())))
                                cap = int(txt_cap)
                                knapsack_items = items
                                knapsack_capacity = cap
                                result_message = f"Knapsack updated: capacity={cap}, items={items}"
                            except:
                                pass
                    else:
                        if subset_update_button.is_clicked(mouse_pos, event):
                            try:
                                txt_nums = subset_numbers_input.text.strip()
                                txt_targ = subset_target_input.text.strip()
                                nums = [int(x) for x in txt_nums.split(",")]
                                targ = int(txt_targ)
                                subset_numbers = nums
                                subset_target  = targ
                                result_message = f"Subset updated: target={targ}, numbers={nums}"
                            except:
                                pass
                elif algorithm_mode == "hanoi":
                    if hanoi_update_button.is_clicked(mouse_pos, event):
                        txt = hanoi_input_box.text.strip()
                        try:
                            new_n = int(txt)
                            if new_n > 0 and new_n != hanoi_n:
                                hanoi_n = new_n
                                pegs = {"A": list(range(hanoi_n, 0, -1)), "B": [], "C": []}
                                result_message = f"Hanoi updated: {hanoi_n} disks."
                        except:
                            pass

                # Info panel
                if pseudocode_button.is_clicked(mouse_pos, event):
                    info_mode = "pseudocode"
                elif flowchart_button.is_clicked(mouse_pos, event):
                    info_mode = "flowchart"
                elif code_button.is_clicked(mouse_pos, event):
                    info_mode = "code"

        # Update input boxes each frame
        if algorithm_mode == "queens":
            queens_input_box.update()
        elif algorithm_mode == "backtracking":
            if backtracking_algorithm == "knapsack":
                knapsack_items_input.update()
                knapsack_capacity_input.update()
            else:
                subset_numbers_input.update()
                subset_target_input.update()
        elif algorithm_mode == "hanoi":
            hanoi_input_box.update()

        # RENDERING
        screen.fill(WHITE)
        draw_header(screen, font, algorithm_mode, num_queens)

        # Divider between left (viz) & right (info)
        pygame.draw.line(screen, BLACK, (VISUAL_WIDTH, HEADER_HEIGHT), (VISUAL_WIDTH, HEIGHT), 2)

        # Row 1
        PATHFINDING_BTN.draw(screen, small_font)
        QUEENS_BTN.draw(screen, small_font)
        BACKTRACKING_BTN.draw(screen, small_font)
        HANOI_BTN.draw(screen, small_font)
        RESET_BTN.draw(screen, small_font)
        START_BTN.draw(screen, small_font)

        # Row 2 + 3
        if algorithm_mode == "pathfinding":
            dijkstra_button.draw(screen, small_font)

        elif algorithm_mode == "queens":
            queens_input_box.draw(screen)
            queens_update_button.draw(screen, small_font)

        elif algorithm_mode == "backtracking":
            # Row 2: sub-mode selection
            back_knapsack_button.draw(screen, small_font)
            back_subset_button.draw(screen, small_font)
            # Row 3: actual inputs
            if backtracking_algorithm == "knapsack":
                knapsack_items_input.draw(screen)
                knapsack_capacity_input.draw(screen)
                knapsack_update_button.draw(screen, small_font)
            else:
                subset_numbers_input.draw(screen)
                subset_target_input.draw(screen)
                subset_update_button.draw(screen, small_font)

        elif algorithm_mode == "hanoi":
            hanoi_input_box.draw(screen)
            hanoi_update_button.draw(screen, small_font)

        # Left Panel
        viz_rect = pygame.Rect(0, HEADER_HEIGHT, VISUAL_WIDTH, VISUAL_AREA_HEIGHT)
        pygame.draw.rect(screen, WHITE, viz_rect)

        if algorithm_mode == "pathfinding":
            draw_grid(screen, grid)
        elif algorithm_mode == "queens":
            draw_queens(screen, queen_positions, queens_solved, num_queens)
        elif algorithm_mode == "backtracking":
            if backtracking_algorithm == "knapsack":
                draw_knapsack(screen, knapsack_items, [], knapsack_capacity, 0, 0)
            else:
                draw_subset_sum(screen, subset_numbers, [], subset_target, 0)
        elif algorithm_mode == "hanoi":
            draw_hanoi(screen, pegs, hanoi_n)

        # Show final result at bottom of left panel
        if result_message:
            msg_font = pygame.font.SysFont("Arial", 16)
            text_surf = msg_font.render(result_message, True, (180,0,0))
            screen.blit(text_surf, (10, HEIGHT - 20))

        # Right Panel (info)
        info_rect = pygame.Rect(VISUAL_WIDTH, HEADER_HEIGHT, INFO_WIDTH, VISUAL_AREA_HEIGHT)
        pygame.draw.rect(screen, (245, 245, 245), info_rect)
        pseudocode_button.draw(screen, small_font)
        flowchart_button.draw(screen, small_font)
        code_button.draw(screen, small_font)

        if info_mode == "pseudocode":
            draw_pseudocode(screen, algorithm_mode, backtracking_algorithm)
        elif info_mode == "flowchart":
            draw_flowchart(screen, algorithm_mode, backtracking_algorithm)
        else:
            draw_algorithm_code(screen, algorithm_mode, pathfinding_algorithm, backtracking_algorithm)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
