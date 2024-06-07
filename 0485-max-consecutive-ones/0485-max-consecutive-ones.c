int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int maximum=0, cnt=0;
    for(int i=0;i<numsSize;i++)
    {
        if(nums[i]==1)
        {
            cnt++;
            if(cnt>maximum)
            {
                maximum = cnt;
            }
        }
        else
        {
            cnt=0;
        }
    }
    return maximum;
}