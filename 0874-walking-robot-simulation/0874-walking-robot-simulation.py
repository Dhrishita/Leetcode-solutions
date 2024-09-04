class Solution(object):
    def robotSim(self, commands, obstacles):
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        dir_index=0  
        x,y=0,0  
        obstacle_set=set(map(tuple,obstacles))
        max_dist_sq=0 
        for d in commands:
            if d==-2: 
                dir_index=(dir_index-1)%4
            elif d==-1:  
                dir_index=(dir_index+1)%4
            else:  
                for _ in range(d):
                    nx,ny=x+directions[dir_index][0],y+directions[dir_index][1]
                    if (nx,ny) not in obstacle_set:
                        x,y=nx,ny
                        max_dist_sq=max(max_dist_sq, x*x+y*y)
                    else:
                        break 
        return max_dist_sq