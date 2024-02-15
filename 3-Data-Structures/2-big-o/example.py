lst_of_numbers = list(range(1,1000001))

def constant_time_example(arr):
    step =0
    return arr[-1], step
# print(constant_time_example(lst_of_numbers))
# independent from the size of input that comes

def linear_time_example(arr):
    step =0 
    for num in arr:
        step += 1
        print(f"Num:{num} , Step{step}")

# linear_time_example(lst_of_numbers)
# one for one ration for operations and input size
bubble_sort_example_input = [64, 34, 25, 12, 22, 11, 90]
      
def bubble_sort(arr):
    step = 0
    n = len(arr)
    for i in range(n):
        step +=1
        for j in range(0, n-i-1):
            step +=1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(step)

# def my_loops(lst):
#     for n in lst:
#         print(n)
#     for j in lst:
#         print(j)


# bubble_sort(bubble_sort_example_input)
logarithmic_example_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def binary_search(arr, target):
    step = 0
    low, high = 0, len(arr) - 1
    while low <= high:
        step +=1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, step
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, step

# print(binary_search(logarithmic_example_input,7))

# O(n log n) - Linearithmic Time
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1