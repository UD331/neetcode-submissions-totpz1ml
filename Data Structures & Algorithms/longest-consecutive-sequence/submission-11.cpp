#include <cmath>
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int c = 0;
        unordered_set<int> s(nums.begin(), nums.end());
        for (int r = 0; r <nums.size(); r++) {
            if (!s.count(nums[r]-1)) {
                int ch = nums[r], l = 1;
                while(s.count(ch+1)) {
                    ch++;
                    l++;
                }
                c = max(c, l);

            }
        }
        return c;
    }
};
