# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = []
        zeros = []
        
        for char in s:
            if char == '0':
                zeros.append(char)
            else:
                ones.append(char)
        
        if len(ones) > 1:
            ans = ones[:-1] + zeros + [ones[-1]] 
            return "".join(ans) 
        
        ans = zeros + ones 
        return "".join(ans) 
