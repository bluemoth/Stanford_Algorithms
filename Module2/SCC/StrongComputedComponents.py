'''
Algorithm for computing strongly connected components (Kosaraju's Two-Pass Algorithm) - Stanford/Coursera

14Feb2021
Bugs:
-Iterative approach works for discovering all nodes, however computing the correct finishing time log doesn't compute correctly for test7 and test9
    -This is because during exploration with edges reversed, new nodes pushed to the stack in wrong order
    -A method to resolve this may be to log the parent node and consider that during backtracking

-Recursive approach passes all files but test9
'''
import time

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
def DFS_Loop(Graph, times=0, recursive=False):
    global finish_time_log, finish_time, s, explored_list, stack, leader, current_node_count
    # leader variable relevant on seond pass
    s = None
    finish_time_log = {}
    explored_list = [False] * maxNodeCount
    current_node_count = 0
    finish_time = 0
    stack = []

    if times == 0:
        for i in Graph:
            # for each node within list, if not explored, set leader to that node
            if explored_list[i] == False:
                s = i
                if recursive == True:
                    DFS_recursive(Graph,i)
                else:
                    DFS_iterative(Graph,i)
    else:
        for i in times:
            if explored_list[i] == False:
                s = i
                if recursive == True:
                    DFS_recursive(Graph,i)
                else:
                    DFS_iterative(Graph,i)
            if s not in leader:
                leader[s] = current_node_count
                current_node_count = 0

# recursive setup of DFS
def DFS_recursive(Graph, vertex):
    global finish_time_log, finish_time, s, explored_list, stack, leader, current_node_count

    explored_list[vertex] = True
    current_node_count += 1
    if vertex in Graph:
        for edge in Graph[vertex]:
            if explored_list[edge] == False:
                DFS_recursive(Graph, edge)
        finish_time += 1
        finish_time_log[edge] = finish_time

# iterative DFS approach using stack
def DFS_iterative(Graph, vertex):
    global finish_time_log, finish_time, s, explored_list, stack, leader, current_node_count

    stack = [vertex]
    while stack:
        v = stack[-1]
        if v in Graph:
            if explored_list[v] == False:
                explored_list[v] = True
                current_node_count += 1
                for w in Graph[v]:
                    stack.append(w)
            # node already explored, log finish time and continue backtrack
            else:
                if v not in finish_time_log:
                    finish_time +=1 
                    finish_time_log[v] = finish_time
                stack.pop()
        else:
            explored_list[v] = True
            finish_time += 1
            finish_time_log[v] = finish_time
            stack.pop()
            
def transpose_graph(Graph):
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
    test1 = "Module2/SCC/input_mostlyCycles_10_32.txt" # should return 11, 10, 5, 4, 1
    test2 = "Module2/SCC/input_mostlyCycles_20_128.txt" # should return 61, 46, 15, 3, 2
    test3 = "Module2/SCC/input_mostlyCycles_1_8.txt" # should return 4, 2, 2, 0, 0
    test4 = "Module2/SCC/input_mostlyCycles_11_32.txt" # should return 16,8,5,2,1
    test5 = "Module2/SCC/input_mostlyCycles_30_800.txt" # should return 437,256,51,44,10
    test6 = "Module2/SCC/input_mostlyCycles_68_320000.txt" # 271384,33830,9100,3102,850
    test7 = "Module2/SCC/Jsemko_1.txt" # 3,3,3,0,0
    test8 = "Module2/SCC/Jsemko_2.txt" # 6,3,2,1,0    
    test9 = "Module2/SCC/MB_1.txt" # 3,1,1,0,0  
    SCCFile = "Module2/SCC/scc.txt"

    # globals
    global finish_time_log, finish_time, s, explored_list, stack, leader, current_node_count, maxNodeCount
        
    maxNodeCount = 875715 # homework # of nodes 875715
    finish_time_log = {}
    leader = {}

    #time tracking
    start = time.time()

    #Step 1: - construct the graph from file
    graph = build_graph(filename=SCCFile)

    #transpose graph
    rev_graph = transpose_graph(graph)

    # Step 2: run DFS Loop on Grev -> Purpose is to compute ordering of nodes by finishing times (stord in dictionary)
    DFS_Loop(rev_graph)

    #reverse finish time for nodes
    reverse_times = []
    for node in finish_time_log:
        reverse_times.append(node)
    reverse_times.reverse()


    # # Step 3: run DFS loop again on G -> but this time, the order of the processing needs to be done in computed order, completed above
    DFS_Loop(graph, reverse_times)
    print("Time to complete Kosaraju: ", time.time()-start)
    scc = sorted(leader.values())
    print(scc[-5:])

# ------------------------------- Main File -------------------------------

main()