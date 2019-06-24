import networkx as net
import matplotlib.pyplot as plt
from src.graph import create_graph1, create_graph2
from src.ppr import personalized_pagerank, queue_based_personalized_pagerank
from src.fbca import fbca

# NOTES:
# - the problem of original page rank is the teleport that makes the matrix dense
# - which results in memory heavy applications but also requires more computations
# - bookmark coloring - the main idea is to spread "color" from a bookmarked node
# - the amount of color decreases every time an edge is traversed (alpha constant)
# - IMPROVE: getting neighbors requires I/O operations (caching techniques)
# - IMPROVE: weights to edges
# - we used it for location based recommendations
# - given a set of friends, recommend places to visit
# FRIENDS BASED BOOKMARK COLORING
# - recommend places according to friend ties
# - two steps - compute importance of friends, use their visits to recommend places
# LIMITATIONS
# - small graph, can't really use metrics precision/recall
# - results make sense, explain

graph = create_graph1()
# graph = create_graph2()

locs = fbca(graph, 'u2', 1, 10)
print(locs)

# pagerank = net.pagerank(graph)
# print(pagerank)

# net.draw(graph, pos=net.spring_layout(graph), with_labels=True)
# plt.show()
