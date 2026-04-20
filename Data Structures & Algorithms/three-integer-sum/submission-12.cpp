class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>> res;
        for (int i = 0; i < n; i++) {
            if (nums[i] > 0)
                break;
            int j = i+1, k = n-1;
            if (i > 0 && nums[i] == nums[i-1])
              continue;
            while (j<k) {
                int s = nums[i] + nums[j] + nums[k];
                if (s < 0) {
                    j++;
                } else if (s > 0) {
                    k--;
                } else {
                    res.push_back({nums[i], nums[j], nums[k]});
                    k--;
                    j++;
                    while(j <n && nums[j] == nums[j-1])
                        j++;
                }
            }
        }
        return res;
    }
};