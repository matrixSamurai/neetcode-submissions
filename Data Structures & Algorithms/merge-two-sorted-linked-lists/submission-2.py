# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        


        if list1.val <= list2.val:
            newHead = list1
            list1 = list1.next
        else:
            newHead = list2
            list2 = list2.next
        
        returnHead = newHead
        
    
        while list1 != None and list2 != None:

            if list1.val <= list2.val:
                newHead.next = list1
                newHead = list1
                list1 = list1.next
            else:
                newHead.next = list2
                newHead = list2
                list2 = list2.next

        if list1 != None:
            newHead.next = list1

        if list2 != None:
            newHead.next = list2

        return returnHead


        