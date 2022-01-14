# Karger Min Cut Algorithm - Cousera(Stanford Algorithms Class)

'''
PsuedoCode
while > 2 vertices (nodes) exist:
    pick an edge (u,v) at random;
    merge (contract) u,v nodes indo a single node/vertex
    remove self loop
return the cut of the final 2 vertices (i.e. final remaining 2 vertices)
'''


#imports
import copy
import random

G = {}

# file open and read
# Stanford_Algorithms/KargerMinCut/tc2_15_50_cut14.txt
# Stanford_Algorithms/KargerMinCut/KargerMinCut.txt
with open("Stanford_Algorithms/KargerMinCut/KargerMinCut.txt") as f:
    # lines should be a single line, stripped of whitespace, and split at newline char
    lines = f.read().strip("\t").split("\n")
for line in lines:
    # for each element, split at whitespace and make char
    lst = [int(s) for s in line.split()]
    G[lst[0]] = lst[1:]


# d = {1:[2,3,4], 2:[1,4], 3:[1,4], 4:[1,2,3]}
def pickRandomEdge(g):
    k, v = random.choice(list(g.items()))
    randomEdge = random.choice(v)
    return k, v, randomEdge
    # print(k,v)
    # print(randomEdge)

def karger(g):
    global cuts
    while len(g) > 2:
        u,v_list,v = pickRandomEdge(g) # gives key, and single value from the values list of that key
        g[u].extend(g[v])

        # scan which nodes are attached r_edge's node
        for x in g[v]:
            # for whichever node selected, remove the soon to be contracted node value
            g[x].remove(v)
            # replace the contracted node in other's edges with original node
            g[x].append(u)

        #remove self loops
        while u in g[u]:
            g[u].remove(u)
        del(g[v])

        # calculate mincut by grabbing final number of edges of vertices
    mincut = len(g[list(g.keys())[0]])
    cuts.append(mincut)
    return(g, mincut)

cuts = []
count = 200
i = 0
while i < count:
    graph1 = copy.deepcopy(G)
    g = karger(graph1)
    # g = FastMinCut(graph1)
    i += 1
print("mincut is ", min(cuts))





# Test build operations

# d = {1:[2,3,4], 2:[1,4], 3:[1,4], 4:[1,2,3]}
# # mincut below is looking at dictionary d[0] key, and grabbing it's length
# mincut = len(d[list(d.keys())[0]])
# print(f"mincut value is {mincut}")
# # print(random.choice(list(d.values())))
# print("Number of keys in dict = " + str(len(d)))
# print(f"dictionary is {d}")
# # attempt to pick a random edge, after randomly selecting key/value set. Needs to be refined. 
# u,v_list,v = pickRandomEdge(d)
# print(f"After random edge call: key = {u}, values = {v_list}, r_edge = {v}")
# # make a copy of the randomly selected key/value list for reference 
# original_list = v_list.copy()
# print(f"node matched edge = {v}, values from that key = {d[v]}")
# # find original key, add on the edge list from selected random edge node
# d[u].extend(d[v])
# print(f"original key '{u}' values = {original_list}, updated values list = {d[u]}")
# # after attaching r_edge's node list to orig key, cycle through entire dictionary, removing reference of that random edge node, and replacing it
# # with original key (this will be the merged node)
# print(d)
# # scan which nodes are attached r_edge's node
# for x in d[v]:
#     # for whichever node selected, remove the soon to be contracted node value
#     d[x].remove(v)
#     # replace the contracted node in other's edges with original node
#     d[x].append(u)
# while u in d[u]:
#     # remove self loops
#     d[u].remove(u)
# del(d[v])
# mincut = len(d[list(d.keys())[0]])
# print(f"mincut value is {mincut}")
# print(d)














