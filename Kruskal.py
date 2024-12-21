class DisjointSet:
    """A class to represent the disjoint-set data structure."""
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        """Find the representative of the set containing v (with path compression)."""
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        """Union the sets containing u and v."""
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1


def kruskal(vertices, edges):
    """Kruskal's algorithm to find the MST of a graph."""
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])  # Each edge is (u, v, weight)

    # Initialize disjoint sets for all vertices
    ds = DisjointSet(vertices)

    mst = []  # List to store edges of the MST
    for u, v, weight in edges:
        # Check if including this edge forms a cycle
        if ds.find(u) != ds.find(v):
            mst.append((u, v, weight))  # Add edge to MST
            ds.union(u, v)  # Union the sets of u and v

    return mst


# Example Usage
if __name__ == "__main__":
    # Define graph as a list of edges (u, v, weight)
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        ('A', 'B', 1),
        ('A', 'C', 5),
        ('B', 'C', 4),
        ('B', 'D', 2),
        ('C', 'D', 3),
        ('C', 'E', 6),
        ('D', 'E', 7),
    ]

    # Find the MST
    mst = kruskal(vertices, edges)
    print("Edges in the MST:")
    for edge in mst:
        print(edge)
