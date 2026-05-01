# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = 0
        count = 0

        while l1 or l2:
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            val *= 10 ** count
            result += val
            count += 1

        if result == 0:
            return ListNode(0)

        dummy = ListNode(0)
        cur = dummy

        while result > 0:
            digit = result % 10
            cur.next = ListNode(digit)
            cur = cur.next
            result //= 10

        return dummy.next