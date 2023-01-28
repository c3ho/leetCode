'''
Given a string s, find the length of the longest substring without repeating characters.


'''
# We have an array storing elements we traverse, for every char we append, we check if the char exists already, if it does,
# get a substring of the element following the first occurrence of the duplicate char
#
# This method is easier, however slower since we traverse the array, to see if there's a duplicate
#
# This can probably be sped up with a dictionary instead where retrieval is in 0(1) time and we won't constantly traverse the array
# to find a duplicate


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = []
        max_length = 0

        for letter in s:
            if letter in arr:
                arr = arr[arr.index(letter) + 1:]

            arr.append(letter)

            if len(arr) > max_length:
                max_length = len(arr)

        return max_length
