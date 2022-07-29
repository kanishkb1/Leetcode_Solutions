# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        
        
        current = head
        previous = None
        
        while left > 1:
            previous = current
            current = current.next
            left = left - 1
            right = right - 1
            
        tail, connect = current,previous
        
        while right:
            third = current.next
            current.next = previous
            previous = current
            current = third
            right-=1
            
            
        if connect:
            connect.next = previous
            
            
        else:
            head = previous
        tail.next = current
        return head
        
       #Space complexity- O(1)
       #Time cpomplexity- O(n) 
            
        