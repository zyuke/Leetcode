// https://leetcode.com/problems/sum-root-to-leaf-numbers

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
    void helper(TreeNode* root, vector<int>& s, int res){
        if (root != nullptr){
            if (root->left == nullptr && root->right == nullptr){
                s.push_back(10*res + root->val);
        }
            else{
                helper(root->left, s, res*10+root->val);
                helper(root->right, s, res*10+root->val);
            }
        }

    }
    
    int sumNumbers(TreeNode* root) {
        vector<int> s;
        helper(root, s, 0);
        int res = 0;
        for(vector<int>::iterator it = s.begin(); it != s.end(); ++it){
            res += *it;
        }
        
        return res;
    }
};