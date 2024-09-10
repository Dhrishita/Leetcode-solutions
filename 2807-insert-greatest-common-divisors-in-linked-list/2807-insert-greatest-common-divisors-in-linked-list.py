# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution(object):
     def gcd(self,d,m):
        while m:
            d,m=m,d%m
        return d
     def insertGreatestCommonDivisors(self, head):
            current=head
            while current and current.next:
                gcd_value=self.gcd(current.val,current.next.val)
                new_node = ListNode(gcd_value)
                new_node.next=current.next
                current.next=new_node
                current=new_node.next
            return head