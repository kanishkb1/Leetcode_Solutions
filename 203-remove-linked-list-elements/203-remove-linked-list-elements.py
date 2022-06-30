# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        previous_node = None
        current_node = head
        while current_node:
            if current_node.val == val:
                if previous_node:
                    previous_node.next = current_node.next
                    current_node = previous_node
                    
                else:
                    head=head.next
                    
            else:
                previous_node = current_node
            current_node = current_node.next
            
        return head
                
        