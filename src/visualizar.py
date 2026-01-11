from antlr4 import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

class TreeVisualizer:
    def __init__(self, tree, parser, fontsize=8):
        self.tree = tree
        self.parser = parser
        self.fontsize = fontsize
        self.positions = {}
        self.current_y = 0
        self.x_spacing = 1.5
        self.y_spacing = 1.5
        
    def get_node_text(self, node):
        """Get display text for a node"""
        if isinstance(node, TerminalNode):
            return f'"{node.getText()}"'
        else:
            rule_index = node.getRuleIndex()
            return self.parser.ruleNames[rule_index]
    
    def calculate_positions(self, node, x=0, depth=0):
        """Calculate positions for all nodes"""
        self.current_y = max(self.current_y, depth)
        
        if isinstance(node, TerminalNode):
            self.positions[id(node)] = (x, -depth)
            return x + self.x_spacing
        
        # Process children first
        child_x = x
        children = [node.getChild(i) for i in range(node.getChildCount())]
        child_positions = []
        
        for child in children:
            child_x = self.calculate_positions(child, child_x, depth + 1)
            child_positions.append(self.positions[id(child)][0])
        
        # Place parent at midpoint of children
        if child_positions:
            parent_x = (child_positions[0] + child_positions[-1]) / 2
        else:
            parent_x = x
            
        self.positions[id(node)] = (parent_x, -depth)
        return child_x
    
    def draw_tree(self, figsize=(16, 10), save_path=None):
        """Draw the parse tree"""
        # Calculate positions
        self.calculate_positions(self.tree)
        
        # Create figure
        fig, ax = plt.subplots(figsize=figsize)
        ax.set_aspect('equal')
        
        # Draw edges and nodes
        self._draw_edges(self.tree, ax)
        self._draw_nodes(self.tree, ax)
        
        # Configure plot
        ax.axis('off')
        ax.autoscale()
        plt.margins(0.1)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Tree saved to {save_path}")
        
        plt.show()
    
    def _draw_edges(self, node, ax):
        """Draw edges between nodes"""
        if isinstance(node, TerminalNode):
            return
        
        parent_pos = self.positions[id(node)]
        
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            child_pos = self.positions[id(child)]
            
            ax.plot([parent_pos[0], child_pos[0]], 
                   [parent_pos[1], child_pos[1]], 
                   'k-', linewidth=1, zorder=1)
            
            self._draw_edges(child, ax)
    
    def _draw_nodes(self, node, ax):
        """Draw nodes"""
        pos = self.positions[id(node)]
        text = self.get_node_text(node)
        
        # Different colors for terminals and non-terminals
        if isinstance(node, TerminalNode):
            color = '#90EE90'  # Light green
        else:
            color = '#87CEEB'  # Sky blue
        
        # Draw box
        bbox = FancyBboxPatch((pos[0] - 0.4, pos[1] - 0.2), 0.8, 0.4,
                              boxstyle="round,pad=0.05", 
                              facecolor=color, 
                              edgecolor='black',
                              linewidth=1.5,
                              zorder=2)
        ax.add_patch(bbox)
        
        # Draw text
        ax.text(pos[0], pos[1], text, 
               ha='center', va='center',
               fontsize=self.fontsize,
               fontweight='bold',
               zorder=3)
        
        # Recursively draw children
        if not isinstance(node, TerminalNode):
            for i in range(node.getChildCount()):
                self._draw_nodes(node.getChild(i), ax)


# Example usage function
def visualize_parse_tree(parser, tree, figsize=(16, 10), fontsize=8, save_path=None):
    """
    Visualize ANTLR4 parse tree
    
    Args:
        parser: Your ANTLR4 parser instance
        tree: Parse tree from parser (usually parser.yourStartRule())
        figsize: Figure size tuple (width, height)
        fontsize: Font size for node labels
        save_path: Optional path to save the image (e.g., 'tree.png')
    """
    viz = TreeVisualizer(tree, parser, fontsize)
    viz.draw_tree(figsize, save_path)