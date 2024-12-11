graph = {
    "A" : {"B" : 3, "C" : 3},
    "B" : {"A" : 3, "D" : 4, "E" : 3 },
    "C" : {"A" : 3, "F" : 4, "E" : 3},
    "D" : {"B" : 4, "E" : 3, "G" : 10},
    "E" : {"B" : 3, "C" : 3, "D" : 3, "G" : 7},
    "F" : {"C" : 4, "G" : 3 },
    "G" : {"D" : 10, "E" : 7, "F" : 3},
}

class Graph :
    def __init__(self, graph: dict = {}):
       self.graph = graph

    def Dijkstra(self, source: str):
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0


first = Graph(graph=graph) 

print(first)