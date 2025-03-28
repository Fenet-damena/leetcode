# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def reptime(time):
            c = 0
            for i in ranks:
                c += int((time // i) ** 0.5)
                if c >= cars:
                    return True
            return False

        left, right = 1, min(ranks) * cars * cars
        while left < right:
            mid = (left + right) // 2
            if reptime(mid):
                right = mid
            else:
                left = mid + 1

        return left
        

    
    
