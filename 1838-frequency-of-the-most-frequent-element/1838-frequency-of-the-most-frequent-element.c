int compare(const void *a, const void *b )
{
    return (*(int *)a- *(int *)b);
}
int maxFrequency(int* nums, int numsSize, int k) {
    qsort(nums, numsSize, sizeof(int),compare);
    long long total =0;
    int left =0;
    int res=1;
    for(int right =0;right<numsSize; right++)
    {
        total+=nums[right];
        int d= right-left+1;
        long long m = (long long)d * nums[right] - total;

        while(m>k)
        {
            total-=nums[left];
            left++;
            d=right-left+1;
            m= (long long)d * nums[right] - total;
        }
        if(d>res)
        {
            res=d;
        }
    }
    return res; 
}