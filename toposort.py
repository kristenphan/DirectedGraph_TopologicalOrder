#Uses python3

import sys


# this function takes in an adjacent list representation of a directed acyclic graph (DAG),
# list 'used' to keep track of which nodes have been previously visited,
# list 'order' that will be used later to construct a topological order of the DAG
# and a vertex 'v' where it will perform depth first search from.
# the function performs a depth first search (DFS) from vertex v and add nodes visited along the way to list 'order'
# list 'order' should arrange vertices with postorders from smallest to largest
def dfs(adj, used, order, v):
    used[v] = True # mark the vertex being traversed as visited
    if len(adj[v]) > 0:
        for adj_node in adj[v]: # search for adjacent vertices
            if not used[adj_node]: # if any of them is not yet visited, traverse down that path in DFS manner
                dfs(adj, used, order, adj_node)
    # after reaching the sink vertex of a path,
    # backtrack and append the vertex to list 'order'
    order.append(v)


# this function takes in an adjacent list representation of a directed acyclic graph (DAG)
# and returns a topological order of said graph
# a DAG might have multiple topological orders. this function will return one of them
def toposort(adj):
    used = [False] * len(adj)
    order = []
    for v in range(len(adj)):
        if not used[v]:
            dfs(adj, used, order, v)

    # list 'order' arranges vertices with postorders from smallest to largest
    # to obtain a topological order, need to reverse the list to rearrange vertices from largest postorder to smallest
    order.reverse()

    return order


# this program reads the input, builds an adjacent list representation of a directed acyclic graph (DAG)
# and returns one of its topological order (a DAG might have multiple topological orders)
# input and output represent a DAG in 1-based index
# example:
# input (and how to interpret input):
# 4 3 (n = number of vertices = 4; m = number of edges = 3)
# 0 1 (a directed edge going from 0 to 1)
# 2 0 (a directed edge going from 2 to 0)
# 3 0 (a directed edge going from 3 to 0)
# output: 3 2 0 1
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    #adj = [[1], [], [0], [0]]
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
