class Solution(object):
    def missingRolls(self, rolls, mean, n):
        m=len(rolls)
        sum_of_nm=mean*(n+m)  
        sum_of_rolls=sum(rolls)    
        
        missing_sum=sum_of_nm-sum_of_rolls
        if missing_sum<n or missing_sum>6*n:
            return []  
        dhrishita=[1]*n 
        missing_sum-=n  
        for i in range(n):
            if missing_sum==0:
                break
            add=min(5,missing_sum)  
            dhrishita[i]+=add
            missing_sum-=add
        return dhrishita