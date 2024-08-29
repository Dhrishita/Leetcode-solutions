class Solution(object):
    def removeStones(self, stones):
        dhrishita={}
        def find(m):
            if dhrishita.setdefault(m,m)!=m:
                dhrishita[m]=find(dhrishita[m])
            return dhrishita[m]
        
        def union(m,d):
            dhrishita[find(m)]=find(d)
        for m, d in stones:
            union(m,~d)  
        unique_components=len({find(m) for m,d in stones})
        return len(stones)-unique_components