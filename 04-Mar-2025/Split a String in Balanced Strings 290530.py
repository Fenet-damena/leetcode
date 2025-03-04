# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        c = Counter()

        for i in range(len(s)):
            c[s[i]] += 1
            if c["R"] == c["L"]:
                ans +=1
                c.clear()
        return ans
        