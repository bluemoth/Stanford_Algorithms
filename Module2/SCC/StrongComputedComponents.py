'''
Algorithm for computing strongly connected components (Kosaraju's Two-Pass Algorithm) - Stanford/Coursera
'''

#Errors/bugs:
# input text leaves out nodes that aren't connected
# keyErrors will appear due to this



# udpdated method to pull info from file and build dictionary using set
def build_graph(filename):
	graph = dict()
	with open(filename, 'r') as file:
		for line in file:
			vertex, edge = line.split()
			vertex, edge = int(vertex), int(edge)
            # grab existing edges from key if avaiable, otherwise (None)
			edge_list = graph.get(vertex, set())
            # append the edge to list
			edge_list.add(edge)
            # assigne edge list to specified vertex 
			graph[vertex] = edge_list
	return graph

# DFS top loop for computing SCCs
# also provides feedback on leader nodes
def DFS_Loop(Graph, times=0):
    global finish_time_log 
    global finish_time
    global s
    global explored_list
    global current_node_list
    # leader variable relevant on seond pass
    s = None
    finish_time_log = {}
    explored_list = []
    current_node_list = []

    if times == 0:
        for i in Graph:
            # for each node within list, if not explored, set leader to that node
            if i not in explored_list:
                s = i
                DFS_recursive(Graph,i)
    else:
        for i in times:
            if i not in explored_list:
                s = i
                DFS_recursive(Graph,i)
            if s not in leader:
                leader[s] = len(current_node_list)
                current_node_list = []

# recursive setup of DFS
def DFS_recursive(Graph, start):
    global finish_time_log 
    global finish_time
    global s
    global explored_list
    global current_node_list

    vertex = start
    explored_list.append(vertex)
    current_node_list.append(vertex)
    for edge in Graph[vertex]:
        if edge not in explored_list:
            DFS_recursive(Graph, edge)
    finish_time += 1
    finish_time_log[edge] = finish_time

def transposeGraph(Graph):
    edge_list = set()
    new_graph = dict()
    for node, edges in Graph.items():
        for edge in edges:
            edge_list.add((node, edge))
    for item in edge_list:
        new_edge = new_graph.get(item[1],set())
        new_edge.add(item[0])
        new_graph[item[1]] = new_edge
    return new_graph

def main():
    # file names
    test1File = "Module2/SCC/input_mostlyCycles_10_32.txt" # should return 11, 10, 5, 4, 1
    test2File = "Module2/SCC/input_mostlyCycles_20_128.txt" # should return 61, 46, 15, 3, 2
    test3File = "Module2/SCC/input_mostlyCycles_1_8.txt" # should return 4, 2, 2, 0, 0
    test4File = "Module2/SCC/input_mostlyCycles_11_32.txt" # should return 16,8,5,2,1
    test5File = "Module2/SCC/input_mostlyCycles_30_800.txt" # should return 437,256,51,44,10
    homeworkFile = "Module2/SCC/scc.txt"

    maxNodeCount = 875715 # homework # of nodes

    # globals
    global finish_time_log 
    global finish_time
    global s
    global explored_list
    global stack_list
    global leader

    finish_time_log = {}
    leader = {}
    finish_time = 0
    s = None
    explored_list = []
    stack_list = []

    # setup - construct the graph from file
    # print("\nGraph constructed from file:")
    graph = build_graph(filename=test3File)
    # print(graph, "\n")

    # Step 1: Create graph and reverse graph
    rev_graph = transposeGraph(graph)
    print("Graph Transposed for first pass of DFS_Loop:")
    print(rev_graph,"\n")

    # Step 2: run DFS Loop on Grev -> Purpose is to compute ordering of nodes by finishing times (stord in dictionary)
    # from lecture: The depth first search on reverse graph is going to compute an ordering of the nodes which, 
    # when the second depth first search goes through them in that order, it will just discover the SCCs one at a time.
    DFS_Loop(graph)
    # print("Finishing times as a result of running DFS_Loop(rev_graph):")
    # print(finish_time_log,"\n") # finishing times are different between DFS_Loop(graph) and DFS_Loop(rev_graph)
    
    reverse_times = []
    for node in finish_time_log:
        reverse_times.append(node)
    reverse_times.reverse()
    # print(reverse_times)

    # Step 3: run DFS loop again on G -> but this time, the order of the processing needs to be done in computed order, completed above
    DFS_Loop(graph, reverse_times)
    # print("\n")
    for leader_node, node_count in leader.items():
        print(leader_node, node_count)
# ------------------------------- Main File -------------------------------

main()