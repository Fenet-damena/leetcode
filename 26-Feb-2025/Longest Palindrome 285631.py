# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)

        ans = 0
        if len(c) == 1:
            return len(s)

        for k , v in c.items():
             ans +=(v//2 *2)


        if ans <len(s):
            return ans+1
        return ans
        