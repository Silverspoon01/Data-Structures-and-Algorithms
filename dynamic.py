# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 11:41:50 2023

@author: Riya
"""
class Graph:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.graph = []
        self.nodes = []
    def add_edge(self, start, destination, weight):
        self.graph.append([start, destination, weight])
    def add_node(self, value):
        self.nodes.append(value)
    def print_solution(self, distance):
        print('Vertex distance from source')
        for key, value in distance.items():
            print('  ' + str(key), ' :    ', value)
    def BellmanFord(self, src):
        distance = {i: float('Inf') for i in self.nodes}
        distance[src] = 0
        for _ in range(self.V - 1):
            for start, destination, weight in self.graph:
                if distance[start] != float('Inf') and distance[start] + weight < distance[destination]:
                    distance[destination] = distance[start] + weight
        for start, destination, weight in self.graph:
            if distance[start] != float('Inf') and distance[start] + weight < distance[destination]:
                print('Graph contains negative cycle')
                return
        self.print_solution(distance)
g = Graph(5)
g.add_node(0)
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 6)
g.add_edge(1, 0, 3)
g.add_edge(2, 3, 1)
g.add_edge(3, 2, 2)
g.add_edge(3, 1, 1)
g.add_edge(4, 1, 4)
g.add_edge(4, 3, 2)
g.BellmanFord(4)
