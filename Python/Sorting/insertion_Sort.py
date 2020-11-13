# Best Case: O(n) Time Complexity | O(1) Space Complexity
# Average Case: O(n^2) Time Complexity | O(1) Space Complexity
# Worst Case: O(n^2) Time Complexity | O(1) Space Complexity

def insertion_sort(array):
    """Function to implement insertion sort algorithm"""
    for i in range(1, len(array)):
        # Looping through array once
        value_sort = array[i] # Current number
        while array[i - 1] > value_sort and i > 0:
            swap(i, i - 1, array) # Swaping to insert current number in sorted sublist
            i = i - 1
    return array

def swap(i, j, array):
    """Function to swap two elements in the same array"""
    array[i], array[j] = array[j], array[i]

# Main Program
print(insertion_sort([1, -12, 9, 54, -11, 75, 8, 14]))