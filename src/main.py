import networkx as net
import matplotlib.pyplot as plt

from src.graph import create_graph1, create_graph2
from src.ppr import personalized_pagerank, queue_based_personalized_pagerank
from src.fbca import fbca

graph = create_graph1()
# graph = create_graph2()

ppr = personalized_pagerank(graph, 'u1', 0.8, 0.1)
# ppr = personalized_pagerank(graph, '1', 0.15, 0.01)
# ppr2 = queue_based_personalized_pagerank(graph, '1', 0.85, 0.01)
# print(ppr)
# print(ppr2)

locs = fbca(graph, 'u2', 1, 10)
print(locs)

# pagerank = net.pagerank(graph)
# print(pagerank)

# net.draw(graph, pos=net.spring_layout(graph), with_labels=True)
# plt.show()
