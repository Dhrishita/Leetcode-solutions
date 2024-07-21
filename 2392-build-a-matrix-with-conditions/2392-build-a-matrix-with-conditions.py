from collections import defaultdict, deque
class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        def topological_sort(graph,in_degree):
            sorted_list =[]
            queue =deque([node for node in range(1, k + 1) if in_degree[node]==0])
            
            while queue:
                node=queue.popleft()
                sorted_list.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor]-=1
                    if in_degree[neighbor]==0:
                        queue.append(neighbor)
            
            return sorted_list if len(sorted_list)==k else []

        def build_graph(conditions):
            graph=defaultdict(list)
            in_degree=[0] *(k + 1)
            for u, v in conditions:
                graph[u].append(v)
                in_degree[v]+=1
            return graph, in_degree

        row_graph,row_in_degree=build_graph(rowConditions)
        row_order=topological_sort(row_graph, row_in_degree)
        if not row_order:
            return []
        
        col_graph,col_in_degree=build_graph(colConditions)
        col_order=topological_sort(col_graph, col_in_degree)
        if not col_order:
            return []

        row_pos={num: i for i, num in enumerate(row_order)}
        col_pos={num: i for i, num in enumerate(col_order)}

        matrix=[[0]*k for _ in range(k)]
        for num in range(1,k + 1):
            r,c=row_pos[num],col_pos[num]
            matrix[r][c]=num

        return matrix