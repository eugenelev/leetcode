'''Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.'''


from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = len(arr) - 1
        while i >= 0:
            if arr[i] == 0:
                arr.insert(i+1, 0)
                arr.pop()
            i -= 1




# time = [1,0,2,3,0,4,5,0]
# # time = [1,2,3]
#
#
# i = len(time) - 1
# while i >= 0:
#     if time[i] == 0:
#         time.insert(i+1, 0)
#         time.pop()
#     i -= 1
#
#
# print(time)


# a = []
#
#
#
#
#
# i = 0
# count = 0
# while i < 3:
#     a.insert(count,i)
#     count += 1
#     i += 1
#
#
# b = len(a)
#
# a.insert(b, 10)
# print(a)
# x = len(a)
#
# a.insert(1,3)
# print(a) # return new list 'a'
# print(a.insert(0,3)) # return None







