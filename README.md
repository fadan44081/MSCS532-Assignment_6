# MSCS 532 - Assignment 6  
## Medians, Order Statistics & Elementary Data Structures

---

## 📌 Overview

This project implements and analyzes:

### Part 1:
- Randomized Quickselect Algorithm
- Deterministic Selection (Median of Medians)
- Empirical performance comparison

### Part 2:
- Custom Array
- Matrix (2D Array)
- Stack (LIFO)
- Queue (FIFO)
- Singly Linked List

The goal is to understand both **algorithm efficiency** and **data structure behavior** through implementation and testing.

---

## ⚙️ Requirements

- Python 3.x
- No external libraries required (uses only built-in modules)

---

## ▶️ How to Run the Code

### Step 1: Download or Clone Repository

```bash

Step 2: Run Selection Algorithms (Part 1)
python selection_algorithms.py

This will:

Test Randomized Quickselect
Test Deterministic Selection
Display k-th smallest elements
Run empirical performance analysis
Step 3: Run Data Structures (Part 2)
python elementary_data_structures.py

This will:

Demonstrate Array operations
Display Matrix behavior
Test Stack (push/pop)
Test Queue (enqueue/dequeue)
Test Linked List operations

📊 Sample Output
Selection Algorithms:
Correct k-th smallest values for:
Normal arrays
Arrays with duplicates
Empirical Analysis:

Shows execution time comparison such as:

Size    Distribution   Quickselect   Deterministic
10000   random         0.003860      0.009316

🧠 Summary of Findings
1. Selection Algorithms
Randomized Quickselect
Faster in practice
Average time: O(n)
Slightly unpredictable (random pivot)
Deterministic Selection (Median of Medians)
Guaranteed O(n) worst-case
Slower due to additional computations
More stable but less efficient in practice

👉 Conclusion:
Randomized Quickselect is preferred in real-world applications due to better performance, while deterministic selection is useful when worst-case guarantees are required.

2. Data Structures
Arrays
Fast access (O(1))
Slow insertion/deletion (O(n))
Matrix
Efficient 2D data storage
Constant-time access
Stack (LIFO)
Push/Pop: O(1)
Used in recursion and undo operations
Queue (FIFO)
Enqueue: O(1)
Dequeue: O(n) in this implementation
Used in scheduling and BFS
Linked List
Dynamic structure
Efficient insert/delete
Slower access (O(n))

⚖️ Key Trade-offs
Structure	Advantage	Disadvantage
Array	Fast access	Slow modification
Linked List	Flexible size	Slow access
Stack	Simple operations	Limited use case
Queue	Order processing	Slower dequeue (list-based)

📚 What This Project Demonstrates
Understanding of order statistics algorithms
Difference between theoretical vs practical performance
Implementation of core data structures
Analysis of time complexity and efficiency

👨‍💻 Author
Fathiya Adan
MSCS 532 - Algorithms and Data Structures
