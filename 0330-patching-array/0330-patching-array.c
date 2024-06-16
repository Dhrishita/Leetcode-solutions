int minPatches(int* nums, int numsSize, int n) {
    long long maxsum = 0; 
    int patches = 0; 
    int i = 0;
    while(maxsum<n) 
    {
        if(i<numsSize && nums[i]<=maxsum+1)
        {
            maxsum+= nums[i];
            i++;
        }
        else 
        {
            maxsum+= maxsum+1; 
            patches++;
        }
    }
    return patches;
}

