import math

def dijkstra_mat(G, src, ln):
    dist = [math.inf] * ln
    dist[src] = 0
    found = [0] * ln
    u = src
    for _ in range(ln):
        minm = math.inf
        for u1 in range(ln):
            if dist[u1] < minm and not found[u1]:
                minm = dist[u1]
                u = u1
        found[u] += 1
        for v in range(ln):
            if (not found[v] and G[u][v] != 0) and (dist[v] > dist[u] + G[u][v]):
                dist[v] = dist[u] + G[u][v]
    return dist

def driver(G, s):
    ln = len(G)
    out = dijkstra_mat(G, s, ln)
    print("Using adjacency matrix")
    for i, j in enumerate(out):
        print(f"\t\t {i} : {j}")
    print()

if __name__ == "__main__":
    # Modify the adjacency matrix for a directed graph
    G = [[0, 4, 0, 5, 0, 7],  [0, 0, 1, 0, 8, 2], [0, 0, 0, 6, 0, 9], [0, 0, 0, 0, 7, 0]]
    s = 2
    driver(G, s)
