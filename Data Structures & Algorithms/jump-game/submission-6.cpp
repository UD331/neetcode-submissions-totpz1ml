class Solution {
public:
    bool canJump(vector<int>& nums) {
        int ind = size(nums)-1;
        for (int i = ind-1; i>=0; i--) {
            cout << nums[i] << "\t" << i << "\n";
            if ((i+nums[i]) >= ind)
                ind = i;
        }
        cout << ind;
        if (ind == 0)
            return true;
        return false;
    }
};
