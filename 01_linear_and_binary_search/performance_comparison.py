import time
from linear_search import linear_search
from binary_search import binary_search

if __name__ == "__main__":
    # Large dataset
    data = list(range(0, 300000))
    target = 299999  # worst case for linear search

    # --- Linear Search ---
    start = time.time()
    linear_result = linear_search(data, target)
    linear_time = time.time() - start

    # --- Binary Search ---
    start = time.time()
    binary_result = binary_search(data, target)
    binary_time = time.time() - start

    # Results
    print("=== PERFORMANCE COMPARISON ===")
    print(f"Linear Search Result: {linear_result}")
    print(f"Linear Search Time:   {linear_time:.6f} seconds\n")

    print(f"Binary Search Result: {binary_result}")
    print(f"Binary Search Time:   {binary_time:.6f} seconds\n")

    # Optional: speedup factor
    speedup = linear_time / binary_time if binary_time > 0 else float('inf')
    print(f"Binary Search is approximately {speedup:.1f}x faster.")
