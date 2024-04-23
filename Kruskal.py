# Helper functions for Kruskal's Algorithm
def make_set(vertices):
    parent = {vertex: vertex for vertex in vertices}
    rank = {vertex: 0 for vertex in vertices}
    return parent, rank

def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]

def union(parent, rank, vertex1, vertex2):
    root1 = find(parent, vertex1)
    root2 = find(parent, vertex2)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal(graph):
    edges = [(weight, vertex1, vertex2) for vertex1, neighbors in graph.items() for vertex2, weight in neighbors.items()]
    edges.sort()

    minimum_spanning_tree = []
    parent, rank = make_set(graph.keys())

    for edge in edges:
        weight, vertex1, vertex2 = edge
        if find(parent, vertex1) != find(parent, vertex2):
            union(parent, rank, vertex1, vertex2)
            minimum_spanning_tree.append((vertex1, vertex2, weight))

    return minimum_spanning_tree

def print_table(headers, data):
    header_str = " | ".join(headers)
    print(header_str)
    print("-" * len(header_str))

    for row in data:
        print(" | ".join(map(str, row)))

def main():
    vertices = input("Enter vertices separated by spaces: ").split()
    graph = {vertex: {} for vertex in vertices}

    while True:
        try:
            edge_input = input("Enter edge (vertex1 vertex2 weight) or 'done' to finish: ")
            if edge_input.lower() == 'done':
                break
            vertex1, vertex2, weight = edge_input.split()
            graph[vertex1][vertex2] = int(weight)
            graph[vertex2][vertex1] = int(weight)
        except ValueError:
            print("Invalid input. Please enter a valid edge.")

    print("\nVertices:", vertices)

    minimum_spanning_tree_kruskal = kruskal(graph)
    total_weight_kruskal = sum(weight for _, _, weight in minimum_spanning_tree_kruskal)
    print("\nMinimum Spanning Tree (Kruskal's Algorithm):")
    print_table(["V1", "V2", "Weight"], minimum_spanning_tree_kruskal)
    print("Total Weight (Kruskal's Algorithm):", total_weight_kruskal)

if __name__ == "__main__":
    main()
