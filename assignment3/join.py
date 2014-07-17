import MapReduce
import sys

"""
Implement a relational join as a MapReduce query
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    for order in list_of_values:
        if order[0] != 'order':
            continue
        for line_item in list_of_values:
            if line_item[0] != 'line_item':
                continue
            mr.emit(order + line_item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
