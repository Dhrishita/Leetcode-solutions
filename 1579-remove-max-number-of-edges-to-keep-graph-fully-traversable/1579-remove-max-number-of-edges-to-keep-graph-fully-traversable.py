class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank=[0]*(n + 1)
        self.components=n
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        X = self.find(x)
        Y = self.find(y)
        
        if X!=Y:
            if self.rank[X]>self.rank[Y]:
                self.parent[Y]=X
            elif self.rank[X]<self.rank[Y]:
                self.parent[X]=Y
            else:
                self.parent[Y]=X
                self.rank[X]+=1
            self.components-=1
    
    def isSingle(self):
        return self.components==1

class Solution(object):
    def maxNumEdgesToRemove(self,n,edges):
        edges.sort(key=lambda x:x[0],reverse=True)
        alice = DSU(n)
        bob = DSU(n)
        added_edges = 0
        
        for edge in edges:
            t,u,v=edge
            if t==3:
                if alice.find(u)!=alice.find(v):
                    alice.union(u,v)
                    if bob.find(u)!=bob.find(v):
                        bob.union(u,v)
                        added_edges+=1
                        
            elif t==2:
                if bob.find(u)!=bob.find(v):
                    bob.union(u,v)
                    added_edges+=1
                    
            elif t==1:
                if alice.find(u)!=alice.find(v):
                    alice.union(u,v)
                    added_edges+=1
        
        if alice.isSingle() and bob.isSingle():
            return len(edges)-added_edges
        else:
            return -1