# Given a fixed length array arr of integers,
# duplicate each occurrence of zero,
# shifting the remaining elements to the right.
#
# Note that elements beyond the length of the original array are not written.
#
# Do the above modifications to the input array in place, do not return anything from your function.
#
#
#
# Example 1:
#
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
# Example 2:
#
# Input: [1,2,3]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,2,3]
#
#
# Note:
#
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9


from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        possible_dups = 0
        length_ = len(arr) - 1

        # Find the number of zeros to be duplicated
        for i in range(len(arr)):

            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if i > length_ - possible_dups:
                break

            # Count the zeros
            if arr[i] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included
                if i == length_ - possible_dups:
                    arr[length_] = 0  # For this zero we just copy it without duplication.
                    length_ -= 1
                    break
                possible_dups += 1

        # Start backwards from the last element which would be part of new list.
        last = length_ - possible_dups

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]


if __name__ == '__main__':
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    # arr = [8, 4, 5, 0, 0, 0, 0, 7]
    sol = Solution()
    sol.duplicateZeros(arr)
    print(arr)
