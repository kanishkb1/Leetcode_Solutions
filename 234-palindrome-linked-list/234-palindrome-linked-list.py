# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast_pointer = head
        slow_pointer = head
        
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            
        node = None
            
        while slow_pointer:
            nxt = slow_pointer.next
            slow_pointer.next=node
            node = slow_pointer
            slow_pointer = nxt
                
        while node:
            if node.val!= head.val:
                return False
                
            node = node.next
            head=head.next
                
        return True
        
        
            