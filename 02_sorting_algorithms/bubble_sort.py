import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



if __name__ == "__main__":
    data = list(range(1,20000))
    start_time = time.time()
    sorted_data = bubble_sort(data)
    end_time = time.time()
    print("Sorted_data: ", sorted_data[:10])
    print("Time taken: ", end_time - start_time)
