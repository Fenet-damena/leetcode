# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.s = 0

class MapSum:

    def __init__(self):
        self.r = TrieNode()
        self.m = {}

    def insert(self, k: str, v: int) -> None:
        d = v - self.m.get(k, 0)
        self.m[k] = v
        
        c = self.r
        for char in k:
            if char not in c.children:
                c.children[char] = TrieNode()
            c = c.children[char]
            c.s += d

    def sum(self, p: str) -> int:
        c = self.r
        for char in p:
            if char not in c.children:
                return 0
            c = c.children[char]
        return c.s

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

