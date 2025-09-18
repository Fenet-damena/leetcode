# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

import numpy as np
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
     ans =[[0]* len(img[0]) for _ in range(len(img))]

     for r in range (len(img)):
        for c in range (len(img[0])):
            sum = img[r][c]
            n = 1
            if r-1 >= 0:
                sum += img[r-1][c]
                n +=1
            if r+1 < (len(img)):
                sum += img[r+1][c]
                n +=1
            if  c-1 >=0:
                sum += img[r][c-1]
                n +=1
            if c+1 < len(img[0]):
                sum += img[r][c+1]
                n +=1
            if r+1 < len(img) and  c+1 < len(img[0]):
                sum += img[r+1][c+1]
                n +=1
            if r-1 >=0 and c-1 >=0:
                    sum += img[r-1][c-1]
                    n +=1
           
            if c+1 < len(img[0]) and r-1 >=0:
                sum += img[r-1][c+1]
                n +=1
            if c-1 >=0 and r+1 < len(img):
                sum += img[r+1][c-1]
                n +=1
            avg = sum // n
            ans[r][c] = avg
     return ans


            


