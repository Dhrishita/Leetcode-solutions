int subarraysDivByK(int* nums, int numsSize, int k) {
    int *hash_map = (int*)calloc(k, sizeof(int));
    hash_map[0] = 1; 
    int sum = 0;
    int cnt = 0;
    
    for (int i = 0; i < numsSize; i++) 
    {
        sum += nums[i];
        int mod = sum % k;
        if (mod < 0)
        {
            mod += k;
        }
        cnt += hash_map[mod];
        hash_map[mod]++;
    }
    free(hash_map);
    return cnt; 
}