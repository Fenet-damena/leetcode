# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.n = None
        self.p = None

class LRUCache:
    def __init__(self, c: int):
        self.m = {}
        self.l, self.r = Node(0, 0), Node(0, 0)
        self.l.n = self.r
        self.r.p = self.l
        self.c = c

    def add_node(self, n):
        p, nx = self.l, self.l.n
        p.n = n
        nx.p = n
        n.n = nx
        n.p = p

    def remove_node(self, n):
        nx, p = n.n, n.p
        p.n = nx
        nx.p = p

    def get(self, k: int) -> int:
        if k in self.m:
            n = self.m[k]
            self.remove_node(n)
            self.add_node(n)
            return n.v
        else:
            return -1

    def put(self, k: int, v: int) -> None:
        if k in self.m:
            n = self.m[k]
            n.v = v
            self.remove_node(n)
            self.add_node(n)
        else:
            n = Node(k, v)
            if len(self.m) >= self.c:
                rm = self.r.p
                self.remove_node(rm)
                del self.m[rm.k]
            self.add_node(n)
            self.m[k] = n