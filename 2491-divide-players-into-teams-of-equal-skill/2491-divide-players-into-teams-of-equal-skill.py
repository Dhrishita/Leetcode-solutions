class Solution(object):
    def dividePlayers(self, skill):
        d=len(skill)
        total_sum=sum(skill)
        num_teams=d//2
        
        if total_sum%num_teams!=0:
            return -1
        
        team_skill=total_sum // num_teams
        skill.sort()
        
        chemistry_sum=0
        for i in range(num_teams):
            if skill[i]+skill[d-1-i]!=team_skill:
                return -1
            chemistry_sum+=skill[i]*skill[d-1-i]
        return chemistry_sum