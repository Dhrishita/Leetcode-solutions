class Solution(object):
    def check(self, nums):
        d=0
        m=len(nums)
        for i in range(m):
            if nums[i]>nums[(i+1)%m]:
                d+=1
            if d>1:  
                return False
        return True