import networkx as net


# Hao Wang, Manolis Terrovitis, and Nikos Mamoulis. 2013.
# Location recommendation in location-based social networks using user check-in data.
# Figure 5
def create_graph1():
    graph = net.Graph()

    graph.add_node('u1', type='user')
    graph.add_node('u2', type='user')
    graph.add_node('u3', type='user')
    graph.add_node('l1', type='location')
    graph.add_node('l2', type='location')
    graph.add_node('l3', type='location')

    graph.add_edge('u1', 'u3')
    graph.add_edge('u2', 'u3')

    graph.add_edge('u1', 'l1', weight=7)
    graph.add_edge('u1', 'l2', weight=3)
    graph.add_edge('u3', 'l2', weight=1)
    graph.add_edge('u3', 'l3', weight=1)

    return graph


# Example from the excel sheet from course's materials
def create_graph2():
    graph = net.DiGraph()

    graph.add_node('1')
    graph.add_node('2')
    graph.add_node('3')
    graph.add_node('4')

    graph.add_edge('1', '2')
    graph.add_edge('2', '1')
    graph.add_edge('1', '3')
    graph.add_edge('2', '3')
    graph.add_edge('3', '4')
    graph.add_edge('2', '4')
    graph.add_edge('4', '2')

    return graph
