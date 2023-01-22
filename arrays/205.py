'''
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # base case
        if len(s) == 0:
            return True

        myDict1 = dict()
        myDict2 = dict()
        # create dictionary to map letters of s to t, we also need a second dictionary to map reverse
        # to check for doubles
        for index, letter in enumerate(s):
            myDict1[letter] = t[index]
            myDict2[t[index]] = letter

        for index, letter in enumerate(s):
            if myDict1[letter] != t[index] or myDict2[t[index]] != letter:
                return False

        return True
