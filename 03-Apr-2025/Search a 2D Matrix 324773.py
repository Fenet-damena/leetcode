# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        t = c * r
        l , r = 0, t - 1

        while l <= r:
            m = (l+r)//2
            i = m // c
            j = m % c 
            if matrix[i][j] <  target:
                l = m + 1
            elif matrix[i][j] > target:
                r = m - 1
            else:
                return True    
        return False 