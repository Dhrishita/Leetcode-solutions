class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        robots=list(zip(positions, healths, directions))
        robots.sort()  
    
        stack=[]  
        survivors=[] 
        
        for pos, health, direction in robots:
            if direction=='R':
                stack.append((pos, health))
            else:  # direction=='L'
                while stack and health>0:
                    last_pos, last_health=stack[-1]
                    if last_health<health:
                        stack.pop()
                        health-=1
                    elif last_health==health:
                        stack.pop()
                        health=0
                        break
                    else: 
                        stack[-1]=(last_pos, last_health - 1)
                        health=0
                        break
                if health>0:
                    survivors.append((pos, health))
                    
        survivors.extend(stack)
        survivors.sort()
        
        pos_index={pos: i for i, pos in enumerate(positions)}
        results=[0]*len(positions)
        
        for pos, health in survivors:
            index=pos_index[pos]
            results[index]=health
        return [health for health in results if health > 0]

