# Cole Nola
# 3196815
# 9/8/2026
# Tuesdays 4:00pm
# Task 1.B Insertion sort algorithm using in place array method

# This function sorts the list in ascending order using the in-place insertion sort method.
# It does not create a new array; instead, it rearranges the elements inside the original list.
# The idea is to take each element one at a time and place it into the correct position
# among the earlier elements that are already sorted.

def insertion_sort_methodB(arr):
    """Return a sorted list using insertion into the same array."""

    # Start from the second element because the first element is already considered sorted.
    for i in range(1, len(arr)):
        # Save the current value so it can be inserted into the correct position.
        current_value = arr[i]

        # Move backward through the sorted portion of the list.
        j = i - 1

        # Shift larger values to the right to make room for the current value.
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the current value into its proper sorted location.
        arr[j + 1] = current_value

        # Print the array state after each pass to show the sorting progress.
        print(f"After iteration {i}: {arr}")

    return arr


# Example test cases demonstrating the algorithm's behavior.
print(insertion_sort_methodB([]))
print(insertion_sort_methodB([7, 7, 7, 7]))
print(insertion_sort_methodB([5, 4, 3, 2, 1]))
