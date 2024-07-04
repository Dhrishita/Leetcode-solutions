/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeNodes(struct ListNode* head) 
{
    struct ListNode* dummy=(struct ListNode*)malloc(sizeof(struct ListNode));
    dummy->val=0;
    dummy->next=NULL;
    struct ListNode* current_new=dummy;
    struct ListNode* current_old=head->next;  
    int current_sum=0;
    
    while (current_old!=NULL) 
    {
        if (current_old->val==0) 
        {
            if (current_sum!=0) 
            {
                struct ListNode* new_node=(struct ListNode*)malloc(sizeof(struct ListNode));
                new_node->val=current_sum;
                new_node->next=NULL;
                current_new->next=new_node;
                current_new=new_node;
                current_sum=0;
            }
        } 
        else 
        {
            current_sum+=current_old->val;
        }
        current_old=current_old->next;
    }
    struct ListNode* result=dummy->next;
    free(dummy);  
    return result;
}
