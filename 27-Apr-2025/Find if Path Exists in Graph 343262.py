# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = defaultdict(list)

        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()
        seen.add(source)

        def dfs(i):
            if i == destination:
                return True
            for nie in graph[i]:
                if nie not in seen:
                    seen.add(nie)
                    if dfs(nie):
                      return True
            return False
        return dfs(source)
        