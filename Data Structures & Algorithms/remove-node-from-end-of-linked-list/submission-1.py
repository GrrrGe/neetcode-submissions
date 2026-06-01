# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head
        prev = head
        while n > 0 and second:
            n-=1
            second = second.next
        
        if not second:
            return head.next
        

        while second:
            second = second.next
            prev = first
            first = first.next
        
        prev.next = first.next

        
        return head

