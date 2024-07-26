class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        distance=[[float('inf')] * n for _ in range(n)]
        for i in range(n):
            distance[i][i]=0
        
        for d, m, w in edges:
            distance[d][m]=w
            distance[m][d]=w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distance[i][j]>distance[i][k]+distance[k][j]:
                        distance[i][j]=distance[i][k]+distance[k][j]
        
        min_reachable_cities=n
        result_city=-1
        for i in range(n):
            count=sum(1 for j in range(n) if distance[i][j]<=distanceThreshold)
            if count<min_reachable_cities or (count==min_reachable_cities and i>result_city):
                min_reachable_cities=count
                result_city=i
        
        return result_city