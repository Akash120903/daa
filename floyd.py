def floyd_marshall(N, connections):
    INF = float('inf')
    distances = [[INF] * N for _ in range(N)]

    # Initialize distances with direct connections
    for D1, D2, L in connections:
        distances[D1][D2] = L
        distances[D2][D1] = L

    # Update distances using the Floyd-Warshall algorithm
    for k in range(N):
        for i in range(N):
            for j in range(N):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances


def minimum_wire_length(N, connections):
    distances = floyd_marshall(N, connections)
    min_distances = [sum(distances[i]) for i in range(N)]
    minimum_length = min(min_distances)

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

