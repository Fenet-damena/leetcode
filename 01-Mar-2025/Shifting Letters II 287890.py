# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        length = len(s)
        shift_values = [0] * length

        for start_idx, end_idx, direction in shifts:
            if direction == 1:
                shift_values[start_idx] += 1
                if end_idx + 1 < length:
                    shift_values[end_idx + 1] -= 1
            else:
                shift_values[start_idx] -= 1
                if end_idx + 1 < length:
                    shift_values[end_idx + 1] += 1
        
        for index in range(1, length):
            shift_values[index] += shift_values[index - 1]

        shifted_string = []
        for index in range(len(s)):
            new_char_val = (ord(s[index]) - ord('a') + shift_values[index]) % 26
            shifted_string.append(chr(new_char_val + ord('a')))
        
        return "".join(shifted_string)
