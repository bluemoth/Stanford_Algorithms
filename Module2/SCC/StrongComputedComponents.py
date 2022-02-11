'''
Algorithm for computing strongly connected components. 
File format (directed graph):
-Vertices labeled 1-875714
-Edges are indicated by rows
-vertex lebel in first column i sthe tail, and the vertex in second column is the head
Example:
11th row => "2 47646", meaning vertex with label 2 has an outgoing edge to vertex label 47646

Instructions: Use SCC algorithm from lecture 
Make sure when using DFS procedures, iterative (stack) approach is taken rather than recursive

Output:
output the sizes of the 5 largest SCCs in the given graph, in decreasing order sizes, separated by commas. 
Keep in mind memory management due to file size... 
'''

def DFS_iter(Graph, start, explored, stack):
    vertex = start
    stack.append(vertex)
    while stack:
        u = stack.pop(0)
        if u not in explored:
            explored.append(u)
            stack = Graph[u] + stack

def main():
    # file names
    test1File = "Module2/SCC/input_mostlyCycles_10_32.txt" # should return 11, 10, 5, 4, 1
    test2File = "Module2/SCC/input_mostlyCycles_20_128.txt" # should return 61, 46, 15, 3, 2
    test3File = "Module2/SCC/input_mostlyCycles_1_8.txt" # should return 4, 2, 2, 0, 0
    homeworkFile = "Module2/SCC/scc.txt"

      # node counts per text file
    test1NodeCount = 128
    test2NodeCount = 30
    test3NodeCount = 9
    maxNodeCount = 875715

    # create edge lists that will later be used to populate graph adj list
    g_edgeList = [[] for i in range(test3NodeCount)]
    r_g_edgeList = [[] for i in range(test3NodeCount)]

    # define empty graph using a dictionary type
    graph = {}
    rev_graph = {}

    # file to open
    fileName = test3File
    graph_file = open(fileName)

    # generate edge lists from file
    for line in graph_file:
        items = line.split()
        g_edgeList[int(items[0])] += [int(items[1])]
        r_g_edgeList[int(items[1])] += [int(items[0])]
    
    # because complaining...
    adj_length = len(g_edgeList)

    # merge edge list into keys
    for i in range(1,adj_length):
        graph[i] = g_edgeList[i]

    for i in range(1,adj_length):
        rev_graph[i] = r_g_edgeList[i]


    # overhead items
    explored_list = []
    stack_list = []

    for i in range(test3NodeCount-1,0,-1):
        DFS_iter(graph, i, explored_list, stack_list)

    print(explored_list)
    

# ------------------------------- Main File Loop -------------------------------

main()