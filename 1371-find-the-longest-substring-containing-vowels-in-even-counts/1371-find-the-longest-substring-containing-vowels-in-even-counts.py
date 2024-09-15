class Solution(object):
    def findTheLongestSubstring(self, s):
        vowel_to_bit = {'a':0,'e':1,'i':2,'o':3,'u':4}
        first_occurrence={0:-1}
        bitmask=0
        max_len=0
        
        for index, char in enumerate(s):
            if char in vowel_to_bit:
                bitmask^=(1<<vowel_to_bit[char])
            if bitmask in first_occurrence:
                max_len=max(max_len,index-first_occurrence[bitmask])
            else:
                first_occurrence[bitmask]=index
            
            for i in range(5):
                masked_bitmask=bitmask^(1<<i)
                if masked_bitmask in first_occurrence:
                    max_length=max(max_len,index-first_occurrence[masked_bitmask])
        return max_len