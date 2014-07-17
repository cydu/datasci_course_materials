import MapReduce
import sys

"""
Assume you have two matrices A and B in a sparse matrix format, where each record is of the form i, j, value. Design a MapReduce algorithm to compute the matrix multiplication A x B
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

N = 100

def mapper(record):
    matrix = record[0]
    if matrix == 'a':
        for k in range(0, N):
            mr.emit_intermediate((record[1], k), (matrix, record[2], record[3]))
    else:
        for k in range(0, N):
            mr.emit_intermediate((k, record[2]), (matrix, record[1], record[3]))

def reducer(key, list_of_values):
    hash_A = {j: a_ij for (x, j, a_ij) in list_of_values if x == 'a'}
    hash_B = {j: b_jk for (x, j, b_jk) in list_of_values if x == 'b'}
    
    result = 0
    for k in range(0, N):
        result += hash_A.get(k, 0) * hash_B.get(k, 0)
    if result != 0:
        mr.emit((key[0], key[1], result))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
