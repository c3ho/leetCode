'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

# Time complexity O(N), potentially go through the whole string
# Space complexity O(N), we'll need a list big enough to store the whole string


class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s)) % 2 == 1:
            return False
        stack = []
        # define dictionary for lookup, this will avoid us having to code multiple if statements to correct closing character
        my_dict = {'{': '}', '(': ')', '[': ']'}
        for l in s:
            # if the character is one of the open characters, append
            if l in my_dict:
                stack.append(l)

            # if its a closing character check it against the most recent character in the list, we'll also check if the list
            # is empty cause that means there's no matching character
            elif len(stack) == 0 or my_dict[stack.pop()] != l:
                return False

        # if all characters are matched, then list should be empty since all chars are popped
        return len(stack) == 0
