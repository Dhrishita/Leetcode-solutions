void reverse(int* nums, int left, int right) 
{
    while (left < right)
    {
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
        left++;
        right--;
    }
}
void rotate(int* nums, int numsSize, int k) {
    k = k % numsSize; 
    if (k == 0) 
    return; 

    reverse(nums, 0, numsSize - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, numsSize - 1);
}

