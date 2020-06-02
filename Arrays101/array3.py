from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i, num in enumerate(A, 0):
            A[i] = num * num
        return sorted(A)

s = Solution()

print(s.sortedSquares([-4, -5, 2, 3, 10]))