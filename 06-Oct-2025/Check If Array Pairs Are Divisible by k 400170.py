# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr, k):
        remfreq = {}

        for i in arr:
            remfreq[(i % k + k) % k] = (
                remfreq.get((i % k + k) % k, 0) + 1
            )

        for i in arr:
            rem = (i % k + k) % k

            if rem == 0:
                if remfreq[rem] % 2 == 1:
                    return False

            elif remfreq[rem] != remfreq.get(k - rem, 0):
                return False
        return True