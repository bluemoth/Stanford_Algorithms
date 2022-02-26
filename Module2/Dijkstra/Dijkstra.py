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

Feb 25 2022 - Implementation below works for assignment (undirected adjacency list). The test cases from github (below) may have issues.
During test of t1-t3, outputs at times are correct for vertex's of interest. Other times they are way off. 
For simple test cases (t4), implementation works fine. Running time of this vertex_queue setup is O(V^2)

For another challenge, may look to implement algorithm using a priority queue or heap

https://github.com/bluemoth/stanford-algs/tree/master/testCases/course2/assignment2Dijkstra

'''

from cmath import inf
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


def Dijkstra(graph, vertex=1):
    dist = dict()
    vertex_queue = [vertex]

    for v in graph:
        dist[v] = inf
        vertex_queue.append(v)
    
    dist[vertex] = 0

    while vertex_queue:
        vertex_queue.pop(0)
        for u in vertex_queue:
            for edge in graph[u]:
                alt = dist[u] + graph[u][edge]
                if alt < dist[edge]:
                    dist[edge] = alt
    return dist

def main():

    # Test / home work data files
    t1 = "Module2/Dijkstra/input_random_1_4.txt" # expected output 253,172,197,242,331,402,143,272,249,265
    t2 = "Module2/Dijkstra/input_random_10_16.txt" # expected output 588,405,675,521,909,328,418,957,830,839
    t3 = "Module2/Dijkstra/input_random_20_64.txt" # expected output 699513,452243,60365,166860,289662,820910,593399,836776,621238,439299
    t4 = "Module2/Dijkstra/TR_input_1.txt" # 0,1,2,3,4,4,3,2
    t5 = ""
    homeworkData = "Module2/Dijkstra/Dijkstra.txt" 
    
    # test graph for formatting/initial usage
    g = { 1 : {2:1, 3:4},
          2 : {4:6, 3:2},
          3 : {4:3},
          4 : {}
    }
    start = time.time()
    # for homework, interested in distances from source vertex 1 to following vertexs 7,37,59,82,99,115,133,165,188,197
    vertex_of_interest = [7,37,59,82,99,115,133,165,188,197]

    # assignments
    graph = dict()
    graph = build_graph(filename=homeworkData)

    distances = Dijkstra(graph)
    print(distances)
    # for v in vertex_of_interest:
    #     print(distances[v])
    print(time.time()-start)

main()