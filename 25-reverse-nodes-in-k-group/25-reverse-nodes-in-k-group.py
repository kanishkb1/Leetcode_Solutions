# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        for _ in range(k):
            if not current:
                return head 
            
            current = current.next
            
        
        previous = None
        current = head
        for _ in range(k):
            next = current.next
            current.next = previous
            previous = current
            current = next
            
        head.next = self.reverseKGroup(current,k)
        return previous
    
    #TC: O(n)
    #SC: O(1)