#include <cmath>
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int c = 0;
        unordered_set<int> s(nums.begin(), nums.end());
        for (int r = 0; r <nums.size(); r++) {
            int n = nums[r], ch = 1;
            while(s.count(n-1)) {
                ch++;
                n--;
            }
            c = max(c,ch);
        }
        return c;
    }
};
