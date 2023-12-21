# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 11:45:51 2023

@author: Riya
"""
graph = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}
def breadth_first_search(graph, start_node):
    queue = [start_node]
    visited = [start_node]
    print("\nOrder of visited nodes by BFS: ", end=" ")
    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
breadth_first_search(graph, "5")
