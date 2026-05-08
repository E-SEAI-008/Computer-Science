# ============================================================
# SECTION 1: HEIGHT CALCULATION EXAMPLES
# ============================================================

# Example 1: Simple tree
#       A
#      / \
#     B   C
#
# Calculate bottom-up:
# B is a leaf → height = 0
# C is a leaf → height = 0
# A has children → height = 1 + max(0, 0) = 1

# Example 2: Deeper tree
#       A
#      / \
#     B   C
#    / \  /
#   D  E F
#  /
# G
#
# Calculate bottom-up:
# G is a leaf → height = 0
# E is a leaf → height = 0
# F is a leaf → height = 0
# D has left child G → height = 1 + max(0, -1) = 1
# B has children D, E → height = 1 + max(1, 0) = 2
# C has left child F → height = 1 + max(0, -1) = 1
# A has children B, C → height = 1 + max(2, 1) = 3


# ============================================================
# SECTION 2: TREE TYPE EXAMPLES
# ============================================================

# General Tree (any number of children)
#         A
#       / | \
#      B  C  D
#     /|  |
#    E F  G

# Binary Tree (max 2 children)
#       A
#      / \
#     B   C
#    / \
#   D   E

# Binary Search Tree (BST) - sorted order
#       5
#      / \
#     3   8
#    / \   \
#   1   4   9


# ============================================================
# SECTION 3: TREE NODE & BINARY TREE CLASS
# ============================================================


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def __len__(self):
        """Return total number of nodes in the tree"""
        return self.count_nodes()

    # --- INSERTION METHODS ---

    def insert_left(self, current_node, new_value):
        """Insert a new node as the left child"""
        new_node = TreeNode(new_value)
        if current_node.left is None:
            current_node.left = new_node
        else:
            # Push existing left child down one level
            new_node.left = current_node.left
            current_node.left = new_node
        return new_node

    def insert_right(self, current_node, new_value):
        """Insert a new node as the right child"""
        new_node = TreeNode(new_value)
        if current_node.right is None:
            current_node.right = new_node
        else:
            # Push existing right child down one level
            new_node.right = current_node.right
            current_node.right = new_node
        return new_node

    # --- HEIGHT ---

    def height(self):
        """Calculate the height of the tree"""
        return self._height(self.root)

    def _height(self, node):
        """Private recursive helper for calculating height"""
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    # --- COUNT NODES ---

    def count_nodes(self):
        """Count total number of nodes in the tree"""
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        """Private recursive helper for counting nodes"""
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    # --- COUNT LEAVES ---

    def count_leaves(self):
        """Count leaf nodes (nodes with no children)"""
        return self._count_leaves(self.root)

    def _count_leaves(self, node):
        """Private recursive helper for counting leaves"""
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._count_leaves(node.left) + self._count_leaves(node.right)


# ============================================================
# SECTION 4: BUILD AND TEST THE TREE
# ============================================================

# Build the tree:
#      R
#     / \
#    A   B
#   / \ / \
#  C  D E  F
#        /
#       G

# Create tree with root 'R'
bt = BinaryTree("R")

# Insert children of root
node_a = bt.insert_left(bt.root, "A")
node_b = bt.insert_right(bt.root, "B")

# Insert children of A
bt.insert_left(node_a, "C")
bt.insert_right(node_a, "D")

# Insert children of B
bt.insert_left(node_b, "E")
node_f = bt.insert_right(node_b, "F")

# Insert child of F
bt.insert_left(node_f, "G")

# ============================================================
# SECTION 5: TEST OUTPUT
# ============================================================

# Test: Access node 'E'
print("root.right.left.value:", bt.root.right.left.value)  # Output: E

# Test tree properties
print(f"Tree height: {bt.height()}")  # Output: 3
print(f"Total nodes: {len(bt)}")  # Output: 8
print(f"Leaf nodes: {bt.count_leaves()}")  # Output: 4 (C, D, E, G)
