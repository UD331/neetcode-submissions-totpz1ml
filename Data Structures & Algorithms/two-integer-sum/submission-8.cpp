class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map <int, int> m;
        for(int i = 0; i < n; i++)
            m[nums[i]] = i;
        for (int i = 0; i < n; i++) {
            int s = target - nums[i];
            if (m.count(s) == 1 && m[s] != i) 
                return {i, m[s]};
        }
        return {};
    }
};