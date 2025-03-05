class Solution(object):
    def mergeArrays(self, nums1, nums2):
        dict={}
        for id,val in nums1:
            dict[id] = dict.get(id,0)+val  
        for id,val in nums2:
            dict[id] = dict.get(id,0)+val  
        return sorted([[id,val] for id,val in dict.items()])       