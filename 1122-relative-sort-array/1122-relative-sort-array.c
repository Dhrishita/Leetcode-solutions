int* relativeSortArray(int* arr1, int arr1Size, int* arr2, int arr2Size, int* returnSize) 
{
    int freq[1001] = {0}; 
    for (int i=0;i<arr1Size;i++)  //counting occurences of element
    {
        freq[arr1[i]]++;
    }
    int* ans = (int*)malloc(arr1Size * sizeof(int));
    int index = 0;
    for (int i=0; i<arr2Size;i++) //arr2->arr1 in sorted according to their freq
    {
        while (freq[arr2[i]] > 0) 
        {
            ans[index++] = arr2[i];
            freq[arr2[i]]--;
        }
    }
    for (int i=0; i<1001;i++) //remaining ele from arr1 (! in arr2) in sorted order
    {
        while (freq[i] > 0) 
        {
            ans[index++] = i;
            freq[i]--;
        }
    }
   *returnSize = arr1Size;
    return ans;
}

