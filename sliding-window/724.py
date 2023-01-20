'''
https://leetcode.com/problems/find-pivot-index/solutions/?envType=study-plan&id=level-1&languageTags=python3

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
'''

# This solution is slower because we'll always compute the sum, the pivot doesn't go towards the sum of either left side or right side


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for index, val in enumerate(nums):
            if sum(nums[0:index]) == sum(nums[index+1:len(nums)]):
                return index
        return -1

# This solution is faster because its a simple subtraction and we don't recalculate the sum on the whole array ever iteration
    def pivotIndex(self, nums: List[int]) -> int:
        lsum, rsum = 0, sum(nums)
        for index, val in enumerate(nums):
            # This fixes the issue with the pivot by putting it before comparing it with the right side
            rsum -= val
            if lsum == rsum:
                return index
            lsum += val
        return -1


nums = [1, 7, 3, 6, 5, 6]
nums2 = [2, 1, -1]

print(Solution.pivotIndex(nums2))
