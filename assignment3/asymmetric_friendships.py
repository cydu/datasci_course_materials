import MapReduce
import sys

"""
The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. Implement a MapReduce algorithm to check whether this property holds. Generate a list of all non-symmetric friend relationships.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

from sets import Set

def mapper(record):
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person, (friend, 1))
    mr.emit_intermediate(friend, (person, 0))

def reducer(key, list_of_values):
    frieds_0 = [x for x, v in list_of_values if v == 0]
    frieds_1 = [x for x, v in list_of_values if v == 1]
    asym_friends = [x for x in frieds_1 if x not in frieds_0]
    asym_friends += [x for x in frieds_0 if x not in frieds_1]
    for person in Set(asym_friends):
        mr.emit((key, person))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
