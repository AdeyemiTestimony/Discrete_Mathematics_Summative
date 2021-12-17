global count0
global count1
count0 = 0
count1 = 0
def main():# A class to represent a graph object
    class Graph:

        def __init__(self, n, edges=[]):
            # resize the list to hold `n` elements
            self.adjList = [[] for _ in range(n)]

            # add an edge from source to destination
            for edge in edges:
                self.addEdge(edge[0], edge[1])

        # Function to add an edge (u, v) to the graph
        def addEdge(self, u, v):
            self.adjList[u].append(v)
            self.adjList[v].append(u)


    # Function to perform DFS traversal on the graph on a graph
    def DFS(graph, v, discovered):
        discovered[v] = True  # mark the current node as discovered

        # do for every edge (v, u)
        for u in graph.adjList[v]:
            if not discovered[u]:  # if `u` is not yet discovered
                DFS(graph, u, discovered)


    # Function to check if all vertices with a non-zero degree in a graph
    # belong to a single connected component
    def isConnected(graph, n):
        # to keep track of whether a vertex is discovered or not
        discovered = [False] * n

        # start DFS from the first vertex with a non-zero degree
        for i in range(n):
            if len(graph.adjList[i]):
                DFS(graph, i, discovered)
                break

        # if a single DFS call couldn't visit all vertices with a non-zero degree,
        # the graph contains more than one connected component
        for i in range(n):
            if not discovered[i] and len(graph.adjList[i]):
                return False

        return True


    # Utility function to return the total number of vertices with an odd degree
    # in a graph
    def countOddVertices(graph):
        count = 0
        for list in graph.adjList:
            if len(list) & 1:
                count += 1
        return count

    from networkx.generators.random_graphs import erdos_renyi_graph


    n = 10
    p = 0.5
    g = erdos_renyi_graph(n, p)

    print("Nodes: " + str(g.nodes))
    # [0, 1, 2, 3, 4, 5]

    print("Edges: " + str(g.edges))
    # [(0, 1), (0, 2), (0, 4), (1, 2), (1, 5), (3, 4), (4, 5)]

    import matplotlib.pyplot as plt
    import networkx as nx


    pos = nx.spring_layout(g)
    nx.draw_networkx(g, pos)
    plt.title("Random Graph Generation Example")
    plt.show()
    if __name__ == '__main__':
        #global count0
        #global count1

        # List of graph edges as per the above diagram
        edges = g.edges

        # total number of nodes in the graph (labelled from 0 to 4)
        n = 10

        # create an undirected graph from the given edges
        graph = Graph(n, edges)

        # check if all vertices with a non-zero degree belong to a single
        # connected component
        is_connected = isConnected(graph, n)

        # find the total number of vertices with an odd degree
        odd = countOddVertices(graph)

        # An Eulerian path exists if all non-zero degree vertices are connected,
        # and zero or two vertices have an odd degree
        if is_connected and (odd == 0 or odd == 2):

            print('The graph has an Eulerian path')

            # A connected graph has an Eulerian cycle if every vertex has
            # an even degree
            if odd == 0:
                global count0
                global count1
                count0 += 1
                count1 += 1
                print(count1)
                print('The graph has an Eulerian cycle')

            # The graph has an Eulerian path but not an Eulerian cycle
            else:
                count0 = +1
                print(count0)
                print('The Graph is Semi–Eulerian')
        else:
            count0 = +1
            print(count1)
            print('The Graph is not Eulerian')



main()
main()
main()
main()
main()

print(count0)
probablity = count1 // count0
prob = probablity * 100
print("The probablity of getting an eulerian circuit is " + str(prob) + "%")





