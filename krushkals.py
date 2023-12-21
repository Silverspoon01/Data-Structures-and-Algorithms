# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 11:48:11 2023

@author: Riya
"""

import numpy as np
n = 6
input_data = [
    [0, 3, 0, 2, 0, 0],
    [3, 0, 1, 0, 0, 4],
    [0, 1, 0, 0, 5, 0],
    [2, 0, 0, 0, 6, 0],
    [0, 0, 5, 6, 0, 1],
    [0, 4, 0, 0, 1, 0]
]

G = np.array(input_data)
def kruskal(G):
    n = G.shape[0]
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if G[i, j] > 0:
                edges.append((i, j, G[i, j]))
    edges.sort(key=lambda x: x[2])
    MST = []
    parent = list(range(n))
    rank = [0] * n
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        px, py = find(x), find(y)
        if rank[px] > rank[py]:
            parent[py] = px
        else:
            parent[px] = py
            if rank[px] == rank[py]:
                rank[py] += 1
    for edge in edges:
        if len(MST) == n - 1:
            break
        u, v, w = edge
        if find(u) != find(v):
            MST.append(edge)
            union(u, v)
    return MST
MST = kruskal(G)
print("Minimum Spanning Tree:")
for edge in MST:
    print(f"{edge[0]} - {edge[1]} : {edge[2]}")
