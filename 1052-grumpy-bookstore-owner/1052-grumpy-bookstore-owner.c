int maxSatisfied(int* customers, int customersSize, int* grumpy, int grumpySize, int minutes) 
{
    int satisfied=0;
    for(int i=0;i<customersSize;i++) 
    {
        if(grumpy[i]==0) 
        {
            satisfied+=customers[i];
        }
    }
    int maxSatisfied=0;
    int currentSatisfied=0;
    
    for(int i=0;i<customersSize;i++) 
    {
        if(grumpy[i]==1) 
        {
            currentSatisfied+=customers[i];
        }
        if(i>=minutes)
        {
            if(grumpy[i - minutes]==1) 
            {
                currentSatisfied-=customers[i - minutes];
            }
        }
        if(i>=minutes-1) 
        {
            if(currentSatisfied>maxSatisfied) 
            {
                maxSatisfied=currentSatisfied;
            }
        }
    }
    return satisfied+maxSatisfied;
}
