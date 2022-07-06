# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #take two pointers
        fast = head
        slow = head
        
        #Move the fast pointer at n-th position
        for k in range(n):
            fast = fast.next
         
        #If we have to remove first element   
        if fast == None:
            return head.next
        
        #Deletion of node at n-th node from end
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
        
        
        