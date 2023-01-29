'''
138. Copy List with Random Pointer


A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# We'll store the node info in a dictionary
# Time complexity is O(N), we do iterate through the linked list twice so technically its O(2N) which simplifies to O(N)
# Space complexity is O(N) as we'll need a dictionary of N nodes


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        my_dict = {}
        curr = head
        while curr:
            # Create the dictionary, use the original nodes as keys and values as the new nodes
            my_dict[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        # map the random value to the node
        while curr:
            # Assign the next based on the OG array
            if curr.next:
                my_dict[curr].next = my_dict[curr.next]
            # Since the original nodes are used as keys, we use the node.random value as the key to see which node it points to.
            # node.random must exist as another key + value in the dictionary, hence we can use my_dict[curr.random] to get the
            # supposed random node and assign it to the new Node's random
            if curr.random:
                my_dict[curr].random = my_dict[curr.random]
            curr = curr.next

        return my_dict[head]
