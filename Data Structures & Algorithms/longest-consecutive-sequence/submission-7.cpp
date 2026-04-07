#include <cmath>
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int c = 0;
        unordered_set<int> s;
        s.insert(nums.begin(), nums.end());
        for(int i: nums) {
            int l = 1;
            while (s.count(i+l) == 1)
                l++;
            c = max(c, l);
        }
        return c;
    }
};
