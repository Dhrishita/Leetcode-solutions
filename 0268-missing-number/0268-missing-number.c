int missingNumber(int* nums, int numsSize) {
    int xor1=0, xor2=0;
    for(int i=0;i<=numsSize;i++)
    {
        xor1=xor1^i;
    }
    for(int i=0;i<numsSize;i++)
    {
        xor2=xor2^nums[i];
    }
    return xor1^xor2;
}