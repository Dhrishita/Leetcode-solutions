# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class Solution(object):
    def spiralMatrix(self, m, n, head):
        matrix=[[-1 for _ in range(n)] for _ in range(m)]
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        direction_index=0
        r, c = 0, 0  
        current=head
        
        for _ in range(m*n):
            if current:
                matrix[r][c]=current.val
                current=current.next
            else:
                matrix[r][c]=-1 
            next_r,next_c=r+directions[direction_index][0], c+directions[direction_index][1]
            if not (0<=next_r<m and 0<=next_c<n and matrix[next_r][next_c]==-1):
                direction_index=(direction_index+1)%4
                next_r,next_c=r+directions[direction_index][0], c+directions[direction_index][1]
            r,c=next_r,next_c
        return matrix