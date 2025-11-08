# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        g=[[] for _ in range(n)]
        for (u,v),p in zip(edges, succProb):
            g[u].append((v,p))
            g[v].append((u,p))
        pq=[(-1.0,start_node)]
        best=[0.0]*n
        best[start_node]=1.0
        while pq:
            p,u = heapq.heappop(pq)
            p=-p
            if u==end_node: return p
            for v,pr in g[u]:
                np=p*pr
                if np>best[v]:
                    best[v]=np
                    heapq.heappush(pq,(-np,v))
        return 0.0

        