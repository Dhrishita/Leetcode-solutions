class Solution(object):
    def twoSum(self, nums, target):
        nums_sorted = [(nums[i], i) for i in range(len(nums))]
        nums_sorted.sort()
        left,right=0,len(nums)-1
        
        while left<right:
            twoSum=nums_sorted[left][0]+nums_sorted[right][0]
            if twoSum==target:
                return [nums_sorted[left][1],nums_sorted[right][1]]
            elif twoSum<target:
                left+=1
            else:
                right-=1
        return []
            
        
   
