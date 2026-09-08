# Cole Nola
# 3196815
# 9/8/2026
# Tuesdays 4:00pm
# Task 1.a Insertion sort algorithm using a new array

# This function sorts the list by creating a new array instead of modifying the original one.
# The idea is to take each value from the input list and insert it into the correct spot
# within the already-sorted portion of the new list.

def insertion_sort_methodA(arr):
    """Return a NEW sorted list using insertion into a separate array."""

    # Initialize an empty list that will hold the sorted values.
    sorted_arr = []

    # Loop through every value in the original list.
    for i in range(len(arr)):
        # Save the current value to compare against the sorted values.
        current_value = arr[i]

        # Track whether the value has already been placed in the correct location.
        inserted = False

        # Check the sorted list from left to right and find the correct insertion point.
        for j in range(len(sorted_arr)):
            if current_value < sorted_arr[j]:
                # Insert the current value before the first larger value.
                sorted_arr.insert(j, current_value)
                inserted = True
                break

        # If no smaller value was found, place the value at the end of the sorted list.
        if not inserted:
            sorted_arr.append(current_value)

        # Print the list after each pass so the sorting process can be observed.
        print(f"After iteration {i + 1}: {sorted_arr}")

    return sorted_arr


# Quick test to demonstrate the sorting behavior on a sample input.
print(insertion_sort_methodA([1, 5, 4, 2, 8]))