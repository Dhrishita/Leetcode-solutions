import sys
class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        n = 26 
        d=sys.maxsize
        distance=[[d]*n for _ in range(n)]
        
        for i in range(n):
            distance[i][i]=0
            
        for o,c,z in zip(original, changed, cost):
            distance[ord(o)-ord('a')][ord(c)-ord('a')]=min(distance[ord(o) - ord('a')][ord(c)-ord('a')],z)

        # Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distance[i][k]!=d and distance[k][j]!=d:
                        distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])

        total_cost = 0
        for s_char,t_char in zip(source,target):
            if s_char==t_char:
                continue
            min_cost = distance[ord(s_char)-ord('a')][ord(t_char)-ord('a')]
            if min_cost==d:
                return -1
            total_cost+=min_cost

        return total_cost