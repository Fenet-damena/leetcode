# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = Counter(s)
        t_counter = Counter(t)

        for  k ,v in t_counter.items():
            if s_counter[k] < t_counter[k]:
                return k

        