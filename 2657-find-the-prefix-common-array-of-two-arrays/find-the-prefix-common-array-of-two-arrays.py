class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        D=len(A)
        seen=set() 
        C=[]        
        common_cnt=0
        for i in range(D):
            if A[i] in seen:
                common_cnt+=1
            else:
                seen.add(A[i])
            if B[i] in seen:
                common_cnt+=1
            else:
                seen.add(B[i])
            C.append(common_cnt)
        return C