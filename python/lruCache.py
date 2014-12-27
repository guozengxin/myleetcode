#!/usr/bin/env python
# https://oj.leetcode.com/problems/lru-cache/


class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addHead(self, node):
        if self.head is None:
            node.prev = None
            node.tail = None
            self.head = node
            self.tail = node
        else:
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def remove(self, node):
        if self.size == 1:
            self.head, self.tail = None, None
        elif node == self.head:
            node.next.prev = None
            self.head = self.head.next
        elif node == self.tail:
            node.prev.next = None
            self.tail = self.tail.prev
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
        self.size -= 1


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.allKey = {}
        self.cache = LinkedList()

    # @return an integer
    def get(self, key):
        if key in self.allKey:
            self.cache.remove(self.allKey[key])
            self.cache.addHead(self.allKey[key])
            return self.allKey[key].value
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.allKey:
            self.allKey[key].value = value
            self.cache.remove(self.allKey[key])
            self.cache.addHead(self.allKey[key])
        else:
            node = Node(key, value)
            self.allKey[key] = node
            self.cache.addHead(node)

        if self.cache.size > self.capacity:
            del self.allKey[self.cache.tail.key]
            self.cache.remove(self.cache.tail)

if __name__ == '__main__':
    lruc = LRUCache(3)
    lruc.set(5, 8)
    lruc.set(10, 7)
    print lruc.get(10)
    print lruc.get(7)
    print lruc.get(5)
    lruc.set(4, 6)
    lruc.set(8, 5)
    lruc.set(4, 10)
    print lruc.get(10)
