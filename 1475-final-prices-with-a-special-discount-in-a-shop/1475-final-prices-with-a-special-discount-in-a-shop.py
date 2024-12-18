class Solution(object):
    def finalPrices(self, prices):
        d=len(prices)
        ans=prices[:]
        for i in range(d):
            for j in range(i+1,d):
                if prices[i]>=prices[j]:
                    ans[i]-=prices[j]
                    break
        return ans
        
        