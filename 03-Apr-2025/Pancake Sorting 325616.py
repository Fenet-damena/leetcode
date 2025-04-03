# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:  
        def flip(end):
            start = 0
            while start < end :
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        n = len(arr)
        ans = []
        for i in range(n-1, -1, -1):
            maxx = i
            for j in range(i , -1, -1):
                if arr[maxx] < arr[j]:
                    maxx = j
            if maxx != i:
                flip(maxx)
                flip(i)
                ans. append(maxx+1)
                ans.append (i+1)
        return ans 

            

            

                        



        