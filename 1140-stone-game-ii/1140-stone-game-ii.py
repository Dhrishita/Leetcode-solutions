class Solution(object):
    def stoneGameII(self,piles):
        n=len(piles)
        sum=[0]*(n+1)
        
        for i in range(n - 1, -1, -1):
            sum[i]=sum[i+1]+piles[i]
    
        dp = {}
        def dfs(i,M):
            if i>=n:
                return 0
            if (i,M) in dp:
                return dp[(i,M)]
            max_stones=0
            for X in range(1,2*M+1):
                if i+X>n:
                    break
                max_stones=max(max_stones,sum[i]-dfs(i+X,max(M,X)))
            dp[(i,M)]=max_stones
            return max_stones
        return dfs(0, 1)
