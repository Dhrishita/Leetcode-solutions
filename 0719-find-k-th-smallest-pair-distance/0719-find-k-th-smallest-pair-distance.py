class Solution(object):
    def smallestDistancePair(self, nums, k):
        def count_pairs(nums, mid):
            cnt=0
            j=0
            for i in range(len(nums)):
                while j<len(nums) and nums[j]-nums[i]<=mid:
                    j+=1
                cnt+=j-i-1
            return cnt

        nums.sort()
        low=0
        high=nums[-1]-nums[0]
        while low<high:
            mid=(low+high)//2
            if count_pairs(nums,mid)>=k:
                high=mid
            else:
                low=mid+1
        return low

        