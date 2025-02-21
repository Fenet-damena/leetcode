# Problem: Check if array is sorted - https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        l=0
        r=1
        while r<len(arr):
            if arr[l]>arr[r]:
                return False
            l+=1
            r+=1
        return True