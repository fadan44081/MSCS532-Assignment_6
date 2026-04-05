# ============================================================
# PART 2: ELEMENTARY DATA STRUCTURES
# Arrays, Matrices, Stack, Queue, Linked List
# ============================================================


# ============================================================
# CUSTOM ARRAY IMPLEMENTATION
# ============================================================

class CustomArray:
    """
    A simple custom array class that supports
    access, insertion, deletion, and display operations.
    """

    def __init__(self):
        self.data = []

    def access(self, index):
        # Access element at given index
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds.")
        return self.data[index]

    def insert(self, index, value):
        # Insert value at given index
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of bounds.")
        self.data.insert(index, value)

    def delete(self, index):
        # Delete element at given index
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds.")
        return self.data.pop(index)

    def display(self):
        # Display array
        print("Array contents:", self.data)


# ============================================================
# CUSTOM MATRIX IMPLEMENTATION
# ============================================================

class CustomMatrix:
    """
    A simple matrix using a 2D list.
    """

    def __init__(self, rows, cols, default_value=0):
        self.rows = rows
        self.cols = cols
        self.data = [[default_value for _ in range(cols)] for _ in range(rows)]

    def access(self, row, col):
        # Access matrix element
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Row or column out of bounds.")
        return self.data[row][col]

    def update(self, row, col, value):
        # Update matrix element
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Row or column out of bounds.")
        self.data[row][col] = value

    def display(self):
        # Display matrix
        print("Matrix contents:")
        for row in self.data:
            print(row)


# ============================================================
# STACK IMPLEMENTATION (LIFO)
# ============================================================

class Stack:
    """
    Stack implementation using list.
    """

    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack.")
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.data[-1]

    def display(self):
        print("Stack contents:", self.data)


# ============================================================
# QUEUE IMPLEMENTATION (FIFO)
# ============================================================

class Queue:
    """
    Queue implementation using list.
    """

    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue.")
        return self.data.pop(0)  # O(n)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.data[0]

    def display(self):
        print("Queue contents:", self.data)


# ============================================================
# SINGLY LINKED LIST IMPLEMENTATION
# ============================================================

class Node:
    """
    Node for linked list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    Singly linked list implementation.
    """

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def delete(self, value):
        current = self.head

        # If head needs to be removed
        if current and current.data == value:
            self.head = current.next
            return

        prev = None
        while current and current.data != value:
            prev = current
            current = current.next

        if current is None:
            print("Value not found.")
            return

        prev.next = current.next

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        elements = []

        while current:
            elements.append(current.data)
            current = current.next

        print("Linked List:", elements)


# ============================================================
# TESTING SECTION
# ============================================================

if __name__ == "__main__":

    print("=== ARRAY TESTS ===")
    arr = CustomArray()
    arr.insert(0, 10)
    arr.insert(1, 20)
    arr.insert(2, 30)
    arr.insert(1, 15)
    arr.display()
    print("Element at index 2:", arr.access(2))
    print("Deleted value:", arr.delete(1))
    arr.display()

    print("\n=== MATRIX TESTS ===")
    matrix = CustomMatrix(3, 3)
    matrix.update(0, 0, 5)
    matrix.update(1, 1, 10)
    matrix.update(2, 2, 15)
    matrix.display()
    print("Element at (1,1):", matrix.access(1, 1))

    print("\n=== STACK TESTS ===")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print("Top element:", stack.peek())
    print("Popped value:", stack.pop())
    stack.display()

    print("\n=== QUEUE TESTS ===")
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()
    print("Front element:", queue.front())
    print("Dequeued value:", queue.dequeue())
    queue.display()

    print("\n=== LINKED LIST TESTS ===")
    ll = SinglyLinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(5)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.display()

    print("Search 20:", ll.search(20))
    print("Search 100:", ll.search(100))

    ll.delete(20)
    print("After deleting 20:")
    ll.display()

    ll.delete(5)
    print("After deleting 5:")
    ll.display()

