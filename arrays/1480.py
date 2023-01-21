'''
1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # base case 
        if len(nums) == 0:
            return []

        arr = []
        runningTotal = 0
        for num in nums:
            runningTotal += num
            arr.append(runningTotal)

        return arr