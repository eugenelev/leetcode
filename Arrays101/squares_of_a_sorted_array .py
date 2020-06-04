'''
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number,
also in sorted non-decreasing order.
'''


from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i, num in enumerate(A, 0):
            A[i] = num * num
        return sorted(A)

s = Solution()

print(s.sortedSquares([-4,-1,0,3,10]))