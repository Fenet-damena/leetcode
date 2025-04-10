# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for i, j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
        
        color = [-1] * (n+1)

        def dfs(node,c):
            color[node] = c

            for nei in graph[node]:
                if color[nei] == color[node]:
                    return False
                if color[nei] == -1 and not dfs(nei, 1-c):
                    return False
            return True
        
        for p in range(1,n+1):
            if color[p] == -1 and not dfs(p,0):
                return False
        return True