import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""
a_rows = 5
a_cols = 5
b_rows = 5
b_cols = 5

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    matrix, i, j, value = record
    if matrix == "a":
      for col in range(b_cols):
        mr.emit_intermediate((i, col), (matrix, j, value))
    else: #matrix == "b"
      for row in range(a_rows):
        mr.emit_intermediate((row, j), (matrix, i, value))

def reducer(key, list_of_values):
    prod_row, prod_col = key
    a_row = [0] * a_cols
    b_col = [0] * b_rows
    for matrix, idx, value in list_of_values:
      if matrix == "a":
        a_row[idx] = value
      else:
        b_col[idx] = value

    final_val = sum(a_val * b_val for (a_val, b_val) in zip(a_row, b_col))
    mr.emit((prod_row, prod_col, final_val))
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
