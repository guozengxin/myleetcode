# https://leetcode.com/problems/game-of-life/

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        dx = (-1, -1, -1, 0, 1, 1, 1, 0)
        dy = (-1, 0, 1, 1, 1, 0, -1, -1)
        for x in xrange(len(board)):
            for y in xrange(len(board[0])):
                lives = 0
                for z in xrange(8):
                    lives += self.status(board, x+dx[z], y+dy[z])
                print lives
                if lives == 3 or board[x][y] + lives == 3:
                    board[x][y] |= 2
        for x in xrange(len(board)):
            for y in xrange(len(board[0])):
                board[x][y] >>= 1

    def status(self, board, x, y):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return 0
        return board[x][y] & 1

board = [
    [1, 1],
    [1, 0],
]

s = Solution()
s.gameOfLife(board)
print board
