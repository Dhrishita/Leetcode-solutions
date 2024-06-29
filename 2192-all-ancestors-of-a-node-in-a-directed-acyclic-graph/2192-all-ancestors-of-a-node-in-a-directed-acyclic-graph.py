from collections import defaultdict, deque
class Solution(object):
    def getAncestors(self, n, edges):
        graph=defaultdict(list)
        degree=[0]*n
        for u, v in edges:
            graph[u].append(v)
            degree[v] += 1
        
        topo_order=[]
        queue=deque([node for node in range(n) if degree[node]==0])
        while queue:
            node=queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                degree[neighbor]-=1
                if degree[neighbor]==0:
                    queue.append(neighbor)
                
        ancestors=[set() for _ in range(n)]
        for node in topo_order:
            for neighbor in graph[node]:
                ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)
        answer=[sorted(list(anc)) for anc in ancestors]
        return answer