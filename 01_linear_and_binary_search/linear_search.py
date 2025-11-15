import time

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


if __name__ == "__main__":
    data = list(range(1,200000))
    target = 199999

    start_time = time.time()
    result = linear_search(data, target)
    end = time.time()

    print("Result: ", result)
    print("Time taken: ", end - start_time)