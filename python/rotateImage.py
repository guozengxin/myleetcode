# https://leetcode.com/problems/rotate-image/

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for i in xrange(0, size/2):
            for j in xrange(i, size-1-i):
                t = matrix[i][j]
                matrix[i][j] = matrix[size-j-1][i]
                matrix[size-j-1][i] = matrix[size-i-1][size-j-1]
                matrix[size-i-1][size-j-1] = matrix[j][size-i-1]
                matrix[j][size-i-1]= t


matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
s = Solution()
s.rotate(matrix)
print matrix

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
s.rotate(matrix)
print matrix
