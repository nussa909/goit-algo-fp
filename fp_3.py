"""
Завдання 3. Дерева, алгоритм Дейкстри
Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. 
Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.
"""

import networkx as nx
import matplotlib.pyplot as plt
import heapq


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    heap = [(0, start)]
    heapq.heapify(heap)

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance == float('infinity'):
            break

        for neighbor, data in graph[current_vertex].items():
            distance = current_distance + data['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


graph = nx.Graph()

graph.add_edge('A', 'B', weight=5)
graph.add_edge('A', 'C', weight=5)
graph.add_edge('B', 'D', weight=3)
graph.add_edge('C', 'D', weight=2)
graph.add_edge('D', 'E', weight=4)
graph.add_edge('F', 'A', weight=10)
graph.add_edge('D', 'F', weight=1)

print(dijkstra(graph.adj, 'A'))

pos = nx.spring_layout(graph, seed=42)
nx.draw(graph, pos, with_labels=True, node_size=700,
        node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
plt.show()
