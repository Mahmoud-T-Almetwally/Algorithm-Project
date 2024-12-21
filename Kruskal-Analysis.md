### Part (a): Algorithms for Kruskal’s Algorithm

---

#### **Pseudo Code for Kruskal's Algorithm**

1. **Kruskal’s Algorithm**

```plaintext
KRUSKAL(graph):
    MST = []  # List to store edges in the MST
    SORT edges in graph by weight
    MAKE-SET(vertices)  # Initialize disjoint sets for each vertex
    
    for each edge (u, v) in sorted edges:
        if FIND-SET(u) != FIND-SET(v):  # Check if u and v belong to different sets
            MST.append((u, v))  # Add edge to MST
            UNION(u, v)  # Merge the sets of u and v
    
    return MST
```

2. **Disjoint-Set Operations**

```plaintext
MAKE-SET(x):
    parent[x] = x  # Each vertex is its own parent
    rank[x] = 0    # Rank is initially 0

FIND-SET(x):
    if parent[x] != x:
        parent[x] = FIND-SET(parent[x])  # Path compression
    return parent[x]

UNION(x, y):
    rootX = FIND-SET(x)
    rootY = FIND-SET(y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1
```

---

### Part (b): Analysis of Algorithms

1. **Sorting Edges**:
   - Time Complexity: \( $O(E \log E)$ \), where \( E \) is the number of edges.
   - Sorting is required to process edges in ascending order of weight.

2. **Disjoint-Set Operations**:
   - **MAKE-SET**: \( O(V) \), where \( V \) is the number of vertices.
   - **FIND-SET** and **UNION**: Each operation runs in \( $O(\alpha(V))$ \), where \( $\alpha(V)$ \) is the **inverse Ackermann function**, which is practically constant.

3. **Overall Complexity**:
   - The dominant term is \( $O(E \log E)$ \) due to sorting the edges. Disjoint-set operations are nearly constant.
   - Total Complexity: \( $O(E \log E + V \cdot \alpha(V))$ \), which simplifies to \( $O(E \log E)$ \).
