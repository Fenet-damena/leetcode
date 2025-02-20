# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        sets = set()
        while n != 1:
            if n in sets:
                return False
            sets.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return True
        