# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #
        tail = dummy
        
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                
            else:
                tail.next=list2
                list2=list2.next
            tail = tail.next
            
        
        #taking remaining portion of list for list l1 and l2 respectively.
        if list1: #if the list is non-empty, get the entire sorted portion of list
            tail.next=list1
        elif list2:
            tail.next=list2
        return dummy.next
    
    #Space Complexity- O(1) as no extra space is used.
    #Time complexity- O(M+N)