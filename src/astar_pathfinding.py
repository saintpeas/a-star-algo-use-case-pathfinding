import heapq
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Button
import numpy as np

class Path:
    """Simple path class to represent connections between nodes"""
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Node: 
    # A simplified Node class for A*
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0 
        self.h = 0 
        self.f = 0 
    
    def __eq__(self, other):
        return self.position == other.position
    
    def __lt__(self, other):
        return self.f < other.f

def build_graph(available_paths: list): \
    """
    Builds an adjacency list representation of a graph from available paths.
    """
    graph = {}
    
    for path in available_paths:
        start_node = (path.x1, path.y1)
        end_node = (path.x2, path.y2)
        
        if start_node not in graph:
            graph[start_node] = []
        if end_node not in graph:
            graph[end_node] = []
        
        graph[start_node].append(end_node)
        graph[end_node].append(start_node)
    
    return graph

def astar_search(graph, start, end): 
    
    # A* search algorithm implementation
    start_node = Node(None, start)
    end_node = Node(None, end)
    
    open_list = []
    closed_list = set()

    heapq.heappush(open_list, (start_node.f, start_node))

    while open_list:
        f_val, current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node.position == end_node.position:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        neighbors = graph.get(current_node.position, [])

        for neighbor_pos in neighbors:
            if neighbor_pos in closed_list:
                continue
            
            new_node = Node(current_node, neighbor_pos)
            
            new_node.g = current_node.g + 1
            new_node.h = abs(new_node.position[0] - end_node.position[0]) + \
                         abs(new_node.position[1] - end_node.position[1])
            new_node.f = new_node.g + new_node.h
            
            in_open = any(open_node.position == new_node.position and open_node.g <= new_node.g for _, open_node in open_list)
            
            if not in_open:
                heapq.heappush(open_list, (new_node.f, new_node))

    return None

def calculate_path(start_node: dict, goal_node: dict, available_paths: list):
    """
    Calculates the shortest path using A* on a predefined graph.
    """
    graph = build_graph(available_paths)

    start = (start_node['x'], start_node['y'])
    end = (goal_node['x'], goal_node['y'])
    
    if start not in graph or end not in graph:
        return {"error": "Start or goal node is not a part of the available paths."}

    path = astar_search(graph, start, end)

    if path:
        return path
    else:
        return {"error": "No path found between the nodes."}

