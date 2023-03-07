'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

# We can brute force this by going over n elements and computing it against n - 1 to see if it exists
# In this case we can use a dictionary and see if it exists


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for idx, num in enumerate(nums):
            # what number are we looking for
            num_to_find = target - num

            # is the number we're looking for in the dictionary?
            if num_to_find in my_dict.keys():
                # return the current index and index of the other number
                return [idx, my_dict[num_to_find]]

            # store the number as a key and the index as the value
            my_dict[num] = idx
