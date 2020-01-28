# 2d_array_neighbours
This functions finding all neighbors for each element in 24 array(matrix)


Array example (INPUT):

arr = [['a', 'b', 'c'],
       ['d', 'e', 'f'],
       ['g', 'h', 'k']]


find_all_neighors result (OUTPUT):

[{'index': 0, 'value': 'a', 'neighbors': ['b', 'e', 'd']}
  {'index': 1, 'value': 'b', 'neighbors': ['c', 'f', 'e', 'd', 'a']}
  {'index': 2, 'value': 'c', 'neighbors': ['f', 'e', 'b']}
  {'index': 3, 'value': 'd', 'neighbors': ['a', 'b', 'e', 'h', 'g']}
  {'index': 4, 'value': 'e', 'neighbors': ['a', 'b', 'c', 'f', 'k', 'h', 'g', 'd']}
  {'index': 5, 'value': 'f', 'neighbors': ['b', 'c', 'k', 'h', 'e']}
  {'index': 6, 'value': 'g', 'neighbors': ['d', 'e', 'h']}
  {'index': 7, 'value': 'h', 'neighbors': ['d', 'e', 'f', 'k', 'g']}
  {'index': 8, 'value': 'k', 'neighbors': ['e', 'f', 'h']}]

       
