class Solution(object):
    def lexicalOrder(self,n):
        d_ans=[]
        def dfs(curr):
            if curr>n:
                return
            d_ans.append(curr)
            for m in range(10):
                next_num=curr*10+m
                if next_num>n:
                    break
                dfs(next_num)
        for m in range(1,10):
            if m>n:
                break
            dfs(m)
        return d_ans