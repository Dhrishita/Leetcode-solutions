class Solution(object):
    def rangeSum(self, nums, n, left, right):
        MOD=10**9+7
        subarray=[]
        for i in range(n):
            curr_sum=0
            for j in range(i,n):
                curr_sum+=nums[j]
                subarray.append(curr_sum)
        subarray.sort()
        ans=sum(subarray[left-1:right])%MOD
        return ans
        