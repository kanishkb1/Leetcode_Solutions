# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        if not head:
            return head
        
        first = head
        second = head.next
        
        while first and second:
            first.val,second.val = second.val,first.val
            
            first = second.next
            if not first:
                break
                
            second = second.next.next
        return head
            
        
        #Run time complexity-O(n)
        #Space-O(1)
        
        
        