from heapq import heappop, heappush
def prim(graph,start_vertex):
    mst_edges=[]
    visited=set()
    heap=[(0, start_vertex, None)]

    while heap:
        cost, current_vertex, prev_vertex=heappop(heap)
        if current_vertex not in visited:
            visited.add(current_vertex)
            if prev_vertex is not None:
                mst_edges.append((prev_vertex, current_vertex, cost))

            for neighbour,weight in graph[current_vertex].items():
                heappush(heap,(weight,neighbour,current_vertex))
    return mst_edges
def printtable(headers,data):
    head_str=" | ".join(headers)
    print(head_str)
    print("-"*len(head_str))
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

    start_vertex = input("Enter the starting vertex for Prim's algorithm: ")

    mst_prim = prim(graph, start_vertex)
    total_weight_prim = sum(weight for _, _, weight in mst_prim)
    print("\nMinimum Spanning Tree (Prim's Algorithm):")
    printtable(["V1", "V2", "Weight"], mst_prim)
    print("Total Weight:", total_weight_prim)

if __name__ == "__main__":
    main()        
