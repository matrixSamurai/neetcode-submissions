# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        if not list1:
            return list2
        
        if not list2:
            return list1
        
        newHead = None

        if list1.val > list2.val:
            newHead = list2
            list2 = list2.next
        else:
            newHead = list1
            list1 = list1.next
        
        currHead = newHead

        while list1 and list2:

            if list1.val > list2.val:
                currHead.next = list2
                currHead = list2
                list2 = list2.next
            else:
                currHead.next = list1
                currHead = list1
                list1 = list1.next
        
        # while list1:
        #     currHead.next = list1
        #     currHead = list1
        #     list1 = list1.next
        
        # while list2:
        #     currHead.next = list2
        #     currHead = list2
        #     list2 = list2.next

        currHead.next = list1 or list2
        
        
        return newHead
            
        