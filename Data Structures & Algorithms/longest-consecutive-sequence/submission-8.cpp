#include <cmath>
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int c = 0;
        unordered_set<int> s(nums.begin(), nums.end());
        for (int n : nums) {
            int check = 1, m = n;
            while (s.count(m-1) == 1) {
                check++;
                m--;
            }
            c = max(c, check);
        }
        return c;
    }
};
