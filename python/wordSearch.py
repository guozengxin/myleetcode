#!/usr/bin/env python
# https://oj.leetcode.com/problems/word-search/


class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        self.boardh = len(board)
        self.boardw = len(board[0])
        for i in range(self.boardh):
            for j in range(self.boardw):
                if board[i][j] == word[0]:
                    t, board[i][j] = board[i][j], '#'
                    if self.dfs(board, word, i, j, 1):
                        return True
                    board[i][j] = t
        return False

    def dfs(self, board, word, x, y, index):
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        if index == len(word):
            return True
        for i in range(4):
            nextx, nexty = x + dx[i], y + dy[i]
            if nextx >= 0 and nextx < self.boardh and nexty >= 0 and nexty < self.boardw and board[nextx][nexty] == word[index]:
                t, board[nextx][nexty] = board[nextx][nexty], '#'
                if self.dfs(board, word, nextx, nexty, index + 1):
                    return True
                board[nextx][nexty] = t
        return False

if __name__ == '__main__':
    import copy
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E'],
    ]
    print Solution().exist(copy.deepcopy(board), 'ABCCED')
    print Solution().exist(copy.deepcopy(board), 'SEE')
    print Solution().exist(copy.deepcopy(board), 'ABCB')
