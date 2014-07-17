import MapReduce
import sys

"""
Assume you have two matrices A and B in a sparse matrix format, where each record is of the form i, j, value. Design a MapReduce algorithm to compute the matrix multiplication A x B
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

from collections import defaultdict
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
    hash_ab = defaultdict(list)
    for item in list_of_values:
        hash_ab[item[1]].append(item[2])
    
    result = 0
    for k, v in hash_ab.iteritems():
        if len(v) >= 2:
            result += v[0] * v[1]
    if result != 0:
        mr.emit((key[0], key[1], result))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
