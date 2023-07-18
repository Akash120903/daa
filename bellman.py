def bellman_ford(N, connections, source):
    distances = [float('inf')] * N
    distances[source] = 0

    for _ in range(N - 1):
        for D1, D2, L in connections:
            if distances[D1] != float('inf') and distances[D1] + L < distances[D2]:
                distances[D2] = distances[D1] + L

    return distances


def minimum_wire_length(N, connections, Di):
    distances = bellman_ford(N, connections, Di)
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
Di = 0  # Device to connect to all others

minimum_length = minimum_wire_length(N, connections, Di)
print("Minimum length of wire required:", minimum_length)
