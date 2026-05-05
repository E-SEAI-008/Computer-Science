# =============================================================================
# SINGLY LINKED LIST
# =============================================================================


class Node:
    """A single element in the linked list."""

    def __init__(self, value):
        self.value = value  # The data
        self.next = None  # Pointer to the next node


class SinglyLinkedList:
    """A Singly Linked List with head and tail pointers for optimized appending."""

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        """Allows printing the list directly (e.g., print(my_list)) — O(n)"""
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.value))
            current = current.next
        values.append("None")
        return " → ".join(values)

    def __contains__(self, value):
        """Allows the use of the 'in' keyword (e.g., if 5 in my_list:) — O(n)"""
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value):
        """Add a new node to the end of the list — O(1)"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, value):
        """Add a new node to the front of the list — O(1)"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def delete(self, value):
        """Remove the first node with the given value — O(n)
        Returns True if successful, False if the value was not found."""
        if self.head is None:
            return False

        # Special case 1: Deleting the head
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True

        # Walk the list to find the node BEFORE the target
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                return True
            current = current.next

        return False


# =============================================================================
# SINGLY LINKED LIST — Tests
# =============================================================================
print("Singly-Linked List:")

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    sll.append(30)
    sll.prepend(0)

    print(f"Initial list:          {sll}")  # 0 → 10 → 20 → 30 → None
    print(f"Is 20 in the list?     {20 in sll}")  # True
    print(f"Is 99 in the list?     {99 in sll}")  # False

    sll.delete(20)
    print(f"After deleting 20:     {sll}")  # 0 → 10 → 30 → None

    sll.delete(30)
    print(f"After deleting 30:     {sll}")  # 0 → 10 → None
    print(f"Current tail value:    {sll.tail.value}")  # 10

    sll.delete(0)
    print(f"After deleting 0:      {sll}")  # 10 → None


# =============================================================================
# DOUBLY LINKED LIST
# =============================================================================


class DoublyNode:
    """A single element in the doubly linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """A Doubly Linked List with head and tail pointers."""

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        """Allows print(dll) for forward traversal — O(n)"""
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.value))
            current = current.next
        values.append("None")
        return " ⇄ ".join(values)

    def __contains__(self, value):
        """Allows the use of the 'in' keyword (e.g., if 5 in my_list:) — O(n)"""
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def display_backward(self):
        """Returns a string representation from tail to head — O(n)"""
        values = []
        current = self.tail
        while current is not None:
            values.append(str(current.value))
            current = current.prev
        values.append("None")
        return " ⇄ ".join(values)

    def append(self, value):
        """Add a new node to the end — O(1)"""
        new_node = DoublyNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail  # new node's prev points to old tail
        self.tail.next = new_node  # old tail's next points to new node
        self.tail = new_node  # update tail to the new node

    def prepend(self, value):
        """Add a new node to the front — O(1)"""
        new_node = DoublyNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head  # new node's next points to old head
        self.head.prev = new_node  # old head's prev points to new node
        self.head = new_node  # update head to the new node

    def delete(self, value):
        """Remove the first node with the given value — O(n)
        Returns True if successful, False if not found."""
        current = self.head
        while current is not None:
            if current.value == value:
                if current.prev is not None:  # 1. Rewire previous node
                    current.prev.next = current.next
                else:
                    self.head = current.next  #    or update head

                if current.next is not None:  # 2. Rewire next node
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev  #    or update tail

                current.next = None  # 3. Isolate deleted node
                current.prev = None
                return True
            current = current.next
        return False


# =============================================================================
# DOUBLY LINKED LIST — Tests
# =============================================================================
print("\nDoubly-Linked List:")

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)

    print(f"Forward:               {dll}")  # 0 ⇄ 1 ⇄ 2 ⇄ 3 ⇄ None
    print(f"Backward:              {dll.display_backward()}")  # 3 ⇄ 2 ⇄ 1 ⇄ 0 ⇄ None

    dll.delete(2)
    print(f"After deleting 2:      {dll}")  # 0 ⇄ 1 ⇄ 3 ⇄ None

    dll.delete(0)
    print(f"After deleting 0:      {dll}")  # 1 ⇄ 3 ⇄ None

    dll.delete(3)
    print(f"After deleting 3:      {dll}")  # 1 ⇄ None
