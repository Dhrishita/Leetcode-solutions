class Solution(object):
    def frequencySort(self, nums):
        frequency={}
        for num in nums:
            frequency[num]=frequency.get(num,0)+1
            
        sorted_nums=sorted(nums,key=lambda x:(frequency[x],-x))
        return sorted_nums
    
        