import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    order_id = key
    line_item_rows = []
    order_rows = []
    for row in list_of_values:
      if row[0] == "line_item":
        line_item_rows.append(row)
      else:
        order_rows.append(row)

    for ord_row in order_rows:
      for line_row in line_item_rows:
        mr.emit(ord_row + line_row)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
