#!/usr/bin/env python3
import unittest
import sys
from recursive_floyd import findMin, floyd, NO_PATH

class TestFloydWarshall(unittest.TestCase):
    # Setup test cases with predefined graphs
    def setUp(self):
        # Define a graph with paths and NO_PATH for unreachable nodes

        self.graph = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        # A single-node graph for edge case tests
        self.single_node_graph = [[0]]

    # Test correct path calculation
    def test_floyd_algorithm(self):
        # Expected result after running the algorithm
        expected_result = [
            [0, 7, 12, 8],
            [NO_PATH, 0, 5, 7],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        result = floyd(self.graph)
        # Verify the algorithm produces the expected result
        self.assertEqual(result, expected_result, "floyd function failed to produce the expected result.")
    
    # Test basic scenario
    def test_findMin_basic(self):
        self.assertEqual(findMin(0, 1, 3, self.graph), 7, "findMin failed for basic scenario.")

    # Test single node graph
    def test_findMin_single_node(self):
        self.assertEqual(findMin(0, 0, 0, self.single_node_graph), 0, "findMin failed for single node graph.")

if __name__ == '__main__':
    unittest.main()
