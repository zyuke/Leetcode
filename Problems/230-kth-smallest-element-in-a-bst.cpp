// https://leetcode.com/problems/kth-smallest-element-in-a-bst

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void inorder(TreeNode* root, int& v, int& k){
        if (!root) return;
        inorder(root->left, v, k);
        k--;
        if (k == 0){
            v = root->val;
            return;
        }
        inorder(root->right, v, k);
    }
    
    int kthSmallest(TreeNode* root, int k) {
        int v = 0;
        inorder(root, v, k);
        return v;
    }
};