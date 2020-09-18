//
// @lc app=leetcode.cn id=2 lang=c
//
// [2] add-two-numbers
//
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* output=malloc(sizeof(struct ListNode));
    output->next=NULL;
    struct ListNode* ptr=output;
    int carry=0;
    while(l1||l2)
    {
        if(l1&&l2)ptr->val=l1->val+l2->val+carry;
        else if(l1)ptr->val=l1->val+carry;
        else if(l2)ptr->val=l2->val+carry;
        if(carry)carry=0;
        carry=ptr->val/10;
        ptr->val=ptr->val%10;
        if(l1)l1=l1->next;
        if(l2)l2=l2->next;
        if(l1||l2)
        {
        struct ListNode *nextNode=malloc(sizeof(struct ListNode));
        nextNode->next=NULL;
        ptr->next=nextNode;
        ptr=ptr->next;
        }
        if(carry&&!l1&&!l2){
        struct ListNode *nextNode=malloc(sizeof(struct ListNode));
        nextNode->next=NULL;
        ptr->next=nextNode;
        ptr=ptr->next;
        ptr->val=1;
        }
    }
    return output;
}
// @lc code=end