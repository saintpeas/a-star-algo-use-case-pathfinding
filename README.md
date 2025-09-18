# A* Pathfinding Visualizer

An interactive Python application demonstrating the A* pathfinding algorithm with real-time visualization using Matplotlib. Click to set start and goal points, and watch the algorithm find the optimal path through a customizable grid network in Visual Studio Code.

[![Python 3.7+](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## Features

- **Interactive Grid Interface**: Click to set start (green) and goal (red) points.
- **Real-time Pathfinding**: Automatic path calculation using the A* algorithm.
- **Visual Path Display**: Clear visualization of the found path with directional arrows.
- **Customizable Obstacles**: Pre-defined obstacles and random grid generation.
- **Graph Visualization**: Intuitive grid layout showing available paths and nodes.
- **Control Buttons**: User-friendly interface for clearing selections and generating new grids.

## Algorithm Overview

The A* (A-star) algorithm is a graph traversal and path search algorithm that finds the shortest path between nodes using a heuristic function for efficiency.

### Key Components
- **g(n)**: Cost from start node to current node.
- **h(n)**: Heuristic estimate from current node to goal (Manhattan distance).
- **f(n)**: Total cost estimate (g(n) + h(n)).

## Installation in VS Code

### Prerequisites
- **Python 3.7+**: Install from [python.org](https://www.python.org/downloads/) and ensure it’s added to PATH.
- **Git**: Install from [git-scm.com](https://git-scm.com/downloads) or your package manager (see above for details).
- **Python Extensions for VS Code**:
  - Install the "Python" extension by Microsoft in VS Code (Ctrl+Shift+X, search for "Python").
  - Optionally, install "Pylance" for enhanced Python support.
- **Dependencies**:
  ```bash
  pip install matplotlib numpy
  ```

### Clone the Repository
1. Open VS Code.
2. Open the integrated terminal (Ctrl+` or View > Terminal).
3. Clone the repository:
   ```bash
   git clone https://github.com/saintpeas/a-star-algo-use-case-pathfinding.git
   cd a-star-algo-use-case-pathfinding
   ```
4. Open the project folder in VS Code:
   - File > Open Folder, select the `a-star-algo-use-case-pathfinding` directory.

### Configure Python Environment
1. Select the Python interpreter:
   - Press Ctrl+Shift+P, type "Python: Select Interpreter," and choose your Python 3.7+ installation.
2. Install dependencies in the terminal:
   ```bash
   pip install matplotlib numpy
   ```

## Usage in VS Code

### Running the Visualizer
1. Open `astar_pathfinding.py` in VS Code.
2. Run the script:
   - Right-click the file and select "Run Python File in Terminal."
   - Or, in the terminal, run:
     ```bash
     python astar_pathfinding.py
     ```

### How to Use
1. **Set Start Point**: Click a blue node to set the start position (appears green).
2. **Set Goal Point**: Click another node to set the goal position (appears red).
3. **View Path**: The algorithm automatically calculates and displays the shortest path in red.
4. **Reset**: Click the "Clear" button to reset start and goal points.
5. **Generate New Grid**: Use the "Random Grid" button for a new layout with random obstacles.

### Interactive Controls
- **Left Click**: Set start/goal points or reset selection.
- **Clear Button**: Remove current start and goal points.
- **Find Path Button**: Manually trigger pathfinding (automatic by default).
- **Random Grid Button**: Generate a new grid with random obstacles.

## `astar_pathfinding.py` Structure

- **Path class**: Represents connections between nodes.
- **Node class**: A* algorithm node with f, g, h values.
- **build_graph()**: Creates adjacency list from paths.
- **astar_search()**: Core A* algorithm implementation.
- **calculate_path()**: Main pathfinding interface.
- **AStarVisualizer**: Interactive Matplotlib visualization.
  - Grid creation and obstacle management.
  - Click event handling.
  - Path visualization and drawing.
  - UI controls and buttons.

## A* Implementation

- **Priority Queue**: Uses `heapq` for efficient open list management.
- **Manhattan Distance**: Heuristic function for grid-based pathfinding.
- **Graph Representation**: Adjacency list for efficient neighbor lookup.

## Demo
Watch a demo of the application in action: [Google Drive Demo Video](https://drive.google.com/file/d/1D7G-svOo40RUnJ-nlzynGmYMUG_TtmTS/view?usp=sharing)

## Example Output

```
A* Pathfinding Visualizer
==============================
Instructions:
1. Click on any blue node to set the START point (green)
2. Click on another node to set the GOAL point (red)
3. The path will be calculated automatically
4. Use buttons to clear selection or generate random grids
5. Blue lines show available paths, red line shows the found path

Start point set to: (1, 1)
Goal point set to: (8, 8)
Path found: [(1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]
Path length: 15 nodes
Path cost: 14 steps
```

## Debugging in VS Code

- Set breakpoints in `astar_pathfinding.py` by clicking in the gutter next to line numbers.
- Press F5 or select "Run > Start Debugging" to debug the script.
- Use the Debug Console to inspect variables and step through the A* algorithm.

## Troubleshooting

- **Git not recognized**: Ensure Git is installed and added to PATH (see above). Restart VS Code after updating PATH.
- **Python not found**: Verify the Python interpreter is set correctly in VS Code.
- **Matplotlib window issues**: If the visualizer window doesn’t appear, ensure `matplotlib` is installed and try running in a new terminal.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- A* algorithm by Peter Hart, Nils Nilsson, and Bertram Raphael (1968).
- Matplotlib for visualization capabilities.
- Pathfinding and game development community for inspiration.

Made with ❤️ and Python

If you find this project helpful, please give it a ⭐ on GitHub!
