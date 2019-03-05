from src.ppr import personalized_pagerank

alpha = 0.8
epsilon = 0.001


# Friendship-based Bookmark-coloring Algorithm (FBCA)
# Hao Wang, Manolis Terrovitis, and Nikos Mamoulis. 2013. Location recommendation in location-based
# social networks using user check-in data. Algorithm 2
# graph - a LBSN
# user - the target user
# distance - a threshold for geographical distance
# n - the number of new locations to recommend
def fbca(graph, user, distance, n):
    visited_locations = []
    for location in graph[user].keys():
        if graph.nodes[location]['type'] == 'location':
            visited_locations.append(location)

    users = list(filter(lambda node: graph.nodes[node]['type'] == 'user' and node != user, graph.nodes()))
    pi = {}
    for other_user in users:
        pi[other_user] = personalized_pagerank(graph, other_user, alpha, epsilon)[other_user]  # TODO is this correct?

    locations = list(filter(lambda node: graph.nodes[node]['type'] == 'location' and node not in visited_locations, graph.nodes()))
    s = {}
    for location in locations:
        s[location] = 0

    # TODO lines 4-14

    return
