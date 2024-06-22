int numberOfSubarrays(int* nums, int numsSize, int k) {
    int cnt=0;
    int odd_cnt=0;
    int prefix_cnt[50001]={0}; 
    prefix_cnt[0]=1;  
    for (int i=0;i<numsSize;i++) 
    {
        if (nums[i]%2== 1) 
        {
            odd_cnt++;
        }
        if (odd_cnt>=k) 
        {
            cnt+=prefix_cnt[odd_cnt - k];
        }
        prefix_cnt[odd_cnt]++;
    }
    return cnt;
}