import queue


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


# Implementation of PPR using a queue
# Pavel Berkhin (2011) Bookmark-Coloring Algorithm for Personalized PageRank Computing, Algorithm 2
# graph - networkx graph with nodes and edges
# bookmark - a bookmark b
# alpha - a retention coefficient
# epsilon - a tolerance threshold
def queue_based_personalized_pagerank(graph, bookmark, alpha, epsilon):
    p = {}
    q = queue.Queue()
    in_queue = {}  # a list of items in the queue (because you can't iterate through a queue 😥)

    # initialize
    for node in graph.nodes():
        p[node] = 0
    q.put(bookmark)
    in_queue[bookmark] = 1

    while not q.empty():
        node = q.get()
        weight = in_queue[node]
        p[node] = p[node] + alpha * weight

        if weight < epsilon:
            continue

        for neighbor in graph[node].keys():
            neighbors_count = len(graph[node].keys())
            if neighbor in in_queue.keys():
                in_queue[neighbor] = in_queue[neighbor] + (1 - alpha) * weight / neighbors_count
            else:
                q.put(neighbor)
                in_queue[neighbor] = (1 - alpha) * weight / neighbors_count

    return p
