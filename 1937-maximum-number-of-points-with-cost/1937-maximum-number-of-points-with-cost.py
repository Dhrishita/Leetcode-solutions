class Solution(object):
    def maxPoints(self, points):
        if not points or not points[0]:
            return 0

        m=len(points)  
        d=len(points[0])  
        dp=points[0][:]
        
        for i in range(1, m):
            max_from_left=[0]*d
            max_from_right=[0]*d
            max_from_left[0]=dp[0]
            for j in range(1,d):
                max_from_left[j]=max(max_from_left[j-1],dp[j]+j)
            max_from_right[d-1]=dp[d-1]-(d-1)
            for j in range(d-2,-1,-1):
                max_from_right[j]=max(max_from_right[j+1],dp[j]-j)
            new_dp=[0]*d
            for j in range(d):
                new_dp[j]=points[i][j]+max(max_from_left[j]-j,max_from_right[j]+j)
            dp=new_dp
        return max(dp)