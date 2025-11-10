# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = 10**15
        dist = [[INF]*n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = min(dist[u][v], w)
            dist[v][u] = min(dist[v][u], w)
        for k in range(n):
            dk = dist[k]
            for i in range(n):
                di = dist[i]
                ik = di[k]
                if ik == INF: 
                    continue
                for j in range(n):
                    nd = ik + dk[j]
                    if nd < di[j]:
                        di[j] = nd
        best_city = -1
        best_count = 10**18
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1
            if count < best_count or (count == best_count and i > best_city):
                best_count = count
                best_city = i
        return best_city
        