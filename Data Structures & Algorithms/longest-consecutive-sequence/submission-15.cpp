#include <cmath>
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int c =0;
        unordered_set<int> s(nums.begin(), nums.end());
        for (int r = 0;r<nums.size();r++){
            if (s.count(nums[r]-1) != 1){
                int n = nums[r]+1;
                int count=1;
                while(s.count(n++))
                    count++;
                c = max(c,count);
            }
        }
        return c;
    }
};
