class Solution(object):
    def minSwaps(self, nums):
        n=len(nums)
        total_ones=sum(nums)
        if total_ones in [0,n]:
            return 0
        
        nums = nums + nums
        current_ones_in_window=sum(nums[:total_ones])
        max_ones_in_window=current_ones_in_window
        
        for i in range(total_ones,len(nums)):
            current_ones_in_window+=nums[i]-nums[i-total_ones]
            max_ones_in_window=max(max_ones_in_window,current_ones_in_window)
        min_swaps_needed=total_ones-max_ones_in_window
        
        return min_swaps_needed

