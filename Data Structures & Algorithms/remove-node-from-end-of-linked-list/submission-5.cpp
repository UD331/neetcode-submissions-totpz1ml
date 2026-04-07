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
        ListNode* n = head;
        int l = 0;
        while (n != nullptr) {
            l++;
            n = n->next;
        }
        int f = l-c;
        if (f == 0) {
            return head->next;
        }
        n = head;
        for (int i = 0; i < l - 1; i++) {
            if ((i + 1) == f) {
                n->next = n->next->next;
                break;
            }
            n = n->next;
        }

        return head;
    }
};
