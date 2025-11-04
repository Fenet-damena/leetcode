# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # DP array
        
        for i in range(n - 1, -1, -1):
            solve = questions[i][0] + (dp[i + questions[i][1] + 1] if i + questions[i][1] + 1 < n else 0)
            dp[i] = max(solve, dp[i + 1])
        
        return dp[0]
