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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* t = head;
        int c = 0;
        while (t){
            c++;
            t=t->next;
        }
        c-=n;
        t = head;
        if (c == 0) {
            return head->next;
        }
        for (int i = 0; i< c;i++) {
            if ((i+1) == c) {
                t->next = t->next->next;
                break;
            }
            t = t->next;
        }
        return head;
    }
};
