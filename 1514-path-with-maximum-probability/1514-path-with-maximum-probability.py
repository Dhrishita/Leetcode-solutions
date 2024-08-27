import heapq
from collections import defaultdict
class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        graph=defaultdict(list)
        for (u,v),prob in zip(edges,succProb):
            graph[u].append((v,prob))
            graph[v].append((u,prob))
        
        maxHeap=[(-1,start)]
        probabilities=[0]*n
        probabilities[start]=1

        while maxHeap:
            currProb,node=heapq.heappop(maxHeap)
            currProb=-currProb
            if node==end:
                return currProb
            for neighbor,edgeProb in graph[node]:
                newProb=currProb*edgeProb
                if newProb>probabilities[neighbor]:
                    probabilities[neighbor]=newProb
                    heapq.heappush(maxHeap,(-newProb,neighbor))
        return 0.0