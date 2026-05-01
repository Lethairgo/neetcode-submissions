# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        prev = slow.next = None

        while head2:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp

        # now head1 -> beginning of first half, prev -> begining of second half
        head2 = prev
        while head2:
            temp1, temp2 = head.next, head2.next
            head.next = head2
            head2.next = temp1
            head, head2 = temp1, temp2
        
        
        