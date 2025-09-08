# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        for i in range(len(strs[0])):
            for j in strs:
                if  len(j) == i or j[i] !=  strs[0][i]:
                    return ans
            ans += strs[0][i]
        return ans