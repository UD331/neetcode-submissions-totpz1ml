class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> x;
        int c = 0;
        int l = 0;
        for (int r = 0; r<s.size(); r++) {
            while (x.count(s[r]) == 1) {
                x.erase(s[l]);
                l++;
            }
            x.insert(s[r]);
            c = max(c, r-l+1);
        }
        return c;
    }
};