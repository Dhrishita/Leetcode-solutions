class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        worker.sort()
        MaxProfit = 0
        current_MP = 0
        j = 0  
        for ability in worker:
            while j < len(jobs) and jobs[j][0] <= ability:
                current_MP = max(current_MP, jobs[j][1])
                j += 1
            MaxProfit += current_MP
        return MaxProfit

