class Solution(object):
    def maximumSwap(self, num):
        num_list=list(str(num))
        last={int(digit): i for i,digit in enumerate(num_list)}
        for i, digit in enumerate(num_list):
            for d in range(9,int(digit),-1):
                if last.get(d,-1)>i:
                    num_list[i],num_list[last[d]]=num_list[last[d]],num_list[i]
                    return int("".join(num_list))
        return num