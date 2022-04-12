# A class to represent a disjoint set



class DisjointSet:
    parent = {}

    # perform MakeSet operation
    def makeSet(self, n):
        # create `n` disjoint sets (one for each vertex)
        for i in n:
            self.parent[i] = i

    # Find the root of the set in which element `k` belongs
    def find(self, k):
        if self.parent[k] == k:
            return k

        # recur for the parent until we find the root
        return self.find(self.parent[k])

    # Perform Union of two subsets
    def union(self, a, b):
        # find the root of the sets in which elements `x` and `y` belongs
        x = self.find(a)
        y = self.find(b)
        self.parent[x] = y


# Function to construct MST using Kruskal’s algorithm
def runKruskalAlgorithm(edges, n):

    # stores the edges present in MST
    MST = []

    # Initialize `DisjointSet` class.
    # Create a singleton set for each element of the universe.
    ds = DisjointSet()
    nodes=["p1","rh1","rh2","dc1","s1","s2"]
    testset = {}
    for f in nodes:
        testset[f] = f
    beta={f:f for f in nodes}
    ds.makeSet(nodes)


    index = 0

    # sort edges by increasing weight
    edges.sort(key=lambda x: x[2])

    # MST contains exactly `V-1` edges
    while (len(MST) != n - 1):

        # consider the next edge with minimum weight from the graph
        (src, dest, weight) = edges[index]
        index = index + 1


        # find the root of the sets to which two endpoints
        # vertices of the next edge belongs
        x = ds.find(src)
        y = ds.find(dest)
        # if both endpoints have different parents, they belong to
        # different connected components and can be included in MST
        if x != y:
            MST.append((src, dest, weight))
            ds.union(x, y)

    return MST


if __name__ == '__main__':

    # (u, v, w) triplet represent undirected edge from
    # vertex `u` to vertex `v` having weight `w`
    edges = [
        ("p1", "rh1", 5), ("p1", "rh2", 1), ("p1", "dc1", 4), ("rh1", "dc1", 1), ("rh1", "rh2", 2), ("rh2", "dc1", 2),
        ("rh2", "s1", 1), ("dc1", "s2", 1), ("dc1", "s1", 6), ("s2", "s1", 2)
    ]

    # total number of nodes in the graph (labelled from 0 to 6)
    n = 6
    c = 10
    for e in edges:
        if "p" in e[0] or "p" in  e[1]:
            if "s" in e[0] or "s" in  e[1]:
                edges.remove(e)
        elif "r" in e[0] or "r" in  e[1]:
            if "s" in e[0] or "s" in  e[1]:
                edges.remove(e)
        elif "d" in e[0] and "d" in e[1]:
            edges.remove(e)

    # construct graph
    e = runKruskalAlgorithm(edges, n)
    print(e)
    f = sum(e[i][2] for i in range(len(e)))
    print(f)
