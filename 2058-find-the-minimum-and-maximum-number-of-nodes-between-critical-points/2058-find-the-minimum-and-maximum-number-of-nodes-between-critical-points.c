/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* nodesBetweenCriticalPoints(struct ListNode* head, int* returnSize) {
     *returnSize = 2;
    int* result = (int*)malloc(2 * sizeof(int));
    result[0] = -1;
    result[1] = -1;
    struct ListNode* prev = head;
    struct ListNode* curr = head->next;
    if (!curr) return result; 

    int index = 1;
    int first=-1, last=-1;
    int min_dist=INT_MAX;

    while (curr->next != NULL) 
    {
        struct ListNode* next = curr->next;
        if ((curr->val > prev->val && curr->val > next->val) || 
            (curr->val < prev->val && curr->val < next->val)) 
        {
            if (first==-1) 
            {
                first=index;
            }
            else 
            {
                min_dist = (min_dist<(index-last)) ? min_dist : (index - last);
            }
            last=index;
        }
        prev = curr;
        curr = next;
        index++;
    }
    if (first!=-1 && last!=-1 && first!=last)
    {
        result[0]=min_dist;
        result[1]=last - first;
    }
    return result;
}