# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0

        for i in range(len(nums)):
            curgcd = 0
            for j in range(i, len(nums)):
                curgcd =math.gcd(nums[j], curgcd)
                if curgcd == k:
                    ans += 1
                if curgcd < k:
                    break
        return ans

        