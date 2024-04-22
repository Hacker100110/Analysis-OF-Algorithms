import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr, 0  # Return a tuple with the sorted array and runtime

    begin = time.time()
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    sorted_less, runtime_less = quicksort(less)
    sorted_greater, runtime_greater = quicksort(greater)
    result = sorted_less + [pivot] + sorted_greater
    print(f"Quick Sort Pass: {result}")
    end = time.time()
   
    runtime_total = runtime_less + runtime_greater + (end - begin)
   
    return result, runtime_total




def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0  # Return a tuple with the sorted array and runtime
   
    begin = time.time()
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left, runtime_left = merge_sort(left_half)
    sorted_right, runtime_right = merge_sort(right_half)
    result = merge(sorted_left, sorted_right)
    print(f"Merge Sort Pass: {result}")
    end = time.time()

    runtime_total = runtime_left + runtime_right + (end - begin)
   
    return result, runtime_total

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Input from user
n = int(input("Enter the number of elements in the list: "))
user_list = [int(input(f"Enter element {i + 1}: ")) for i in range(n)]

# Quicksort
print("\nQuicksort:")
sorted_quick, runtime_quick = quicksort(user_list.copy())
print(f"Sorted list by Quicksort: {sorted_quick}")
print(f"Quicksort Runtime: {runtime_quick} seconds")

# Merge sort
print("\nMerge Sort:")
sorted_merge, runtime_merge = merge_sort(user_list.copy())
print(f"Sorted list by Merge Sort: {sorted_merge}")
print(f"Mergesort Runtime: {runtime_merge} seconds")
