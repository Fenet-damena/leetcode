# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        perfix_sum = 0
        res = 0
        perfix_c = defaultdict(int)
        perfix_c[0] = 1

        for n in nums:
            perfix_sum += n
            rem = perfix_sum % k
            if rem in perfix_c:
                res += perfix_c[rem]
            perfix_c[rem] += 1
        return res


      

        