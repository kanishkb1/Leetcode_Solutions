# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        #Calculate the length of the list and last node in the list
        length  = 1
        tail = head
        
        #count of number of nodes
        while tail.next:
            tail=tail.next
            length+=1
            
        #Calculate the length of the node    
        k = k % length
        if k==0:
            return head
        
        current = head
        
        #get the nodes before we have made the cut (we have to rotate)
        for i in range(length - k -1):
             current = current.next
    
        newHead = current.next
        #connect the new node with the tail pointer (where we have cutted the Kth node to end)
        current.next = None
        
        
        tail.next=head
        return newHead
        
        #Time complexity- O(N)
        #SC:O(1)
            
    