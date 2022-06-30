# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        
        slow_pointer = head
        fast_pointer = head.next
        
        while fast_pointer!=None:
            if slow_pointer.val == fast_pointer.val:
                slow_pointer.next = fast_pointer.next
                fast_pointer = slow_pointer.next
                
            
            else:
                slow_pointer= slow_pointer.next
                fast_pointer = fast_pointer.next
        return head
        
        
        #Run-time complexity- O(N)
        #Space-time complexity- O(1)
                