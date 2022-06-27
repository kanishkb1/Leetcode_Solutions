# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #declaration of two pointers
        slow_pointer = head
        fast_pointer = head
        
        while fast_pointer is not None and fast_pointer.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            
            if slow_pointer==fast_pointer:
                return True
            
        return False
    
    #Time complexity- O(N)
    #Space complexiuty- O(1) as no extra space is used. 