'''
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

'''
# nothing special, runs in 0(n) / 2 = O(n)
# space is nothing extra since we're modifying in place

# Using two pointers we swap the letters and stop at the halfway point so they don't undo the switching we did


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        l = 0
        r = (len(s) - 1)
        while l < r:
            placeholder = s[l]
            s[l] = s[r]
            s[r] = placeholder
            l += 1
            r -= 1
