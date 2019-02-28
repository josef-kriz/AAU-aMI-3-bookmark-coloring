

# Implementation of personalized pagerank (PPR) with the coloring bookmark algorithm (CBA)
# graph - networkx graph with nodes and edges
# bookmark - a node we simulate the spread of paint from
# alpha - each node keeps 1−alpha portion of the paint that it receives
# epsilon - the process terminates if the paint to be redistributed at each node exceeds a small constant epsilon
def personalized_pagerank(graph, bookmark, alpha, epsilon):
    b = {}
    pi = {}
    for node in graph.nodes():  # initialize b and pi
        pi[node] = 0
        b[node] = 0
        b[bookmark] = 1

    for i in range(0, 1):  # should be while
        for node in graph.nodes():
            # print(node, b)
            # print(' ', pi)
            if b[node] < epsilon:
                continue

            pi[node] = pi[node] + (1 - alpha) * b[node]
            # print(node)
            for neighbor in graph[node].keys():
                # print(' ' + neighbor, b[neighbor] + alpha * b[node] / len(graph[node].keys()))
                b[neighbor] = b[neighbor] + alpha * b[node] / len(graph[node].keys())

    return pi