class AStarVisualizer:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.ax.set_aspect('equal')
        self.ax.grid(True, alpha=0.3)
        self.ax.set_title('A* Pathfinding\nClick to set start (green) and goal (red) points')
        
        # State variables
        self.start_point = None
        self.goal_point = None
        self.available_paths = []
        self.graph = {}
        self.current_path = None
        
        # Visual elements
        self.path_lines = []
        self.node_circles = []
        self.path_line = None
        self.start_marker = None
        self.goal_marker = None
        
        # Create sample grid paths
        self.create_sample_paths()
        
        # Set up event handlers
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        
        # Add buttons
        self.setup_buttons()
        
        # Initial drawing
        self.draw_graph()
        
    def create_sample_paths(self):
        """Create a sample grid of paths for demonstration"""
        self.available_paths = []
        
        # Create a 10x10 grid with some paths
        for x in range(10):
            for y in range(10):
                # Horizontal connections
                if x < 9:
                    self.available_paths.append(Path(x, y, x+1, y))
                # Vertical connections
                if y < 9:
                    self.available_paths.append(Path(x, y, x, y+1))
        
        # Remove some paths to create obstacles
        obstacles = [
            # Create some walls
            (3, 3, 3, 4), (3, 4, 3, 5), (3, 5, 3, 6),
            (6, 2, 7, 2), (7, 2, 8, 2),
            (5, 6, 6, 6), (6, 6, 7, 6), (7, 6, 8, 6),
        ]
        
        # Remove obstacle paths
        self.available_paths = [path for path in self.available_paths 
                              if not any((path.x1, path.y1, path.x2, path.y2) == obs or 
                                       (path.x2, path.y2, path.x1, path.y1) == obs 
                                       for obs in obstacles)]
        
        self.graph = build_graph(self.available_paths)
    
    def setup_buttons(self):
        """Setup control buttons"""
        # Clear button
        ax_clear = plt.axes([0.02, 0.02, 0.1, 0.04])
        self.btn_clear = Button(ax_clear, 'Clear')
        self.btn_clear.on_clicked(self.clear_selection)
        
        # Find path button
        ax_find = plt.axes([0.13, 0.02, 0.1, 0.04])
        self.btn_find = Button(ax_find, 'Find Path')
        self.btn_find.on_clicked(self.find_path)
        
        # Random paths button
        ax_random = plt.axes([0.24, 0.02, 0.12, 0.04])
        self.btn_random = Button(ax_random, 'Random Grid')
        self.btn_random.on_clicked(self.create_random_paths)
    
    def draw_graph(self):
        """Draw the graph structure"""
        self.ax.clear()
        self.ax.set_xlim(-0.5, 9.5)
        self.ax.set_ylim(-0.5, 9.5)
        self.ax.set_aspect('equal')
        self.ax.grid(True, alpha=0.3)
        self.ax.set_title('A* Pathfinding\nClick to set start (green) and goal (red) points')
        
        # Draw all available paths
        for path in self.available_paths:
            self.ax.plot([path.x1, path.x2], [path.y1, path.y2], 
                        'b-', alpha=0.3, linewidth=1)
        
        # Draw all nodes
        all_nodes = set()
        for path in self.available_paths:
            all_nodes.add((path.x1, path.y1))
            all_nodes.add((path.x2, path.y2))
        
        for node in all_nodes:
            circle = plt.Circle(node, 0.1, color='lightblue', alpha=0.7)
            self.ax.add_patch(circle)
        
        # Redraw start and goal if they exist
        if self.start_point:
            self.start_marker = plt.Circle(self.start_point, 0.15, color='green', zorder=5)
            self.ax.add_patch(self.start_marker)
            self.ax.text(self.start_point[0], self.start_point[1] + 0.3, 'START', 
                        ha='center', fontweight='bold', color='green')
        
        if self.goal_point:
            self.goal_marker = plt.Circle(self.goal_point, 0.15, color='red', zorder=5)
            self.ax.add_patch(self.goal_marker)
            self.ax.text(self.goal_point[0], self.goal_point[1] + 0.3, 'GOAL', 
                        ha='center', fontweight='bold', color='red')
        
        # Redraw path if it exists
        if self.current_path:
            self.draw_path(self.current_path)
        
        self.fig.canvas.draw()
    
    def on_click(self, event):
        """Handle mouse clicks to set start and goal points"""
        if event.inaxes != self.ax:
            return
        
        # Round to nearest integer coordinates
        x, y = round(event.xdata), round(event.ydata)
        
        # Check if the clicked point is a valid node
        if (x, y) not in self.graph:
            print(f"Point ({x}, {y}) is not a valid node!")
            return
        
        if self.start_point is None:
            self.start_point = (x, y)
            print(f"Start point set to: {self.start_point}")
        elif self.goal_point is None:
            self.goal_point = (x, y)
            print(f"Goal point set to: {self.goal_point}")
            # Automatically find path when both points are set
            self.find_path(None)
        else:
            # Reset and set new start point
            self.clear_selection(None)
            self.start_point = (x, y)
            print(f"Start point reset to: {self.start_point}")
        
        self.draw_graph()
    
    def find_path(self, event):
        """Find and display the path"""
        if not self.start_point or not self.goal_point:
            print("Please set both start and goal points!")
            return
        
        start_dict = {'x': self.start_point[0], 'y': self.start_point[1]}
        goal_dict = {'x': self.goal_point[0], 'y': self.goal_point[1]}
        
        result = calculate_path(start_dict, goal_dict, self.available_paths)
        
        if isinstance(result, dict) and 'error' in result:
            print(f"Error: {result['error']}")
            self.current_path = None
        else:
            self.current_path = result
            print(f"Path found: {result}")
            self.draw_path(result)
    
    def draw_path(self, path):
        """Draw the found path"""
        if not path or len(path) < 2:
            return
        
        # Draw path as thick red line
        path_x = [point[0] for point in path]
        path_y = [point[1] for point in path]
        
        self.ax.plot(path_x, path_y, 'r-', linewidth=4, alpha=0.7, zorder=3)
        
        # Add arrows to show direction
        for i in range(len(path) - 1):
            dx = path[i+1][0] - path[i][0]
            dy = path[i+1][1] - path[i][1]
            self.ax.arrow(path[i][0], path[i][1], dx*0.3, dy*0.3,
                         head_width=0.1, head_length=0.1, fc='darkred', ec='darkred', zorder=4)
        
        self.fig.canvas.draw()
        
        # Print path info
        print(f"Path length: {len(path)} nodes")
        print(f"Path cost: {len(path) - 1} steps")
    
    def clear_selection(self, event):
        """Clear start and goal points"""
        self.start_point = None
        self.goal_point = None
        self.current_path = None
        print("Selection cleared!")
        self.draw_graph()
    
    def create_random_paths(self, event):
        """Create a random grid with obstacles"""
        import random
        
        self.available_paths = []
        
        # Create base grid
        for x in range(10):
            for y in range(10):
                # Horizontal connections
                if x < 9 and random.random() > 0.2:  # 20% chance to block
                    self.available_paths.append(Path(x, y, x+1, y))
                # Vertical connections
                if y < 9 and random.random() > 0.2:  # 20% chance to block
                    self.available_paths.append(Path(x, y, x, y+1))
        
        self.graph = build_graph(self.available_paths)
        self.clear_selection(None)
        print("Random grid generated!")
    
    def show(self):
        """Display the visualization"""
        plt.tight_layout()
        plt.show()

def main():
    print("A* Pathfinding Visualizer")
    print("=" * 30)
    print("Instructions:")
    print("1. Click on any blue node to set the START point (green)")
    print("2. Click on another node to set the GOAL point (red)")
    print("3. The path will be calculated automatically")
    print("4. Use buttons to clear selection or generate random grids")
    print("5. Blue lines show available paths, red line shows the found path")
    print()
    
    visualizer = AStarVisualizer()
    visualizer.show()

if __name__ == "__main__":
    main()
