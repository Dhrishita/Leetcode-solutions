class Solution(object):
    def findMinDifference(self, timePoints):
        def convertToMinutes(time):
            hrs,mins=map(int,time.split(":"))
            return hrs*60+mins

        mins_seen=[False]*1440
        for time in timePoints:
            mins=convertToMinutes(time)
            if mins_seen[mins]:  
                return 0
            mins_seen[mins] = True

        first_time=-1
        last_time=-1
        prev_time=-1
        min_diff=float('inf')

        for i in range(1440):
            if mins_seen[i]:
                if first_time==-1:
                    first_time=i  
                if prev_time!=-1:
                    min_diff=min(min_diff, i - prev_time) 
                prev_time=i
                last_time=i  
        min_diff=min(min_diff,1440+first_time-last_time)
        return min_diff