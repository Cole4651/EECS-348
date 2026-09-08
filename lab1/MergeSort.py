# Cole Nola
# 3196815
# 9/8/2026
# Tuesdays 4:00pm
# Task 2 Merge sort algorithm

# Recursive merge sort uses divide-and-conquer:
# 1) Split the list into two halves
# 2) Recursively sort each half
# 3) Merge the two sorted halves back together


def merge(left, right):
    """Merge two sorted lists into one sorted list."""
    merged = []
    left_index = 0
    right_index = 0

    # Compare the front of each list and add the smaller value first.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add any remaining values from the left list.
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Add any remaining values from the right list.
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def merge_sort(arr):
    """Return a new list sorted in ascending order using recursion."""
    # Base case: a list with 0 or 1 item is already sorted.
    if len(arr) <= 1:
        return arr[:]

    # Split the list into two halves.
    middle = len(arr) // 2
    left_half = merge_sort(arr[:middle])
    right_half = merge_sort(arr[middle:])

    # Merge the two sorted halves.
    return merge(left_half, right_half)


# Example test cases
print(merge_sort([]))
print(merge_sort([7, 7, 7, 7]))
print(merge_sort([5, 4, 3, 2, 1]))
print(merge_sort([3, 1, 2, 5, 4]))