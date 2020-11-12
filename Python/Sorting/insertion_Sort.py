# Best Case: O(n) Time Complexity | O(1) Space Complexity
# Average Case: O(n^2) Time Complexity | O(1) Space Complexity
# Worst Case: O(n^2) Time Complexity | O(1) Space Complexity

def insertion_sort(array):
    """Function to implement insertion sort algorithm"""
    for i in range(1, len(array)):
        # Looping through array once
        j = i # Current number
        while j > 0 and array[j] < array[j - 1]:
            # Looping array backwards
            swap(j, j - 1, array) # Swaping to insert current number in sorted sublist
    return array

def swap(i, j, array):
    """Function to swap two elements in the same array"""
    array[i], array[j] = array[j], array[i]

# Main Program
array = [8, 5, 2, 9, 5, 6, 3]
print(insertion_sort(array))