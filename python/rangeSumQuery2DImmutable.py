# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        self.sums = []
        for row in matrix:
            rowLen = len(row)
            rowSums = [0] * rowLen
            rowSums[0] = row[0]
            for i in xrange(1, rowLen):
                rowSums[i] = rowSums[i-1] + row[i]
            self.sums.append(rowSums)



    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = 0
        for r in xrange(row1, row2 + 1):
            if col1 == 0:
                sum += self.sums[r][col2]
            else:
                sum += self.sums[r][col2] - self.sums[r][col1-1]
        return sum


matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
# Your NumMatrix object will be instantiated and called as such:
numMatrix = NumMatrix(matrix)
print numMatrix.sumRegion(0, 1, 2, 3)
print numMatrix.sumRegion(1, 2, 3, 4)