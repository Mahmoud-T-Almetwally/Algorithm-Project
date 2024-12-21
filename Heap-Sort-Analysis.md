### Part (a): Algorithms for Heap-Sort

Heap-Sort consists of the following steps:

1. **Build a Max-Heap**: Convert the input array into a max-heap.
2. **Heapify**: Maintain the max-heap property during the sorting process.
3. **Heap-Sort**: Sort the array by repeatedly extracting the largest element (root of the heap).

#### **Algorithms in Pseudo Code**

1. **Max-Heapify**  
   Ensures the max-heap property for a given node.

   ```plaintext
   MAX-HEAPIFY(A, i, n):
       left = 2 * i + 1
       right = 2 * i + 2
       largest = i

       if left < n and A[left] > A[largest]:
           largest = left

       if right < n and A[right] > A[largest]:
           largest = right

       if largest != i:
           swap A[i] with A[largest]
           MAX-HEAPIFY(A, largest, n)
   ```

2. **Build Max-Heap**  
   Converts the input array into a max-heap.

   ```plaintext
   BUILD-MAX-HEAP(A):
       n = length(A)
       for i = floor(n/2) - 1 down to 0:
           MAX-HEAPIFY(A, i, n)
   ```

3. **Heap-Sort**  
   Sorts the array using the max-heap.

   ```plaintext
   HEAPSORT(A):
       BUILD-MAX-HEAP(A)
       n = length(A)
       for i = n - 1 down to 1:
           swap A[0] with A[i]
           n = n - 1
           MAX-HEAPIFY(A, 0, n)
   ```

---

### Part (b): Analysis of Algorithms

1. **Max-Heapify**
   - Time Complexity: \( O(\log n) \), as it works recursively down the height of the heap.
   - Space Complexity: \( O(1) \), since it operates in-place.

2. **Build Max-Heap**
   - Time Complexity: \( O(n) \), as it calls `MAX-HEAPIFY` on \( n/2 \) nodes.
   - Space Complexity: \( O(1) \), since it operates in-place.

3. **Heap-Sort**
   - Time Complexity: \( O(n \log n) \), as it extracts \( n \) elements and calls `MAX-HEAPIFY` for each.
   - Space Complexity: \( O(1) \), since it uses no additional memory.

Overall, Heap-Sort is efficient for sorting and works well with limited memory resources.

---

### Summary of Python Implementation:
1. **`max_heapify`** ensures the heap property for a subtree.
2. **`build_max_heap`** constructs the heap structure.
3. **`heap_sort`** sorts the array in ascending order by leveraging the heap property.

The implementation is efficient with a worst-case time complexity of \( O(n \log n) \).
