# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:
    def __init__(self):
        self.pref = [1]
    def add(self, num: int) -> None:
        if num == 0:
            self.pref = [1]

        else:
            self.pref.append(self.pref[-1] * num)

    def getProduct(self, k: int) -> int:
        if len(self.pref) <= k:
            return 0 
        return self.pref[-1] // self.pref[-k - 1]  