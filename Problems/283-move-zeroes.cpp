// https://leetcode.com/problems/move-zeroes

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int count =  0;
        int n = nums.size();
        for (int i = 0; i < n; i++){
            if (nums[i] != 0){
                
                nums[count] = nums[i];
                count++;
            }
        }
        for (int j = count; j < n; j++){
            nums[j] = 0;
        }
    }
};