# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sortedList = None

        if list1 and list2:
            if list1.val < list2.val:
                sortedList = list1
                list1 = list1.next
            else:
                sortedList = list2
                list2 = list2.next
        else:
            if list1:
                sortedList = list1
                list1 = list1.next
            elif list2:
                sortedList = list2
                list2 = list2.next
            else:
                return None

        listHead = sortedList

        while list1 and list2:
            if list1.val < list2.val:
                sortedList.next = list1
                list1 = list1.next
            else:
                sortedList.next = list2
                list2 = list2.next
            sortedList = sortedList.next
        
        if list1:
            sortedList.next = list1
        elif list2:
            sortedList.next = list2
        
        return listHead

