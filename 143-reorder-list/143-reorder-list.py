# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
           
        slow_pointer,fast_pointer = head,head
        
        while fast_pointer and fast_pointer.next:
            slow_pointer, fast_pointer = slow_pointer.next, fast_pointer.next.next
        mid = slow_pointer


        previous_pointer,current_pointer = None,mid
        
        while current_pointer:
            current_pointer.next,previous_pointer,current_pointer = previous_pointer,current_pointer,current_pointer.next   
        head_of_second_rev = previous_pointer
        
    
        first,second = head,head_of_second_rev
         
        
        while second.next:
            
            next_hop = first.next
            first.next = second
            first = next_hop
            
            
            next_hop = second.next
            second.next = first
            second = next_hop
            
            #Time complexity- O(n)
            #Space Complexity- O(1) as no extra space is used.      
        
        
        
        
        