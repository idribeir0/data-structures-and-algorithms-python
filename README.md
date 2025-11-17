# Algorithms and Data Structures

This repository contains implementations of fundamental search and sorting algorithms in Python.

The objective is to develop strong algorithmic thinking, deepen computer science foundations, and build the technical maturity required for data engineering and international-level roles.

All code is written with clarity, performance awareness, and clean structure in mind.

## 📚 Project Structure

```
.
├── 01_linear_and_binary_search/
│   ├── linear_search.py               # Linear search implementation
│   ├── binary_search.py               # Binary search implementation
│   └── performance_comparison.py      # Performance comparison between algorithms
├── 02_sorting_algorithms/
│   ├── bubble_sort.py                 # Bubble sort implementation
│   └── merge_sort.py                  # Merge sort implementation
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

## 🔄 Sorting Algorithms

### 4. Bubble Sort

**Location:** `02_sorting_algorithms/bubble_sort.py`

Bubble sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

**Complexity**

- **Time:** O(n²)
- **Space:** O(1)

**Characteristics**

- Simple to understand and implement
- Inefficient for large datasets
- Stable sorting algorithm
- In-place sorting (requires only O(1) extra space)

**Run:**

```bash
cd 02_sorting_algorithms
python bubble_sort.py
```

### 5. Merge Sort

**Location:** `02_sorting_algorithms/merge_sort.py`

Merge sort is a divide-and-conquer algorithm that divides the input array into two halves, sorts them recursively, and then merges the sorted halves.

**Complexity**

- **Time:** O(n log n)
- **Space:** O(n)

**Characteristics**

- Efficient and stable
- Guaranteed O(n log n) performance
- Uses divide-and-conquer strategy
- Requires additional memory space

**Run:**

```bash
cd 02_sorting_algorithms
python merge_sort.py
```

## 📊 Algorithm Comparison Table

### Search Algorithms

| Algorithm | Time Complexity | Space Complexity | Requires Sorting |
|-----------|----------------|------------------|------------------|
| Linear Search | O(n) | O(1) | ❌ No |
| Binary Search | O(log n) | O(1) | ✅ Yes |

### Sorting Algorithms

| Algorithm | Time Complexity | Space Complexity | Stable | In-Place |
|-----------|----------------|------------------|--------|----------|
| Bubble Sort | O(n²) | O(1) | ✅ Yes | ✅ Yes |
| Merge Sort | O(n log n) | O(n) | ✅ Yes | ❌ No |

## 🎯 When to Use Each Algorithm

### Search Algorithms

**Use Linear Search when:**

- The list is unsorted
- The dataset is small
- Only one search is needed

**Use Binary Search when:**

- The list is sorted
- You must perform multiple searches
- You need high performance at scale

### Sorting Algorithms

**Use Bubble Sort when:**

- The dataset is very small
- You need a simple, easy-to-understand algorithm
- Memory is extremely constrained

**Use Merge Sort when:**

- You need guaranteed O(n log n) performance
- Stability is important (equal elements maintain their relative order)
- You can afford the extra O(n) memory space

## 📈 Practical Importance

Algorithmic thinking prepares you for system design, data engineering, and cloud computing.

Understanding time complexity makes you faster in interviews and more confident in code reviews.

These foundational skills scale into advanced CS topics: sorting algorithms, recursion, trees, graphs, and hashing.

## 🔮 Next Steps

Upcoming additions to this repository:

- More sorting algorithms (Quick Sort, Heap Sort, etc.)
- Hash tables
- Linked lists, stacks, queues
- Recursion examples
- Trees and graph traversal
- More performance benchmarks

## 👤 Author

Ione Ribeiro — Data Analyst focusing on building strong computer science fundamentals and preparing for advanced data engineering and global opportunities.

---

