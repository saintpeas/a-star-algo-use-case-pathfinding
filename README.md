# A* Pathfinding Visualizer

An interactive Python application that demonstrates the A* pathfinding algorithm with real-time visualization using Matplotlib. Click to set start and goal points, and watch as the algorithm finds the optimal path through a customizable grid network.

[![Python 3.7+](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## Features

- **Interactive Grid Interface**: Click to set start (green) and goal (red) points.
- **Real-time Pathfinding**: Automatic path calculation using the A* algorithm.
- **Visual Path Display**: Clear visualization of the found path with directional arrows.
- **Customizable Obstacles**: Pre-defined obstacles and random grid generation.
- **Graph Visualization**: See available paths and nodes in an intuitive grid layout.
- **Control Buttons**: Easy-to-use interface for clearing selections and generating new grids.

## Algorithm Overview

The A* (A-star) algorithm is a graph traversal and path search algorithm that finds the shortest path between nodes. It uses a heuristic function to guide the search, making it more efficient than algorithms like Dijkstra's algorithm.

### Key Components
- **g(n)**: Cost from start node to current node.
- **h(n)**: Heuristic estimate from current node to goal (Manhattan distance).
- **f(n)**: Total cost estimate (g(n) + h(n)).

## Installation

### Prerequisites
```bash
pip install matplotlib numpy
```

### Clone the Repository
```bash
git clone https://github.com/saintpeas/a-star-algo-use-case-pathfinding.git
cd a-star-algo-use-case-pathfinding
```

## Usage

### Running the Visualizer
```bash
python astar_visualizer.py
```

### How to Use
1. **Set Start Point**: Click on any blue node to set the starting position (appears in green).
2. **Set Goal Point**: Click on another node to set the goal position (appears in red).
3. **View Path**: The algorithm automatically calculates and displays the shortest path in red.
4. **Reset**: Use the "Clear" button to reset start and goal points.
5. **Generate New Grid**: Use "Random Grid" to create a new layout with random obstacles.

### Interactive Controls
- **Left Click**: Set start/goal points or reset selection.
- **Clear Button**: Remove current start and goal points.
- **Find Path Button**: Manually trigger pathfinding (automatic by default).
- **Random Grid Button**: Generate a new grid with random obstacles.

## `astar_visualizer.py` Structure

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

The implementation uses:
- **Priority Queue**: `heapq` for efficient open list management.
- **Manhattan Distance**: Heuristic function for grid-based pathfinding.
- **Graph Representation**: Adjacency list for efficient neighbor lookup.

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- A* algorithm originally developed by Peter Hart, Nils Nilsson, and Bertram Raphael in 1968.
- Matplotlib for excellent visualization capabilities.
- The pathfinding and game development community for inspiration.

Made with ❤️ and Python

If you find this project helpful, please give it a ⭐ on GitHub!
