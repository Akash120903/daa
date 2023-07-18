import heapq


def dijkstra(N, graph):
    distances = [float('inf')] * N  # Initialize distances with infinity
    distances[0] = 0  # Start from device 0
    min_heap = [(0, 0)]  # (distance, device)

    while min_heap:
        distance, device = heapq.heappop(min_heap)

        if distance > distances[device]:
            continue

        for neighbor, neighbor_length in graph[device]:
            new_distance = distance + neighbor_length
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(min_heap, (new_distance, neighbor))

    return distances


def minimum_wire_length(N, connections):
    graph = [[] for _ in range(N)]

    for D1, D2, L in connections:
        graph[D1].append((D2, L))
        graph[D2].append((D1, L))

    distances = dijkstra(N, graph)
    minimum_length = sum(distances)

    return minimum_length


# Example usage
N = 5  # Number of devices
connections = [
        (0, 1, 2),  # D0 connected to D1 with wire length 2
        (0, 2, 3),  # D0 connected to D2 with wire length 3
        (1, 3, 1),  # D1 connected to D3 with wire length 1
        (2, 3, 4),  # D2 connected to D3 with wire length 4
        (2, 4, 5),  # D2 connected to D4 with wire length 5
]

minimum_length = minimum_wire_length(N, connections)
print("Minimum length of wire required:", minimum_length)
