from src.ppr import personalized_pagerank

alpha = 0.8
epsilon = 0.001


# Friendship-based Bookmark-coloring Algorithm (FBCA)
# Hao Wang, Manolis Terrovitis, and Nikos Mamoulis. 2013. Location recommendation in location-based
# social networks using user check-in data. Algorithm 2
# graph - a LBSN
# target - the target user
# max_dist - a threshold for geographical distance
# n - the number of new locations to recommend
def fbca(graph, target, max_dist, n):
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

    r = {}

    for location in locations:
        if 0 > max_dist:  # the real distance between the location and user's locations is not considered
            continue

        if len(r) < n:
            r[location] = s[location]
        elif s[location] <= r[min(r, key=r.get)]:
            continue
        else:
            r.pop(min(r, key=r.get))
            r[location] = s[location]

    return r
