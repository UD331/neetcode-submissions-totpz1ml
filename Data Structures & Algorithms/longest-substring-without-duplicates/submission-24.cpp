class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0, n = 0;
        unordered_set<char> c;
        for (int r = 0; r < s.size(); r++) {
            while(c.count(s[r]) == 1) {
                c.erase(s[l]);
                l++;
            }
            c.insert(s[r]);
            n = max(n, (r-l+1));
        }
        return n;
    }
};