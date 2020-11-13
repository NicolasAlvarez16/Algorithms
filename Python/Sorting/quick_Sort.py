# QUICK SORT -> Divide and Conquer Algorithm

# Best: O(nlog(n)) Time Complexity | O(nlog(n)) Space Complexity
# Average: O(nlog(n)) Time Complexity | O(nlog(n)) Space Complexity
# Worst: O(n^2) Time Complexity | O(nlog(n)) Space Complexity

def quick_sort(array):
    """Function to hold the main implementation of quick sort algorithm"""
    quick_sort_aux(array, 0, len(array) - 1)
    return array

def quick_sort_aux(array, start_idx, end_idx):
    """Function to sort array"""
    if start_idx >= end_idx:
        # Array sorted
        return
    pivot_idx = start_idx
    left_idx = start_idx + 1
    right_idx = end_idx
    while right_idx >= left_idx:
        # Main loop to sort array
        if array[left_idx] > array[pivot_idx] and array[right_idx] < array[pivot_idx]:
            swap(left_idx, right_idx, array)
        if array[left_idx] <= array[pivot_idx]:
            left_idx += 1
        if array[right_idx] >= array[pivot_idx]:
            right_idx -= 1
    swap(pivot_idx, right_idx, array)
    left_sub_array_smaller = right_idx - 1 - start_idx < end_idx - (right_idx - 1) # If left sub array is smaller than right sub array
    if left_sub_array_smaller:
        # Start sorting the smaller sub array first -> Best approach regarding space complexity (so log of n is not exceede)
        quick_sort_aux(array, start_idx, right_idx - 1)
        quick_sort_aux(array, right_idx + 1, end_idx)
    else:
        quick_sort_aux(array, right_idx + 1, end_idx)
        quick_sort_aux(array, start_idx, right_idx - 1)

def swap(i, j, array):
    """Function to swap two elements in the same array"""
    array[i], array[j] = array[j], array[i]

# Main program
print(quick_sort([1, -12, 9, 54, -11, 75, 8, 14]))
    