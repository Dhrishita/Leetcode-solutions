import heapq
class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        IPO = [(capital[i], profits[i]) for i in range(len(profits))]
        IPO.sort()  
        
        max_heap = []  
        index = 0
        for _ in range(k):
            while index < len(IPO) and IPO[index][0] <= w:
                heapq.heappush(max_heap, -IPO[index][1])
                index += 1
            
            if max_heap:
                w -= heapq.heappop(max_heap)
            else:
                break
        return w

