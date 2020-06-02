from typing import List

# Given an array nums of integers, return how many of them contain an even number of digits.

# class Solution:
#     def findNumbers(self) -> int:
#         return 2
#
# a = Solution()
#
# print(a.findNumbers())


# dvd = []
# #
# # dvd[0] = "22"
# # dvd.append(2)
#
#
# # print(len(dvd))
# for i in range(11-1):
#     b = (i+1) * (i+1)
#     dvd.append(b)
#
# print(*dvd)
# # print(*dvd, sep = ", ")
# # print(*dvd, sep = "\n")
#
# for i in range(len(dvd)):
#     print(i)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxvalue = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if maxvalue < count:
                    maxvalue = count
            else:
                count = 0
        return maxvalue



a = Solution()
print(a.findMaxConsecutiveOnes([1,0,0,0,1,1,1,1,0,1,1,1,0]))










