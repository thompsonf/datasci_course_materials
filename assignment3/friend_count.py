import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person = record[0]
    friend_of_person = record[1]
    mr.emit_intermediate(person, friend_of_person)

def reducer(key, list_of_values):
    person = key
    num_friends = len(set(list_of_values))
    mr.emit((person, num_friends))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
