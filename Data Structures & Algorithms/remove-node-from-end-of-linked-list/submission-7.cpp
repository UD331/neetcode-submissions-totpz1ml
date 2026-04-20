/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int c) {
        ListNode* t = head;
        int l = 0;
        while(t) {
            l++;
            t = t->next;
        }
        int r = l-c;
        if (r < 0)
            return head;
        else if (r == 0)
            return head->next;
        t = head;
        ListNode* prev = nullptr;
        int i = 0;
        while (i<r) {
            prev = t;
            t = t->next;
            i++;
        }
        
        prev->next = t->next;
        return head;
    }
};
