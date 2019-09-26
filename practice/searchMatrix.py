# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

#[
#  [1, 3,  4, 11, 15],
#  [2,  5,  8, 12, 19],
#  [3,   6,  9, 16, 22],
#  [10, 13, 14, 17, 24],
#  [18, 21, 23, 26, 30]
#]
#Given target = 5, return true.

#Given target = 20, return false.

def searchMatrix(matrix, target):
  row, col = 0, len(matrix)-1
  while row < len(matrix) and col > 0:
    if matrix[row][col] > target:
      col -= 1
    elif matrix[row][col] < target:
      row += 1
    else:
      return True
  return False

matrix = [
  [1, 3,  4, 11, 15],
  [2,  5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print (searchMatrix(matrix, 21))
