import heapq

graph = {
    "A" : {"B" : 3, "C" : 3},
    "B" : {"A" : 3, "D" : 4, "E" : 4 },
    "C" : {"A" : 3, "F" : 4, "E" : 3},
    "D" : {"B" : 4, "E" : 3, "G" : 10},
    "E" : {"B" : 4, "C" : 3, "D" : 3, "G" : 7},
    "F" : {"C" : 4, "G" : 3 },
    "G" : {"D" : 10, "E" : 7, "F" : 3},
}


def dijkstra(graph, start):
    # Inicjalizacja odległości do wierzchołków (nieskończoność)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Odległość do wierzchołka startowego = 0
    
    # Kolejka priorytetowa do przechowywania wierzchołków do odwiedzenia
    priority_queue = [(0, start)]  # (koszt, wierzchołek)

    # Śledzenie odwiedzonych wierzchołków
    visited = set()

    while priority_queue:
        # Pobranie wierzchołka o najmniejszym koszcie
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jeżeli wierzchołek został już odwiedzony, pomijamy
        if current_node in visited:
            continue

        visited.add(current_node)

        # Przeglądanie sąsiadów
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Aktualizacja odległości, jeśli znaleziono krótszą ścieżkę
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
count = 0
for node in nodes:
    start_node = node
    result = dijkstra(graph, start_node)
    print(f"{count}. Najkrótsze odległości od wierzchołka {start_node}: {result} \n")

    count = count + 1
