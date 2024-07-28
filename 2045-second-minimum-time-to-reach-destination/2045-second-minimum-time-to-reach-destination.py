from collections import deque, defaultdict
import sys

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj=defaultdict(list)
        for edge in edges:
            a,b=edge
            adj[a].append(b)
            adj[b].append(a)
        
        time_taken=[[sys.maxsize,sys.maxsize] for _ in range(n+1)]
        time_taken[1][0]=0
        queue=deque([(1, 0)])
        
        while queue:
            node,current_time=queue.popleft()
            if node==n and time_taken[node][1]!=sys.maxsize:
                break
            if (current_time//change)%2!=0:
                wait_time=change-(current_time%change)
                current_time+=wait_time+time
            else:
                current_time+=time

            for neighbor in adj[node]:
                if time_taken[neighbor][0]==sys.maxsize:
                    time_taken[neighbor][0]=current_time
                    queue.append((neighbor, current_time))
                elif time_taken[neighbor][1]==sys.maxsize and current_time >time_taken[neighbor][0]:
                    time_taken[neighbor][1]=current_time
                    queue.append((neighbor,current_time))
        
        return time_taken[n][1]

