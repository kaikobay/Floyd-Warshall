#!/usr/bin/env python3
import sys
import itertools
NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
[NO_PATH, 0, 5, NO_PATH],
[NO_PATH, NO_PATH, 0, 2],
[NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])

def findMin(start, end, intermediate, distance):
    """
    Calculate minimum distance between two nodes with optional intermediates.
    :return: Minimum distance.
    """
    # Return direct distance if no intermediates
    if intermediate < 0:
        return(distance[start][end])

    # Calculate direct vs. indirect path through an intermediate
    direct = findMin(start, end, intermediate - 1, distance)
    indirect = findMin(start, intermediate, intermediate - 1, distance) + findMin(intermediate, end, intermediate -1 , distance)
    
    # Choose shorter path
    return min(direct, indirect)

def floyd(distance):
    """
    Apply Floyd's algorithm for shortest paths between all node pairs.
    """
    # Iterate through all node pairs
    for start_node, end_node in itertools.product(range(MAX_LENGTH), repeat=2):
        # Distance to self is 0
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        
        # Update matrix with shortest path
        distance[start_node][end_node] = findMin(start_node, end_node, MAX_LENGTH - 1, distance)
    return distance

if __name__ == "__main__": 
    print(floyd(graph))