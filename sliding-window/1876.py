"""
https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/

1876:
A string is good if there are no repeated characters.

Given a string s, return the number of good substrings of length three in s.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

- 1 <= s.length <= 100
- s consists of lowercase English letters.
"""

# We can use a sliding window and shift it by 1, while in the loop, we'll also have to identify if the 3 letter
# substring is distinct. In this case we can use a SET as sets don't allow duplicates, we insert the letters as values
# into the set and if there are less than 3 items in the set it is not distinct because it contains duplicates


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        counter = 0
        for index, val in enumerate(s):
            # stop condition for loop
            if index + 3 > len(s):
                break
            word = s[index:index + 3]
            # create a set from the three letters
            mySet = set(list(word))

            # get length of the set, if there are no duplicates, it should return 3
            # if there are 1 or 2 dupes, it'll not be 3
            if (len(mySet)) == 3:
                counter = counter + 1
        return counter
