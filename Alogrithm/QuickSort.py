def partition(arr, low, high):
    pivot = arr[high]  # Choose the pivot element (last element in this case)
    i = low - 1  # Index of smaller element

    p_ass=1

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
       
        if arr[j] <= pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

        p_ass= j

    # Swap arr[i+1] and arr[high] (pivot)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and obtain the partitioning index
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Example usage:
arr = [12, 7, 3, 9, 2, 5]
print("Original array:", arr)

quick_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)
