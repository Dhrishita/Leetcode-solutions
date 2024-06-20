class Solution(object):
    def maxDistance(self, position, m):
        position.sort()
        n = len(position)
    
        def check(min_dist):
            count = 1  
            last_position = position[0]
            
            for i in range(1, n):
                if position[i] - last_position >= min_dist:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        
        left, right = 1, position[-1] - position[0]
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans
