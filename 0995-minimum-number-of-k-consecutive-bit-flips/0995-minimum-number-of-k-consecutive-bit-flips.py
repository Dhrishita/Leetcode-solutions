class Solution(object):
    def minKBitFlips(self, nums, k):
        N = len(nums)
        flip_queue=[]
        flips=0
        for i in range(N):
            if flip_queue and flip_queue[0]+k<=i:
                flip_queue.pop(0)
           
            if len(flip_queue)%2==nums[i]:
                if i+k>N:
                    return -1
                flip_queue.append(i)
                flips+=1
        return flips