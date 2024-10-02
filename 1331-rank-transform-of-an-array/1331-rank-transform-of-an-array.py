class Solution(object):
    def arrayRankTransform(self, arr):
        sort_the_arr=sorted(set(arr))
        rank_map={num:rank+1 for rank, num in enumerate(sort_the_arr)}
        return [rank_map[num] for num in arr]