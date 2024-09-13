class Solution(object):
    def xorQueries(self, arr, queries):
        n = len(arr)
        d=[0]*(n+1)
        for i in range(n):
            d[i+1]=d[i]^arr[i]
        ans=[]
        for left,right in queries:
            ans.append(d[right+1]^d[left])
        return ans