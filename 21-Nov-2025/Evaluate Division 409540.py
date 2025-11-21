# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)
        
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1/val))
        
        def dfs(start, end, visited):
            if start not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            visited.add(start)
            for neighbor, value in graph[start]:
                if neighbor in visited:
                    continue
                product = dfs(neighbor, end, visited)
                if product != -1.0:
                    return value * product
            return -1.0
        
        result = []
        for c, d in queries:
            result.append(dfs(c, d, set()))
        
        return result

        