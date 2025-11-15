# Algorithms and Data Structures

This repository contains implementations of fundamental search algorithms in Python.

The objective is to develop strong algorithmic thinking, deepen computer science foundations, and build the technical maturity required for data engineering and international-level roles.

All code is written with clarity, performance awareness, and clean structure in mind.

## 📚 Project Structure

```
.
├── 01_linear_and_binary_search/
│   ├── linear_search.py               # Linear search implementation
│   ├── binary_search.py               # Binary search implementation
│   └── performance_comparison.py      # Performance comparison between algorithms
└── README.md
```

## 🔍 Implemented Algorithms

### 1. Linear Search

**Location:** `01_linear_and_binary_search/linear_search.py`

Linear search scans each element in sequence until it finds the target or reaches the end of the list.

**Complexity**

- **Time:** O(n)
- **Space:** O(1)

**Characteristics**

- Works on any list (sorted or not)
- Very simple to implement
- Inefficient for large datasets

**Run:**

```bash
cd 01_linear_and_binary_search
python linear_search.py
```

### 2. Binary Search

**Location:** `01_linear_and_binary_search/binary_search.py`

Binary search halves the search space at every iteration using the middle element.
Works only on sorted lists.

**Complexity**

- **Time:** O(log n)
- **Space:** O(1)

**Characteristics**

- Extremely efficient
- Ideal for large datasets
- Uses a divide-and-conquer strategy

**Run:**

```bash
cd 01_linear_and_binary_search
python binary_search.py
```

### 3. Performance Comparison

**Location:** `01_linear_and_binary_search/performance_comparison.py`

Benchmarks both algorithms using the same dataset, illustrating the dramatic speed difference between O(n) and O(log n).

**Run:**

```bash
cd 01_linear_and_binary_search
python performance_comparison.py
```

**Expected Output:**

- Result index
- Execution time of each algorithm
- Speedup factor

## 📊 Algorithm Comparison Table

| Algorithm | Time Complexity | Space Complexity | Requires Sorting |
|-----------|----------------|------------------|------------------|
| Linear Search | O(n) | O(1) | ❌ No |
| Binary Search | O(log n) | O(1) | ✅ Yes |

## 🎯 When to Use Each Algorithm

**Use Linear Search when:**

- The list is unsorted
- The dataset is small
- Only one search is needed

**Use Binary Search when:**

- The list is sorted
- You must perform multiple searches
- You need high performance at scale

## 📈 Practical Importance

Algorithmic thinking prepares you for system design, data engineering, and cloud computing.

Understanding time complexity makes you faster in interviews and more confident in code reviews.

These foundational skills scale into advanced CS topics: sorting algorithms, recursion, trees, graphs, and hashing.

## 🔮 Next Steps

Upcoming additions to this repository:

- Sorting algorithms (Merge Sort, Quick Sort, etc.)
- Hash tables
- Linked lists, stacks, queues
- Recursion examples
- Trees and graph traversal
- More performance benchmarks

## 👤 Author

Ione Ribeiro — Data Analyst focusing on building strong computer science fundamentals and preparing for advanced data engineering and global opportunities.

---

