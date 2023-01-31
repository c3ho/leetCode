'''
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

'''
# Brute force would be to test all sub-combinations within a range
# Could we use a sliding window?

# I messed up and tried to start from the smallest window, but we should start with the biggest window and go down from there

# We're trying to find the max area that means we want to keep the taller value of the two points and move the smaller value pointer
# in this case, we increase the first pointer of the value of the first pointer is smaller than the second pointer, inversely if the second pointer is
# smaller than the first pointer, we decrease the second pointer


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # keep track of max
        max_area = 0
        p1 = 0
        p2 = len(height) - 1
        while p1 != p2:
            area = min(height[p1], height[p2]) * (p2 - p1)
            max_area = max(max_area, area)
            # if the height of the second pointer is bigger than the first one
            # we move the first pointer to the right since we want to keep the higher of the two values
            if height[p2] > height[p1]:
                p1 += 1
            # otherwise we decrease the second pointer since its a smaller value
            else:
                p2 -= 1
        return max_area
