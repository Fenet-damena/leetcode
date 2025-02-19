# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wl = 0
        for i in accounts:
            sums=sum(i)
            max_wl=max(max_wl,sums)
        return max_wl
        