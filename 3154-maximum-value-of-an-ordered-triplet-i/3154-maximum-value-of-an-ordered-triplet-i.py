class Solution(object):
    def maximumTripletValue(self, nums):
        n = len(nums)
        max_value = 0

        for j in range(1, n - 1):  
            max_i = max(nums[:j])  
            max_k = max(nums[j+1:]) 

            triplet_value = (max_i - nums[j]) * max_k
            max_value = max(max_value, triplet_value)
        return max_value 