# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, n: List[int], r: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        p_sum = [0] * (len(n) + 1)
        for s, e in r:
            p_sum[s] += 1
            p_sum[e + 1] -= 1
        
        for i in range(len(n)):
            p_sum[i + 1] += p_sum[i]

        p_sum.sort(reverse=True)
        n.sort(reverse=True)
        
        total = 0
        for num, pre in zip(n, p_sum):
            total += (num * pre)

        return total % mod