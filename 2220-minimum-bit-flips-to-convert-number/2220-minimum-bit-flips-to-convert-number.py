class Solution(object):
    def minBitFlips(self, start, goal):
        xor_res=start^goal
        return bin(xor_res).count('1')