# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        tempHead = head
        listLen = 0

        # Finding the length of the linkedList
        while tempHead:
            tempHead = tempHead.next
            listLen += 1

        segments = listLen // k

        # Setting the temp again for traversing
        curr = head
        previousGroupTail = None
        globalHead = None

        for i in range(0, segments):
            prev = None
            count = k

            listPrev = None

            while count > 0:
                if count == k:
                    listPrev = curr

                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

                count -= 1
            
            if i == 0:
                globalHead = prev
            
            if previousGroupTail != None:
                previousGroupTail.next = prev
            
            previousGroupTail = listPrev

              # attach remaining nodes
            if previousGroupTail:
                previousGroupTail.next = curr
        
        return globalHead

            



                
            
            

        