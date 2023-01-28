'''
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

'''

# I'm not going to be a smart ass and try to figure this out with bitewise operators and do it through the method I do know
# which is by using a dictionary

# Time complexity = O(N) - we iterate through the whole list of nums
# Space complexity = 0(N) - we need a dictionary to store all the numbers


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dict = {}

        for i in nums:
            # if entry doesn't exist in dictionary, initialize with key with the number and value with count of 1
            if i not in my_dict:
                my_dict[i] = 1
            # if it does exist just increase the count
            else:
                my_dict[i] = my_dict[i] + 1

        # iterate through dictionary to find the key with a value of 1 and return it
        for i in my_dict:
            if my_dict[i] == 1:
                return i
