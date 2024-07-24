class Solution(object):
    def sortJumbled(self, mapping, nums):
        def get_mapped_value(num):
            mapped_num=int(''.join(str(mapping[int(digit)]) for digit in str(num)))
            return mapped_num
        return sorted(nums,key=get_mapped_value)


