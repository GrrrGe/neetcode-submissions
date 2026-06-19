# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupPrev = dummy

        while True:
            kthNode = self.getKthNode(groupPrev,k)
            
            if not kthNode:
                return dummy.next

            print("kth node:")
            print(kthNode.val)

            groupNext = kthNode.next
            # print("groupNext:")
            # print(groupNext.val)
            prev = groupNext
            curr = groupPrev.next
            while curr!=groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            tmp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = tmp
            print("groupPrev")
            print(groupPrev.val)
    
    def getKthNode(self,node,k):
        while node and k:
            node = node.next
            k-=1
        return node