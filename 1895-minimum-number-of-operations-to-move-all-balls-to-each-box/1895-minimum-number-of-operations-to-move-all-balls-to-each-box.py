class Solution(object):
    def minOperations(self, boxes):
        n = len(boxes)
        d = [0] * n
        moves = 0  
        balls = 0  
        for i in range(1, n):
            if boxes[i-1] == '1':
                balls += 1
            moves += balls
            d[i] += moves
        moves = 0  
        balls = 0 
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1':
                balls += 1
            moves += balls
            d[i] += moves  
        return d
