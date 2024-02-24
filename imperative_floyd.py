import itertools
from config import graph, NO_PATH, MAX_LENGTH

def floyd(distance):
    for intermediate, start_node, end_node in itertools.product (range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        distance[start_node][end_node] = min(distance[start_node][end_node],distance[start_node][intermediate] + distance[intermediate][end_node])
    
    print(distance)

floyd(graph)