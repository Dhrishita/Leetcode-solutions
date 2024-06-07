int singleNumber(int* nums, int numsSize) {
    int XOR=0;
    for(int i=0;i<numsSize;i++)
    {
        XOR=XOR^nums[i];
    }
    return XOR;
}