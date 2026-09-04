# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        map1 = {}

        while head != None:

            if head in map1:
                return True
            
            map1[head] = 1
            
            head = head.next
        
        return False