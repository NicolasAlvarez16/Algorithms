# MERGER SORT -> DIVIDED AND CONQUER ALGORITHM
# O(nlog(n)) Time Complexity | O(n) Space Complexity

def merge_sort(array):
    """Function to hold the main implementation of merge sort algorithm"""
    if len(array) <= 1:
        # If array given is 1 or less 
        return array
    aux_array = array[:] # Copy of array
    merge_sort_aux(array, 0, len(array) - 1, aux_array)
    return array

def merge_sort_aux(main_array, start_idx, end_idx, aux_array):
    """Function to divide the arrays recursively"""
    if start_idx == end_idx:
        return
    mid_idx = (start_idx + end_idx) // 2 # Middle of array
    merge_sort_aux(aux_array, start_idx, mid_idx, main_array) # Dividing Array
    merge_sort_aux(aux_array, mid_idx + 1, end_idx, main_array) # Dividing Array
    final_merge(main_array, start_idx, mid_idx, end_idx, aux_array)

def final_merge(main_array, start_idx, mid_idx, end_idx, aux_array):
    """Function to merge subarrays"""
    k = start_idx
    i = start_idx
    j = mid_idx + 1
    while i <= mid_idx and j <= end_idx:
        if aux_array[i] <= aux_array[j]:
            main_array[k] = aux_array[i]
            i += 1
        else: 
            main_array[k] = aux_array[j]
            j += 1
        k += 1
    while i <= mid_idx:
        main_array[k] = aux_array[i] 
        i += 1
        k += 1
    while j <= end_idx:
        main_array[k] = aux_array[j]
        j += 1
        k += 1

# Main Program
print(merge_sort([1, -12, 9, 54, -11, 75, 8, 14]))