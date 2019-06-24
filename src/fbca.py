from src.ppr import personalized_pagerank, queue_based_personalized_pagerank

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
    # locations visited by the target user
    visited_locations = list(filter(lambda node: graph.nodes[node]['type'] == 'location', graph[target]))

    # get all other users
    users = list(filter(lambda node: graph.nodes[node]['type'] == 'user' and node != target, graph.nodes()))
    pi = {}
    # compute importance of all users using ppr
    for user in users:
        pi[user] = personalized_pagerank(graph, user, alpha, epsilon)[user]

    print(pi)

    # get all locations not visited by current user
    locations = list(filter(lambda node: graph.nodes[node]['type'] == 'location' and node not in visited_locations, graph.nodes()))
    s = {}
    for location in locations:
        s[location] = 0

    # compute importance of locations based on friends importance
    for user in users:
        user_locations = list(filter(lambda node: graph.nodes[node]['type'] == 'location' and node not in visited_locations, graph[user]))
        for location in user_locations:
            s[location] = s[location] + pi[user] * graph.get_edge_data(user, location)['weight']

    r = {}

    # return top n recommendations
    for location in locations:
        if 0 > max_dist:  # the real distance between the location and user's locations is not considered
            continue

        # if not enough recommendations, use the location
        if len(r) < n:
            r[location] = s[location]
        # if we have enough and importance is lower or equal to already recommended, skip
        elif s[location] <= r[min(r, key=r.get)]:
            continue
        # otherwise change the least important with the current
        else:
            r.pop(min(r, key=r.get))
            r[location] = s[location]

    return r
