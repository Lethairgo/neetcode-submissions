"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2Copy = {None: None}

        current = head
        while current:
            copied = Node(current.val)
            old2Copy[current] = copied
            current = current.next
        
        current = head
        while current:
            copied = old2Copy[current]
            copied.next = old2Copy[current.next]
            copied.random = old2Copy[current.random]
            current = current.next
        return old2Copy[head]
        