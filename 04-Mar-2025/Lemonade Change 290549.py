# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for i in range(len(bills)):
            if bills[i] == 5:
                five +=1
            elif bills[i] == 10:
                if five > 0:
                    five -=1
                    ten +=1
                else:
                    return False
            else:
                if ten > 0:
                    ten -=1
                    if five > 0:
                        five -=1
                    else:
                        return False
                elif five > 2:
                    five -= 3
                else:
                    return False
        return True
        