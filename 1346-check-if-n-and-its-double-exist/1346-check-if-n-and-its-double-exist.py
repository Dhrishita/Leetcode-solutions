class Solution(object):
    def checkIfExist(self, arr):
        arr.sort()
        d=len(arr)
        for m in range(d):
            for s in range(m+1,d):
                if arr[m]==2*arr[s] or arr[s]==2*arr[m]:
                    return True
        return False
        