import heapq
import time

def greedy(graph, start):
    vertices = len(graph)
    distance = [float('inf')] * vertices
    distance[start] = 0
    visited = [False] * vertices
    priority_queue = [(0, start)]
    path = [-1] * vertices

    while priority_queue:
        dist_u, u = heapq.heappop(priority_queue)

        if visited[u]:
            continue

        visited[u] = True

        for v, weight in enumerate(graph[u]):
            if not visited[v] and weight != 0 and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                path[v] = u  # Update the parent vertex for reconstructing the path
                heapq.heappush(priority_queue, (distance[v], v))

    return distance, path

def print_path(source, target, path):
    if source == target:
        print(f"{target}", end="")
    elif path[target] == -1:
        print("No path exists")
    else:
        print_path(source, path[target], path)
        print(f" -> {target}", end="")

if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices: "))

    print("Enter the weighted adjacency matrix (row-wise, separate values with spaces):")
    graph = [list(map(int, input().split())) for _ in range(vertices)]

    start_vertex = int(input("Enter the starting vertex: "))

    start_time = time.time()
    time.sleep(1)  # Introduce a delay using time.sleep(1) for demonstration purposes

    for target_vertex in range(vertices):
        result, path = greedy(graph, start_vertex)

        print(f"\nShortest distances from source {start_vertex} to target {target_vertex}:")
        print(f"Shortest distance: {result[target_vertex]}")

        print("Shortest path:")
        print_path(start_vertex, target_vertex, path)

    end_time = time.time()

    print(f"\nTotal execution time: {end_time - start_time:.6f} seconds")
