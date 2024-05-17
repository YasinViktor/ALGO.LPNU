import unittest
from find_optimal_server import Graph, Vertex, Edge, read_graph_from_file, find_optimal_server_location

class TestGraphMethods(unittest.TestCase):

    def test_dijkstra(self):
        vertices = {1: Vertex(1), 2: Vertex(2), 3: Vertex(3)}
        edges = {1: [(2, 1)], 2: [(3, 2)]}
        graph = Graph(vertices, edges)
        distances = graph.dijkstra(vertices[1])
        self.assertEqual(distances, {vertices[1]: 0, vertices[2]: 1, vertices[3]: 3})

    def test_find_optimal_server_location(self):
        vertices = {1: Vertex(1), 2: Vertex(2), 3: Vertex(3)}
        edges = {1: [(2, 1)], 2: [(3, 2)]}
        graph = Graph(vertices, edges)
        clients = [vertices[1], vertices[3]]
        min_max_latency = find_optimal_server_location(graph, clients)
        self.assertEqual(min_max_latency, 2)

if __name__ == '__main__':
    unittest.main()
