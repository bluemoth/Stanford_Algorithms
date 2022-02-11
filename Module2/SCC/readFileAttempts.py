#  Below steps will create a normal graph struct: Graph{Node: [edges]}
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