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

import copy


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

    fileName = homeworkFile
    
    # define empty graph using a dictionary type
    graph = {}
    reverse_graph = {}

    num_nodes = 0
    topFive = []
    visitedNodes = []
    stackElements = []


    graph_file = open(fileName)
    # variables to hold node/edge data from file contents
    edgeList = []
    nodeNum = 1 #start at node1 since all text files start there

    # Below steps will create a normal graph struct: Graph{Node: [edges]}
    for line in graph_file:
        items = line.split()
        # if node number matches first column node
        if nodeNum == int(items[0]):
            # append it's edge to a running list
            edgeList.append(int(items[1]))
        # if node number doesn't match
        elif nodeNum != int(items[0]):
            # make a copy/overwrite the existing edge list
            copyEdge = copy.deepcopy(edgeList)
            # create a graph with that deepcopied edge list
            graph[nodeNum] = copyEdge
            # assign new nodeNum
            nodeNum = int(items[0])
            # clear the edge list, but not the copyEdge since values referenced
            edgeList.clear()
            # append the new edge from the new nodeNum
            edgeList.append(int((items[1])))
        # if last node reached, just used the edgeList    
        graph[nodeNum] = edgeList

# Main File Loop -------------------------------

main()