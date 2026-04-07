class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map <int, int> m;
        for(int i = 0; i < n; i++){
            m[nums[i]] = i;
        }
        for(int i = 0; i < n; i++){
            int k = target - nums[i];
            if (m.count(k) == 1)
                if (i != m[k])
                    return {i, m[k]};
        }
        return {};
    }
};