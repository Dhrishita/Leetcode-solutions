# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class Solution(object):
    def splitListToParts(self, head, k):
        n=0
        current=head
        while current:
            n+=1
            current=current.next
        
        part_size=n//k  
        extra_nodes=n%k  
        dhrishita=[]
        current=head
        
        for i in range(k):
            part_head=current  
            part_current_size=part_size+(1 if i<extra_nodes else 0)  
            for j in range(part_current_size-1):
                if current:
                    current=current.next
    
            if current:
                next_part_head=current.next
                current.next=None
                current=next_part_head
            dhrishita.append(part_head)
        return dhrishita