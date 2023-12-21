# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 11:47:15 2023

@author: Riya
"""
class PrimsAlgo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph_matrix = [[0 for _ in range(self.num_vertices)] for _ in range(self.num_vertices)]
    def add_edge(self, src, dest, cost):
        if src == dest:
            print('Same vertices')
        else:
            self.graph_matrix[src][dest] = cost
            self.graph_matrix[dest][src] = cost
    def print_graph(self):
        for row in self.graph_matrix:
            for val in row:
                print(val, end=' ')
            print()
    def get_neighbors(self, vertex):
        neighbors = []
        for i in range(len(self.graph_matrix[vertex])):
            if self.graph_matrix[vertex][i] > 0:
                neighbors.append(i)
        return neighbors
    def edge_weight(self, src, dest):
        return self.graph_matrix[src][dest]
    def minimum_spanning_tree(self, source):
        visited = []
        distances = {i: float('inf') for i in range(len(self.graph_matrix))}
        distances[source] = 0
        temp = {i: distances[i] for i in distances}
        while temp:
            min_node = float('inf')
            key = None
            for i in temp:
                if temp[i] < min_node:
                    min_node = temp[i]
                    key = i
            temp.pop(key)
            if key not in visited:
                visited.append(key)
                neighbors = self.get_neighbors(key)
                for neighbor in neighbors:
                    if (self.edge_weight(key, neighbor) < distances[neighbor]) and (neighbor not in visited):
                        distances[neighbor] = self.edge_weight(key, neighbor)
                        temp[neighbor] = self.edge_weight(key, neighbor)
        print('Total weight is', sum(distances.values()))
        print('Path is', visited)
g = PrimsAlgo(6)
g.add_edge(0, 3, 15)
g.add_edge(0, 1, 21)
g.add_edge(1, 2, 37)
g.add_edge(1, 4, 78)
g.add_edge(2, 3, 50)
g.add_edge(2, 4, 24)
g.add_edge(3, 4, 43)
g.add_edge(3, 5, 62)
g.add_edge(4, 5, 19)
g.print_graph()
g.minimum_spanning_tree(3)
