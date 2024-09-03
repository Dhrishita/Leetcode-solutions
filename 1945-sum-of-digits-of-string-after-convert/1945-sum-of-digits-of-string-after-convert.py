class Solution(object):
    def getLucky(self, s, k):
        number=''.join(str(ord(char)-ord('a')+1) for char in s)
        curr_sum=sum(int(digit) for digit in number)
        for _ in range(k - 1):
            curr_sum=sum(int(digit) for digit in str(curr_sum))
        return curr_sum