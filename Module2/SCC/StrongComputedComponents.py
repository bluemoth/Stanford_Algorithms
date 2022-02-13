'''
Algorithm for computing strongly connected components (Kosaraju's Two-Pass Algorithm) - Stanford/Coursera
'''


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
def DFS_Loop(Graph, times=0):
    global finish_time_log 
    global finish_time
    global s
    global explored_list
    global stack
    global leader
    global current_node_list
    # leader variable relevant on seond pass
    s = None
    finish_time_log = {}
    explored_list = [False] * maxNodeCount
    current_node_list = []
    finish_time = 0

    if times == 0:
        for i in Graph:
            # for each node within list, if not explored, set leader to that node
            if explored_list[i] == False:
                s = i
                DFS_recursive(Graph,i)
    else:
        for i in times:
            if explored_list[i] == False:
                s = i
                DFS_recursive(Graph,i)
            if s not in leader:
                leader[s] = len(current_node_list)
                current_node_list = []

# recursive setup of DFS
def DFS_recursive(Graph, vertex):
    global finish_time_log 
    global finish_time
    global s
    global explored_list
    global stack
    global leader
    global current_node_list

    explored_list.append(vertex)
    current_node_list.append(vertex)
    if vertex in Graph:
        for edge in Graph[vertex]:
            if explored_list[edge] == False:
                DFS_recursive(Graph, edge)
        finish_time += 1
        finish_time_log[edge] = finish_time

def DFS_Loop_Iter(Graph, times=0):
    global finish_time_log 
    global finish_time
    global s
    global explored_list
    global stack
    global leader
    global current_node_list
    # leader variable relevant on seond pass
    s = None
    finish_time = 0
    finish_time_log = {}
    explored_list = [False] * maxNodeCount
    current_node_list = [] 

    if times == 0:
        for i in Graph:
            current_node_list = [] 
            # for each node within list, if not explored, set leader to that node
            if explored_list[i] == False:
                s = i
                DFS_iterative(Graph,i)
    else:
        for i in times:
            if explored_list[i] == False:
                s = i
                DFS_iterative(Graph,i)
            if s not in leader:
                leader[s] = len(current_node_list)
                current_node_list = []

def DFS_iterative(Graph, vertex):
    global finish_time_log 
    global finish_time
    global s
    global explored_list
    global stack
    global leader
    global current_node_list

    stack = [vertex]
    while stack:
        v = stack[-1]
        if v in Graph:
            if explored_list[v] == False:
                explored_list[v] = True
                current_node_list.append(v)
                for w in Graph[v]:
                    stack.append(w)
            else: 
                if v not in finish_time_log:
                    finish_time +=1 
                    finish_time_log[v] = finish_time
                stack.pop()
        else:
            stack.pop()
            
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
    test3File = "/Users/jacobcase/Documents/Projects/Workspace/Stanford_Algorithms/Module2/SCC/input_mostlyCycles_1_8.txt" # should return 4, 2, 2, 0, 0
    test4File = "Module2/SCC/input_mostlyCycles_11_32.txt" # should return 16,8,5,2,1
    test5File = "Module2/SCC/input_mostlyCycles_30_800.txt" # should return 437,256,51,44,10
    test6File = "Module2/SCC/input_mostlyCycles_68_320000.txt" # 271384,33830,9100,3102,850
    test7File = "Module2/SCC/Jsemko_1.txt" # 3,3,3,0,0
    test8File = "Module2/SCC/Jsemko_2.txt" # 6,3,2,1,0    
    test9File = "Module2/SCC/MB_1.txt" # 3,1,1,0,0  
    homeworkFile = "/Users/jacobcase/Documents/Projects/Workspace/Stanford_Algorithms/Module2/SCC/scc.txt"

    

    # globals
    global finish_time_log 
    global finish_time
    global s
    global explored_list
    global stack
    global leader
    global current_node_list
    global maxNodeCount
        
    maxNodeCount = 875715 # homework # of nodes 875715
    finish_time_log = {}
    leader = {}
    finish_time = 0
    s = None
    explored_list = [False] * maxNodeCount 
    stack = [] 


    # setup - construct the graph from file
    graph = build_graph(filename=homeworkFile)

    # Step 1: Create graph and reverse graph
    rev_graph = transposeGraph(graph)
    # print(rev_graph,"\n")

    # Step 2: run DFS Loop on Grev -> Purpose is to compute ordering of nodes by finishing times (stord in dictionary)
    # DFS_Loop(graph)
    # # print(explored_list)
    # print(finish_time_log) 

    DFS_Loop_Iter(rev_graph)
    # print(explored_list)
    # print(finish_time_log)
    
    reverse_times = []
    for node in finish_time_log:
        reverse_times.append(node)
    reverse_times.reverse()
    # print(reverse_times)

    # # Step 3: run DFS loop again on G -> but this time, the order of the processing needs to be done in computed order, completed above
    # DFS_Loop(graph, reverse_times)    
    # # print("\n")
    # for leader_node, node_count in leader.items():
    #     print(leader_node, node_count)

    DFS_Loop_Iter(graph, reverse_times)
    # print("\n")
    # for leader_node, node_count in leader.items():
    #     print(leader_node, node_count)
    scc = sorted(leader.values())
    print(scc[-5:])
    # 13Feb2022 - above produces correct answer
# ------------------------------- Main File -------------------------------

main()