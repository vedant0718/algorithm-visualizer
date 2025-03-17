# Algorithm Visualizer

A dynamic, AAA-quality algorithm visualizer built with Python and Pygame. This interactive tool allows you to visualize and experiment with several classical algorithms through engaging animations and dynamic inputs.

## 🚀 Features

### Interactive Algorithms
- **Pathfinding (Dijkstra's Algorithm)**
  - Left-click to toggle walls
  - Right-click to set start (green) and end (red) points
  - Watch as the algorithm finds the shortest path in real-time

- **N-Queens Problem**
  - Adjust board size dynamically via input field
  - Visualize the backtracking process step-by-step
  - See solutions populate in real-time

- **Backtracking Visualizations**
  - **Knapsack Problem**
    - Input items as `weight:value` pairs
    - Set custom knapsack capacity
    - View tabular solution with animated updates
  
  - **Subset Sum Problem**
    - Input a list of numbers and target sum
    - View animated recursion tree showing algorithm decisions
    - Follow the backtracking process visually

- **Tower of Hanoi**
  - Specify disk count through intuitive interface
  - Watch animated solution showing each move
  - Adjust speed to understand the recursive pattern

### UI & Layout
- **Intuitive Interface**
  - Three-row header for organized navigation
  - Algorithm-specific input fields that appear contextually
  - Reset/Start controls for easy experimentation

- **Split-Screen Design**
  - Left 70%: Real-time algorithm animations
  - Right 30%: Information panel with tabs for:
    - Pseudocode
    - Flowchart
    - Algorithm code with complexity analysis

## 📁 Project Structure

```
algorithm-visualizer/
├── config.py                # Configuration constants
├── main.py                  # Main entry point
├── algorithms/              # Algorithm implementations
│   ├── __init__.py
│   ├── pathfinding.py       # Dijkstra's algorithm
│   ├── queens.py            # N-Queens backtracking
│   ├── backtracking.py      # Knapsack and Subset Sum algorithms
│   └── hanoi.py             # Tower of Hanoi algorithm
├── ui/                      # User Interface components
│   ├── __init__.py
│   ├── buttons.py           # Button classes and UI elements
│   ├── drawing.py           # Drawing and animation functions
│   ├── ui_manager.py        # Header and UI layout functions
│   └── input_box.py         # Custom input box for user inputs
└── utils/                   # Utility functions
    ├── __init__.py
    └── helpers.py           # Grid and board initialization helpers
```

## 🔧 Installation

### Prerequisites
- Python 3.x
- Pygame

```bash
pip install pygame
```

### Clone the Repository
```bash
git clone https://github.com/vedant0718/algorithm-visualizer.git
cd algorithm-visualizer
```

### Run the Program
```bash
python main.py
```

## 📖 How to Use

### 1. Select a Mode
Choose from the header buttons: Pathfinding, N-Queens, Backtracking, or Hanoi

### 2. Configure Algorithm Parameters

#### Pathfinding
- Left-click: Toggle walls
- Right-click: Set start (green) and end (red) points
- Click "Start" to run Dijkstra's algorithm

#### N-Queens
- Enter board size in the input box
- Click "Update Board" to apply
- Click "Start" to run the backtracking solution

#### Backtracking
- Choose "Knapsack" or "Subset Sum" from sub-mode buttons
- For Knapsack:
  - Enter items as `weight:value` pairs (comma-separated)
  - Set knapsack capacity
  - Click "Update Knap"
- For Subset Sum:
  - Enter numbers (comma-separated)
  - Set target sum
  - Click "Update Subset"
- Click "Start" to run the algorithm

#### Tower of Hanoi
- Enter number of disks in the input box
- Click "Update Disks" to apply
- Click "Start" to watch the solution

### 3. Explore Additional Information
Use tabs in the right panel to view:
- **Pseudocode**: High-level algorithm overview
- **Flowchart**: Visual algorithm representation
- **Code**: Implementation with complexity details

### 4. Reset
Click "Reset" to start over with the current algorithm

## 🛠️ Customization

### Screen Resolution & Layout
Adjust parameters in `config.py`:
- `WIDTH`, `HEIGHT` for screen dimensions
- `HEADER_HEIGHT` for interface proportions

### Visual Elements
Customize in `config.py`:
- Fonts
- Colors
- Animation speeds

### Extend Functionality
- Add new algorithms in the `algorithms/` folder
- Create corresponding UI elements in `ui/drawing.py`

## 👥 Contributing
Contributions, issues, and feature requests are welcome! Feel free to:
- Open an issue for bugs or enhancement ideas
- Submit a pull request with improvements
- Suggest new algorithms to visualize

## 🙏 Acknowledgements
- [Pygame](https://www.pygame.org/) – The game development framework powering this visualizer
- Inspiration from various algorithm visualization tools in education