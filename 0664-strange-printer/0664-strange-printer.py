class Solution(object):
    def strangePrinter(self,s):
        n=len(s)
        if n==0:
            return 0
        memo={}
        def dp(i,j):
            if i>j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            result=dp(i,j-1)+1
        
            for k in range(i,j):
                if s[k]==s[j]:
                    result=min(result,dp(i,k)+dp(k+1,j-1))
            memo[(i,j)]=result
            return result
        return dp(0,n-1)