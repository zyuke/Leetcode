// https://leetcode.com/problems/sort-colors

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n1 = 0; int n2 = 0;
        int n = nums.size();
        for (int i = 0 ; i < n; i++){
            if (nums[i] == 0) n1+=1;
            if (nums[i] == 1) n2+=1;
        }
        
        for (int i = 0; i <n; i++){
            if (n1 > 0) {
                nums[i] = 0;
                n1--;
            }
            else {
                if (n2 > 0) {
                    nums[i] = 1;
                    n2--;   
                }
                else {
                    nums[i] = 2;
                }
            }
        }
    }
};