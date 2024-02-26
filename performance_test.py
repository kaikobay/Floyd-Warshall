import timeit
import copy
import sys
from imperative_floyd import floyd as imperative_floyd
from recursive_floyd import floyd as recursive_floyd

original_graph = [[0, 7, sys.maxsize, 8],
                  [sys.maxsize, 0, 5, sys.maxsize],
                  [sys.maxsize, sys.maxsize, 0, 2],
                  [sys.maxsize, sys.maxsize, sys.maxsize, 0]]

def measure_time(func, graph):
    # Time the execution of a function
    start_time = timeit.default_timer()
    func(copy.deepcopy(graph))
    end_time = timeit.default_timer()
    return end_time - start_time

# Measure and print execution times for both algorithms
time_imperative = measure_time(imperative_floyd, original_graph)
time_recursive = measure_time(recursive_floyd, original_graph)

print(f"Imperative Floyd function execution time: {time_imperative} seconds")
print(f"Recursive Floyd function execution time: {time_recursive} seconds")
