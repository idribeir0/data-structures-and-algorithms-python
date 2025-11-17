import time
def merge(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) //2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
    
if __name__ == "__main__":
    data = list(range(1,20000))
    start_time = time.time()
    sorted_data = merge_sort(data)
    end_time = time.time()
    print("Sorted_data:" , sorted_data[:10])
        
        