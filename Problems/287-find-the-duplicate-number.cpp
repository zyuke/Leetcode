// https://leetcode.com/problems/find-the-duplicate-number

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        set<int> seen;
        int n = nums.size();
        for (int i = 0; i<n;i++){
            if (seen.count(nums[i])) return nums[i];
            else seen.insert(nums[i]);
        }
        return 0;
    }
};