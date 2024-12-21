def max_heapify(arr, i, n):
    """Ensures the max-heap property for the subtree rooted at index i."""
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        max_heapify(arr, largest, n)  # Recursively heapify the affected subtree


def build_max_heap(arr):
    """Builds a max-heap from an unsorted array."""
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, i, n)


def heap_sort(arr):
    """Sorts an array using the Heap-Sort algorithm."""
    build_max_heap(arr)
    n = len(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap the root (largest element) with the last element
        max_heapify(arr, 0, i)  # Restore the heap property for the reduced heap


# Example Usage:
if __name__ == "__main__":
    numbers = [4, 10, 3, 5, 1]
    print("Original array:", numbers)
    heap_sort(numbers)
    print("Sorted array:", numbers)
