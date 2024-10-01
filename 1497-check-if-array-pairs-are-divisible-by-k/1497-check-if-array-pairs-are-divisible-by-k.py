class Solution(object):
    def canArrange(self, arr, k):
        rem_cnt=[0]*k
        for num in arr:
            rem=num%k
            if rem<0:  
                rem+=k
            rem_cnt[rem]+=1

        for d in range(k):
            if d==0:
                if rem_cnt[d]%2!=0:
                    return False
            else:
                if rem_cnt[d]!=rem_cnt[k-d]:
                    return False
        return True