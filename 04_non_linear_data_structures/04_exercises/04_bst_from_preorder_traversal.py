# Approach 1
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time Complexity: O(N)
# Where N is the number of nodes (length of the preorder array). We process each element exactly once by adjusting the min_val and max_val bounds.
# Space Complexity: O(N) auxiliary space
# In the worst case (a completely skewed tree) due to the recursive call stack. In the average case of a balanced tree, it would be O(log N).
def bst_from_preorder(preorder):
    if not preorder:
        return None

    idx = 0

    def build(min_val, max_val):
        nonlocal idx

        if idx >= len(preorder) or not (min_val < preorder[idx] < max_val):
            return None

        val = preorder[idx]
        node = TreeNode(val)

        idx += 1

        node.left = build(min_val, val)

        node.right = build(val, max_val)

        return node

    return build(float("-inf"), float("inf"))


# Time Complexity: O(N)
# We visit every node in the tree once.
# Auxiliary Space: O(N)
# The queue holds nodes level by level. At the widest part of a balanced tree (the bottom), it holds roughly N/2 nodes.
def tree_to_list_level_order(root):
    if not root:
        return []

    result = []

    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")

    while result and result[-1] == "null":
        result.pop()

    return result


root1 = bst_from_preorder([8, 5, 1, 7, 10, 12])
print("Example 1 Output:", tree_to_list_level_order(root1))

root2 = bst_from_preorder([1, 3])
print("Example 2 Output:", tree_to_list_level_order(root2))


# preorder = [8, 5, 1, 7, 10, 12]
# idx = 0

# Call: build(-∞, +∞)
#   idx=0, val=8, range=(-∞, +∞) ✓
#   Create node(8), idx=1

#   Build left of 8: build(-∞, 8)
#     idx=1, val=5, range=(-∞, 8) ✓
#     Create node(5), idx=2

#     Build left of 5: build(-∞, 5)
#       idx=2, val=1, range=(-∞, 5) ✓
#       Create node(1), idx=3

#       Build left of 1: build(-∞, 1)
#         idx=3, val=7, range=(-∞, 1) ✗ (7 > 1)
#         return None

#       Build right of 1: build(1, 5)
#         idx=3, val=7, range=(1, 5) ✗ (7 > 5)
#         return None

#       Return node(1)

#     Build right of 5: build(5, 8)
#       idx=3, val=7, range=(5, 8) ✓
#       Create node(7), idx=4

#       Build left of 7: build(5, 7)
#         idx=4, val=10, range=(5, 7) ✗ (10 > 7)
#         return None

#       Build right of 7: build(7, 8)
#         idx=4, val=10, range=(7, 8) ✗ (10 > 8)
#         return None

#       Return node(7)

#     Return node(5) with left=node(1), right=node(7)

#   Build right of 8: build(8, +∞)
#     idx=4, val=10, range=(8, +∞) ✓
#     Create node(10), idx=5

#     Build left of 10: build(8, 10)
#       idx=5, val=12, range=(8, 10) ✗ (12 > 10)
#       return None

#     Build right of 10: build(10, +∞)
#       idx=5, val=12, range=(10, +∞) ✓
#       Create node(12), idx=6

#       Build left of 12: build(10, 12)
#         idx=6, out of bounds
#         return None

#       Build right of 12: build(12, +∞)
#         idx=6, out of bounds
#         return None

#       Return node(12)

#     Return node(10) with right=node(12)

#   Return node(8) with left=node(5), right=node(10)

# Final tree:
#        8
#       / \
#      5   10
#     / \    \
#    1   7   12


# Approach 2
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time Complexity: O(N)
# Where N is the number of nodes. We iterate through the array once. The inner while loop pops items from the stack, but each node is pushed and popped at most once across the entire run. This amortizes to O(1) time per node.
# Space Complexity: O(N) auxiliary space
# In the worst case (a completely left-skewed tree), all nodes will be pushed onto the stack before any are popped.
def bst_from_preorder_iterative(preorder):
    if not preorder:
        return None

    root = TreeNode(preorder[0])
    stack = [root]

    for val in preorder[1:]:
        node = TreeNode(val)

        if val < stack[-1].val:
            stack[-1].left = node
        else:
            parent = None
            while stack and stack[-1].val < val:
                parent = stack.pop()
            parent.right = node

        stack.append(node)
    return root


# Time Complexity: O(N)
# Auxiliary Space: O(N)
def tree_to_list_level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")

    while result and result[-1] == "null":
        result.pop()

    return result


root1 = bst_from_preorder_iterative([8, 5, 1, 7, 10, 12])
print("Example 1 Output:", tree_to_list_level_order(root1))

root2 = bst_from_preorder_iterative([1, 3])
print("Example 2 Output:", tree_to_list_level_order(root2))

# preorder = [8, 5, 1, 7, 10, 12]

# Step 1: root = node(8), stack = [8]

# Step 2: val = 5
#   5 < 8, so 5 is left child of 8
#   8.left = node(5)
#   stack = [8, 5]

# Step 3: val = 1
#   1 < 5, so 1 is left child of 5
#   5.left = node(1)
#   stack = [8, 5, 1]

# Step 4: val = 7
#   7 > 1, pop 1 (parent = 1)
#   7 > 5, pop 5 (parent = 5)
#   7 < 8, stop
#   5.right = node(7)
#   stack = [8, 7]

# Step 5: val = 10
#   10 > 7, pop 7 (parent = 7)
#   10 > 8, pop 8 (parent = 8)
#   stack empty, stop
#   8.right = node(10)
#   stack = [10]

# Step 6: val = 12
#   12 > 10, pop 10 (parent = 10)
#   stack empty, stop
#   10.right = node(12)
#   stack = [12]

# Final tree:
#        8
#       / \
#      5   10
#     / \    \
#    1   7   12
