# Problem: Smallest Even Multiple - https://leetcode.com/problems/smallest-even-multiple/

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
       
        i=1
        while True:
            if i%2==0 and i%n==0:
                return i
            i+=1
        