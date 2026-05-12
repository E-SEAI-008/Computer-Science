class BSTNode:
    def __init__(self, key, data):
        self.key = key  # The value we compare (e.g., user_id, score)
        self.data = data  # The actual data (e.g., user object, record)
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        """Insert a new key-data pair into the BST."""
        if self.root is None:
            self.root = BSTNode(key, data)
        else:
            self._insert_recursive(self.root, key, data)

    def _insert_recursive(self, current_node, key, data):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = BSTNode(key, data)
            else:
                self._insert_recursive(current_node.left, key, data)
        else:  # key >= current_node.key goes to the right
            if current_node.right is None:
                current_node.right = BSTNode(key, data)
            else:
                self._insert_recursive(current_node.right, key, data)

    def in_order_traversal(self, node, visit_list):
        """In-order yields ascending order for a BST."""
        if node is None:
            return
        self.in_order_traversal(node.left, visit_list)
        visit_list.append((node.key, node.data))
        self.in_order_traversal(node.right, visit_list)

    def search(self, key):
        """Search for 'key' starting from the root.
        Return the data if found, None otherwise."""
        current = self.root
        while current is not None:
            if key == current.key:
                return current.data
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def _find_min(self, node):
        """Find the node with the minimum key in this subtree
        by going left as far as possible."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, key):
        """Delete 'key' from the tree if it exists."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        """Returns the (possibly new) root of the subtree after deletion."""
        if node is None:
            return None  # key not found, do nothing

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Found the node to delete
            # Case 1: no children
            if node.left is None and node.right is None:
                node = None
            # Case 2: one child
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            # Case 3: two children
            else:
                # Find in-order successor (minimum in right subtree)
                successor = self._find_min(node.right)
                # Copy successor's key and data
                node.key = successor.key
                node.data = successor.data
                # Delete successor from right subtree
                node.right = self._delete_recursive(node.right, successor.key)

        return node


# Example usage: User database indexed by user_id
bst = BinarySearchTree()

# Insert users (key=user_id, data=user info)
bst.insert(1005, {"name": "Alice", "email": "alice@example.com"})
bst.insert(1002, {"name": "Bob", "email": "bob@example.com"})
bst.insert(1008, {"name": "Charlie", "email": "charlie@example.com"})
bst.insert(1001, {"name": "Diana", "email": "diana@example.com"})
bst.insert(1004, {"name": "Eve", "email": "eve@example.com"})
bst.insert(1010, {"name": "Frank", "email": "frank@example.com"})

# Search for a user
user = bst.search(1004)
print(f"Found user: {user}")
# Expected: Found user: {'name': 'Eve', 'email': 'eve@example.com'}

user = bst.search(9999)
print(f"User not found: {user}")
# Expected: User not found: None

# In-order traversal (sorted by user_id)
users = []
bst.in_order_traversal(bst.root, users)
print("\nAll users sorted by ID:")
for user_id, user_data in users:
    print(f"  ID {user_id}: {user_data['name']}")
# Expected output:
#   ID 1001: Diana
#   ID 1002: Bob
#   ID 1004: Eve
#   ID 1005: Alice
#   ID 1008: Charlie
#   ID 1010: Frank

# Delete a user
bst.delete(1005)
users = []
bst.in_order_traversal(bst.root, users)
print("\nAfter deleting user 1005:")
for user_id, user_data in users:
    print(f"  ID {user_id}: {user_data['name']}")
