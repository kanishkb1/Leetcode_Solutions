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
            
        prev = None
            
        while slow_pointer:
            temp = slow_pointer.next
            slow_pointer.next=prev
            prev = slow_pointer
            slow_pointer = temp 
                
        while prev:
            if prev.val!= head.val:
                return False
                
            prev = prev.next
            head=head.next
                
        return True
    
    #Time complexity- O(1)
    #Space complexity- O(N)
        
        
            