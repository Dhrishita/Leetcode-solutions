def combine(a,low,mid,high):
    i=low
    j=mid+1
    k=0
    temp=[0]*(high-low+1)

    while i<=mid and j<=high:
        if a[i]>a[j]:
            temp[k]=a[j]
            j+=1
        else:
            temp[k]=a[i]
            i+=1
        k+=1

    while i<=mid:
        temp[k]=a[i]
        i+=1
        k+=1

    while j<=high:
        temp[k]=a[j]
        j+=1
        k+=1

    for i in range(low,high+1):
        a[i]=temp[i-low]


def merge_sort(a,low,high):
    if low<high:
        mid=(low+high)//2
        merge_sort(a,low,mid)
        merge_sort(a,mid+1,high)
        combine(a,low,mid,high)

class Solution(object):
    def sortArray(self,nums):
        numsSize=len(nums)
        merge_sort(nums,0,numsSize-1)
        return nums