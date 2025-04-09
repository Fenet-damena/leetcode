# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts =[0] * (n+1)

        for i, j in trust:
            trusts[i] -=1
            trusts[j] +=1
        for p in range(1,n+1):
            if trusts[p] == n-1:
                return p
        return -1


        
        