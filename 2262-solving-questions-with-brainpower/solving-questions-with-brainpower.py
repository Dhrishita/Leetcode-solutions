class Solution(object):
    def mostPoints(self,questions):
        n=len(questions)  
        dp_next=0 
        dp=[0]*(n+1)  

        for i in range(n-1,-1,-1): 
            points,brainpower=questions[i]  
            next_q=i+brainpower+1 
            solve=points+(dp[next_q] if next_q<n else 0)
            dp[i]=max(solve,dp_next)
            dp_next=dp[i]
        return dp[0]    