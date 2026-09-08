# Cole Nola
# 3196815
# 9/8/2026
# Tuesdays 4:00pm
# Task 1.a Insertion sort algorithm using a new array

def insertion_sort_method1(arr):
    """Return a NEW sorted list using insertion into a separate array."""
    sorted_arr = []
    # TODO:
    # Define outer loop and/or inner loop based on the algorithm where a new array is used to
    # insert the sorted elements.
    for i in range(len(arr)):
        # Insert the current element into the sorted array
        current_value = arr[i]
        inserted = False
        for j in range(len(sorted_arr)):
            if current_value < sorted_arr[j]:
                sorted_arr.insert(j, current_value)
                inserted = True
                break
        if not inserted:
            sorted_arr.append(current_value)
        print(f"After iteration {i + 1}: {sorted_arr}")

    return sorted_arr


# Quick test
print(insertion_sort_method1([1, 5, 4, 2, 8]))