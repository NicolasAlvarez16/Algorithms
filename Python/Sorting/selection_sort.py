# O(n^2) Time Complexity | O(1) Space Complexity

def selection_sort(array):
    """Function to implement selection sort algorithm"""
    current_idx = 0 # Starting index
    while current_idx < len(array) - 1:
        smallest_idx = current_idx
        for i in range(current_idx + 1, len(array)):
            if array[smallest_idx] > array[i]:
                smallest_idx = i # Updating smallest number
        swap(current_idx, smallest_idx, array)
        current_idx += 1 # New current index
    return array

def swap(i, j, array):
    """Function to swap two elements in the same array"""
    array[i], array[j] = array[j], array[i]

# Main Program
print(selection_sort([2, 3, 5, 5, 6, 8, 9]))