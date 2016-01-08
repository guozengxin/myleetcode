# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = {}
        self.val = ''
        self.isLeaf = True


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
                newNode.val = c
                newNode.isLeaf = False
                node.nodes[c] = newNode
                node = newNode
        node.isLeaf = True


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


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("some")
print trie.search("some")