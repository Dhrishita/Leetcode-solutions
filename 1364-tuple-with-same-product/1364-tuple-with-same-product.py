from collections import defaultdict

class Solution(object):
    def tupleSameProduct(self, nums):
        pc = defaultdict(int)
        cnt = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                cnt += pc[product] * 8
                pc[product] += 1
        return cnt