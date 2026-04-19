/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {

        rev(root);
        return root;
    }

    void rev(TreeNode* node) {
        if (node == nullptr)
            return;
        TreeNode* t = node->left;
        node->left = node->right;
        node->right = t;
        rev(node->left);
        rev(node->right);
    }

};
