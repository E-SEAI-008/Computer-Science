class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert_left(self, current_node, new_value):
        new_node = TreeNode(new_value)
        if current_node.left is None:
            current_node.left = new_node
        else:
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, new_value):
        new_node = TreeNode(new_value)
        if current_node.right is None:
            current_node.right = new_node
        else:
            new_node.right = current_node.right
            current_node.right = new_node

    def post_order_traversal(self, start_node, visit_list, depth=0):
        indent = "  " * depth

        if start_node is None:
            print(f"{indent}→ None, returning")
            return

        print(f"{indent}→ Entered: {start_node.value}")

        # 1) Traverse left subtree
        print(f"{indent}  Going LEFT from {start_node.value}")
        self.post_order_traversal(start_node.left, visit_list, depth + 1)

        # 2) Traverse right subtree
        print(f"{indent}  Going RIGHT from {start_node.value}")
        self.post_order_traversal(start_node.right, visit_list, depth + 1)

        # 3) Visit current node
        print(f"{indent}  Processing: {start_node.value}")
        visit_list.append(start_node.value)
        print(f"{indent}← Done with {start_node.value}")


# -- Now build the tree --

#      R
#     / \
#    A   B
#   / \ / \
#  C  D E  F
#        /
#       G

# Create a tree with root 'R'
bt = BinaryTree("R")
# Insert 'A' as left child of 'R', and 'B' as right child of 'R'
bt.insert_left(bt.root, "A")  # nodeA
bt.insert_right(bt.root, "B")  # nodeB
# Get references to the newly inserted nodes for further insertions
nodeA = bt.root.left
nodeB = bt.root.right
# Insert 'C' and 'D' under 'A'
bt.insert_left(nodeA, "C")
bt.insert_right(nodeA, "D")
# Insert 'E' and 'F' under 'B'
bt.insert_left(nodeB, "E")
bt.insert_right(nodeB, "F")
# Insert 'G' under 'F' (as left child)
nodeF = nodeB.right
bt.insert_left(nodeF, "G")
# Test Post-order traversal
visit_order = []
bt.post_order_traversal(bt.root, visit_order)
print("Post-order traversal (DFS):", visit_order)
