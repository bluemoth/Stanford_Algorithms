'''
Dijkstra Algorithm Homework:
The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200.  
Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. 
For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. 
The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200.  
The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, 
and to compute the shortest-path distances between 1 and every other vertex of the graph. 
If there is no path between a vertex vv and vertex 1, we'll define the shortest-path distance between 1 and vv to be 1000000. 
'''


import time

def build_graph(filename):
    with open(filename, 'r') as file:
        graph = dict()
        for line in file:
            # vel -> vertex, edge, list variable
            vel = line.strip().strip('\n').split()
            vertex = int(vel[0])
            graph[vertex] = dict()
            for item in range(1, len(vel)):
                # filter out edge,weights from vel
                edge, weight = vel[item].split(',')
                graph[vertex][int(edge)] = int(weight)
    return graph

def Dijkstra(graph):
    None




def main():

    # Test / home work data files
    t1 = ""
    t2 = ""
    t3 = ""
    t4 = ""
    t5 = ""
    homeworkData = "Module2/Dijkstra/Dijkstra.txt"
    
    # assignments
    graph = dict()
    graph = build_graph(filename=homeworkData)
    print(graph)

main()