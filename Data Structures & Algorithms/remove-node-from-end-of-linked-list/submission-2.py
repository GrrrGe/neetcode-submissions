# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length = 0
        while temp:
            length+=1
            temp = temp.next # O(n)
        new_n = length - n
        if new_n == 0:
            return head.next
        temp = head
        prev = head
        while new_n > 0:
            prev = temp
            temp = temp.next #O(n)
            new_n -=1
        prev.next = temp.next
        return head