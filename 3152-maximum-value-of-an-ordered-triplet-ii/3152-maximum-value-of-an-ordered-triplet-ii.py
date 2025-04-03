class Solution(object):
    def maximumTripletValue(self, nums):
        n = len(nums)
        if n < 3: return 0

        max_left = [0] * n
        max_right = [0] * n
        
        max_left[0] = nums[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], nums[i])

        max_right[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], nums[i])

        max_value = 0
        for j in range(1, n-1):
            triplet_value = (max_left[j-1] - nums[j]) * max_right[j+1]
            max_value = max(max_value, triplet_value)

        return max_value