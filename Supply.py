# CS4102 Spring 2022 - Unit B Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the
# comments at the top of each submitted file. Do not share written notes,
# documents (including Google docs, Overleaf docs, discussion notes, PDFs), or
# code. Do not seek published or online solutions, including pseudocode, for
# this assignment. If you use any published or online resources (which may not
# include solutions) when completing this assignment, be sure to cite them. Do
# not submit a solution that you are unable to explain orally to a member of
# the course staff. Any solutions that share similar text/code will be
# considered in breach of this policy. Please refer to the syllabus for a
# complete description of the collaboration policy.
#################################
# Your Computing ID: rjl4sw
# Collaborators:
# Sources: Introduction to Algorithms, Cormen
#################################
edgeWeightSum = 0
set
dep={}
def extract(raw_edges):
    global dep
    nodes = int(raw_edges[0][0])
    dependencies=[]
    stores=[]
    for f in raw_edges[1:nodes+1]:
        stores.append(f[0])
        if "d" in f[0]:
            dependencies.append(f[0])
    for d in dependencies:
        dep[d] = []
    key = ""
    for r in stores:
         if "d" in r:
            key = r
         if "s" in r:
            dep[key].append(r)
    print(dep)
    p_edges = (sorted(truncator(list((x[0],x[1],int(x[2])) for x in raw_edges[nodes+1:])), key=lambda x: x[2]))
    disjoint={f:f for f in list(x[0] for x in raw_edges[1:nodes+1])}
    return nodes, p_edges, disjoint

def truncator(edges):
    global dep
    index=0
    print(len(edges))
    new_edges=edges[:]
    for e in edges:
        if e == ("dc1","s2",1):
            print("accounted for!")
        if "p" in e[0] or "p" in e[1]:
            if "s" in e[0] or "s" in e[1]:
                new_edges.remove(e)
        if "r" in e[0] or "r" in  e[1]:
            if "s" in e[0] or "s" in  e[1]:
                new_edges.remove(e)
        if "d" in e[0] and "d" in e[1]:
            new_edges.remove(e)
        if "d" in e[0] and "s" in e[1]:
            if e[1] in dep[e[0]]:
                print("keeping")
                print(e)
            else:
                print("deleting")
                print(e)
                new_edges.remove(e)
        "This stops ports from being able to reach other ports"
        # elif "p" in e[0] and "p" in e[1]:
        #     edges.remove(e)
        #elif "s" in e[0] or "s" in e[1]:
        #    if "d" in e[0] or "d" in e[1]:
        #        if e[1] == edges[index-1][1] and ("d" in e[0] and "d" in edges[index-1][0]):
        #            if e[2] < edges[index-1][2]:
        #            else:
        #                edges.remove(e)
        index += 1
    return new_edges

def find(x):
    global set
    if x == set[x]:
        return x
    else:
        return find(set[x])

def union(x,y):
    global set
    x = find(x)
    y = find(y)
    set[x] = y

def kruskal(data):
    global edgeWeightSum
    global set
    num_nodes=data[0]
    edges=data[1]
    set=data[2]
    index=0
    min_span_tree = []
    while len(min_span_tree) < num_nodes-1:
        (s,d,dist) = edges[index]
        x = find(s)
        y = find(d)
        if x != y:
            union(x,y)
            min_span_tree.append((s,d,dist))
            edgeWeightSum += dist
        index += 1
    print(min_span_tree)
    return edgeWeightSum

class Supply:
    def __init__(self):
        return
    # This is the method that should set off the computation
    # of the supply chain problem.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the total edge-weight sum
    # and return that value from this method
    #
    # @return the total edge-weight sum of a tree that connects nodes as described
    # in the problem statement


    def compute(self, file_data):
        raw_edges = [tuple(str(i) for i in numbers.split()) for numbers in file_data]
        edgeWeightSum=kruskal(extract(raw_edges))
        return edgeWeightSum