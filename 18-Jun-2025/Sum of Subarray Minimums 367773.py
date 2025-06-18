# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        left = [0] * n  
        right = [0] * n  

        prev_less_elem = []  
        for i in range(n):
            while prev_less_elem and arr[prev_less_elem[-1]] >= arr[i]:
                prev_less_elem.pop()
            left[i] = i - prev_less_elem[-1] if prev_less_elem else i + 1
            prev_less_elem.append(i)

    
        next_less_elem = []  
        for i in range(n - 1, -1, -1):
            while next_less_elem and arr[next_less_elem[-1]] > arr[i]:
                next_less_elem.pop()
            right[i] = next_less_elem[-1] - i if next_less_elem else n - i
            next_less_elem.append(i)

        result = 0
        for i in range(n):
            result = (result + arr[i] * left[i] * right[i]) % MOD

        return result