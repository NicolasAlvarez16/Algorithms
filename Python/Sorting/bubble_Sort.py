# Best Case: O(n) Time complexity | O(1) Space complexity
# Average Case: O(n^2) Time complexity | O(1) Space complexity 
# Worst Case: O(n^2) Time complexity | O(1) Space complexity 

def bubble_sort(array):
    """Function to implment bubble sort algorithm to sort an array"""
    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True # Assume is sorted
        for i in range(len(array) - 1 - counter):
            # Check if actual element is greater than following element
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                is_sorted = False
        counter += 1
    return array

def swap(i, j, array):
    """Function to swap two elements"""
    array[i], array[j] = array[j], array[i]

# Main Program
print(bubble_sort([1, -12, 9, 54, -11, 75, 8, 14]))
