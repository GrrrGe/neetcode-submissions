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
        
        if head1:
            dummy.next = head1
        
        if head2:
            dummy.next = head2

        return head.next


            
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists)> 1:
            mergedLists = []
            # for i in range(len(lists),2):
            #     print("i = "+ str(i))
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)< len(lists) else None
                mergedLists.append(self.merge2Lists(l1,l2))
            lists = mergedLists
        
        return lists[0]

        