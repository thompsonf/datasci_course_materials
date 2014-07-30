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
    if person < friend_of_person:
      mr.emit_intermediate(person, friend_of_person)
    else:
      mr.emit_intermediate(friend_of_person, person)

def reducer(key, list_of_values):
    person = key
    asymmetric_friends = set()
    for f in list_of_values:
      if f not in asymmetric_friends:
        asymmetric_friends.add(f)
      else:
        asymmetric_friends.remove(f)
    
    for f in asymmetric_friends:
      mr.emit((person, f))
      mr.emit((f, person))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
