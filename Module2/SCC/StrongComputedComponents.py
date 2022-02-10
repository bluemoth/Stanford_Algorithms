'''
Algorithm for computing strongly connected components. 
File format (directed graph):
-Vertices labeled 1-875714
-Edges are indicated by rows
-vertex lebel in first column i sthe tail, and the vertex in second column is the head
Example:
11th row => "2 47646", meaning vertex with label 2 has an outgoing edge to vertex label 47646

Instructions: Use SCC algorithm from lecture (will choose DFS slick method)

Output:
output the sizes of the 5 largest SCCs in the given graph, in decreasing order sizes, separated by commas. 
Keep in mind memory management due to file size... 
'''




def DFS(G, vertex, visited, stack):
    if vertex not in visited:
        # mark vertex as explored
        visited.append(vertex)
        print(vertex)
    # for every edge (s, v)
        for edge in G[vertex]:
            DFS(G, edge, visited, stack)




def main():
    test1File = "Module2/SCC/input_mostlyCycles_10_32.txt" # should return 11, 10, 5, 4, 1
    test2File = "Module2/SCC/input_mostlyCycles_20_128.txt" # should return 61, 46, 15, 3, 2
    test3File = "Module2/SCC/input_mostlyCycles_1_8.txt" # should return 4, 2, 2, 0, 0
    homeworkFile = "Module2/SCC/scc.txt"

    fileName = test3File
    graph_file = open(fileName)
    # define empty graph using a dictionary type
    graph = {}

    topFive = []
    visitedNodes = []
    stackElements = []

    for line in graph_file:
        node = int(line.split()[0])
        edges = []
        for edge in line.split()[1]:
            edges.append(int(edge))
        graph[node] = edges
    graph_file.close

    print(graph)
        



    print("main")

main()