class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        minimum=prices[0]
        profit=0
        
        for price in prices[1:]:
            cost=price-minimum
            if cost>profit:
                profit=cost
            if price<minimum:
                minimum=price
                
        return profit
    