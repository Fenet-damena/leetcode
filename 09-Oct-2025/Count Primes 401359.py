# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0

        prime = [True] * n
        prime[0] = False
        prime[1] = False

        d = 2

        while d*d <= n:
            if prime[d]:
                for i in range(d*d, n, d):
                    prime[i] = False
            d += 1
        ans = 0

        for i in prime:
            if i :
                ans += 1
        return ans
 

