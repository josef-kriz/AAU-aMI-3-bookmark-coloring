import networkx as net
import matplotlib.pyplot as plt

from src.graph import create_graph1, create_graph2
from src.ppr import personalized_pagerank

# graph = create_graph1()
graph = create_graph2()

# ppr = personalized_pagerank(graph, 'u1', 0.8, 0.1)
ppr = personalized_pagerank(graph, '1', 0.15, 0.02)
print(ppr)

# pagerank = net.pagerank(graph)
# print(pagerank)

# net.draw(graph, pos=net.spring_layout(graph), with_labels=True)
# plt.show()
