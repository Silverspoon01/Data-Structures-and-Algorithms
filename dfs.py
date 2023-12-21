# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 11:45:31 2023

@author: Riya
"""

new_graph = { "A": ["B", "C"],"B": ["D", "E"],   "C": ["F"],   "D": [],  "E": ["F"],"F": []}
def depth_first_search(graph, start_node):
    stack = [start_node]
    visited_nodes = []
    print("\nOrder of visited nodes by DFS: ", end=" ")
    while stack:
        current_node = stack.pop()
        if current_node not in visited_nodes:
            visited_nodes.append(current_node)
            print(current_node, end=" ")
        for neighbor in graph[current_node]:
            if neighbor not in visited_nodes:
                stack.append(neighbor)
depth_first_search(new_graph, "A")
