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
        old2Copy = defaultdict(lambda: Node(0))
        old2Copy[None] = None

        current = head
        while current:
            copied = old2Copy[current]
            copied.val = current.val
            copied.next = old2Copy[current.next]
            copied.random = old2Copy[current.random]
            current = current.next
        return old2Copy[head]
        