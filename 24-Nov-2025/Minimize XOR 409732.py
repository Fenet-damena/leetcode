# Problem: Minimize XOR - https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        target = bin(num2).count("1")
        x = num1
        cur = bin(x).count("1")

        i = 0
        while cur > target:
            if (x >> i) & 1:
                x &= ~(1 << i)   
                cur -= 1
            i += 1

        i = 0
        while cur < target:
            if ((x >> i) & 1) == 0:
                x |= (1 << i)   
                cur += 1
            i += 1

        return x
        