# https://leetcode.com/problems/word-search-ii/

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        for w in words:
            trie.insert(w)
        res = set()
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                visited = set()
                self.dfs(board, trie.root, i, j, visited, res)

        return list(res)

    def dfs(self, board, trieNode, i, j, visited, res):
        if (i, j) in visited:
            return
        if (i < 0 or j < 0 or i >= len(board) or j >= len(board[i])):
            return
        cur = board[i][j]
        if cur in trieNode.nodes:
            if trieNode.nodes[cur].isLeaf:
                res.add(trieNode.nodes[cur].word)
            visited.add((i, j))
            self.dfs(board, trieNode.nodes[cur], i+1, j, visited, res)
            self.dfs(board, trieNode.nodes[cur], i, j+1, visited, res)
            self.dfs(board, trieNode.nodes[cur], i-1, j, visited, res)
            self.dfs(board, trieNode.nodes[cur], i, j-1, visited, res)
            visited.remove((i, j))





class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = {}
        self.word = ''
        self.isLeaf = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c in node.nodes:
                node = node.nodes[c]
            else:
                newNode = TrieNode()
                node.nodes[c] = newNode
                node = newNode
        node.isLeaf = True
        node.word = word


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c in node.nodes:
                node = node.nodes[c]
            else:
                return False
        return node.isLeaf


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c in node.nodes:
                node = node.nodes[c]
            else:
                return False
        return True

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
s = Solution()
print s.findWords(board, words)