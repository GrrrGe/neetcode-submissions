# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge2Lists(self, head1: ListNode, head2:ListNode) -> ListNode:
        dummy = ListNode(float('-inf'), None)
        head = dummy
        while head1 and head2:
            # print("head1.val:"+ str(head1.val))
            # print("head2.val:"+str(head2.val))
            if head1.val < head2.val:
                dummy.next = head1
                head1 = head1.next
            else:
                dummy.next = head2
                head2 = head2.next
            dummy = dummy.next
        
        while head1:
            dummy.next = head1
            head1 = head1.next
            dummy = dummy.next
        
        while head2:
            dummy.next = head2
            head2 = head2.next
            dummy = dummy.next

        return head.next


            
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(float('-inf'), None)
        head = dummy
        for l in lists:
            dummy = self.merge2Lists(dummy, l)
        
        return head.next

        