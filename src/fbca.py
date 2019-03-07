from src.ppr import personalized_pagerank

alpha = 0.8
epsilon = 0.001


# Friendship-based Bookmark-coloring Algorithm (FBCA)
# Hao Wang, Manolis Terrovitis, and Nikos Mamoulis. 2013. Location recommendation in location-based
# social networks using user check-in data. Algorithm 2
# graph - a LBSN
# target - the target user
# distance - a threshold for geographical distance
# n - the number of new locations to recommend
def fbca(graph, target, distance, n):
    visited_locations = list(filter(lambda node: graph.nodes[node]['type'] == 'location', graph[target]))

    users = list(filter(lambda node: graph.nodes[node]['type'] == 'user' and node != target, graph.nodes()))
    pi = {}
    for user in users:
        pi[user] = personalized_pagerank(graph, user, alpha, epsilon)[user]

    locations = list(filter(lambda node: graph.nodes[node]['type'] == 'location' and node not in visited_locations, graph.nodes()))
    s = {}
    for location in locations:
        s[location] = 0

    for user in users:
        user_locations = list(filter(lambda node: graph.nodes[node]['type'] == 'location' and node not in visited_locations, graph[user]))
        for location in user_locations:
            s[location] = s[location] + pi[user] * graph.get_edge_data(user, location)['weight']

    # TODO lines 7-14

    return
