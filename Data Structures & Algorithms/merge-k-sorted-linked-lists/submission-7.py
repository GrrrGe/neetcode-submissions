# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge2Lists(self,l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1= l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
            
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        
        return curr.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        for r in range(1,len(lists)):
            lists[0]=self.merge2Lists(lists[0],lists[r])
            r+=1
        return lists[0]
        
        