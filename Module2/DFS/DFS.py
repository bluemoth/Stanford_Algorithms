'''
Depth first search algorithm, coded based on Stanford Algo's lecture material.
DFS to use a stack rather than a queue (BFS). 

Recursive approach found in slides.
'''

def DFS(G, vertex, visited, s):
    if vertex not in visited:
        # mark vertex as explored
        visited.append(vertex)
        print(vertex)
    # for every edge (s, v)
        for edge in G[vertex]:
            DFS(G, edge, visited, s)

def main():
    
    visitedNodes = []
    stack = []

    graph = {
        5 : [3, 7],
        3 : [2, 4],
        7 : [8],
        2 : [],
        4 : [8],
        8 : []
    }

    DFS(graph, 5, visitedNodes, stack)
    print(visitedNodes)


main()