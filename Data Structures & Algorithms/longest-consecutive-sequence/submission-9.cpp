#include <cmath>
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int c = 0;
        unordered_set<int> s(nums.begin(), nums.end());
        for (int n:nums) {
            int m = n, check = 1;
            while(s.count(m-1)==1) {
                m--;
                check++;
            }
            c=max(check,c);
        }
        return c;
    }
};
