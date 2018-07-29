# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """ 
        tmp=head
        prev=None
        while tmp and tmp.next:
            if tmp.val==tmp.next.val:
                while tmp.next and tmp.val == tmp.next.val:                    
                    tmp=tmp.next
                if prev:
                    prev.next = tmp.next   
                else:
                    head=tmp.next
            else:                
                prev=tmp
                
            tmp=tmp.next
        return head
                    
                    
                    
                
        

                
    
