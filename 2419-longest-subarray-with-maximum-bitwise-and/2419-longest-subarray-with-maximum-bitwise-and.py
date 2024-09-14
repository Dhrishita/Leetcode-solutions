class Solution(object):
    def longestSubarray(self, nums):
        max_value=max(nums)
        max_len=0
        curr_len=0
        for num in nums:
            if num==max_value:
                curr_len+=1
                max_len=max(max_len,curr_len)
            else:
                curr_len=0
        return max_len