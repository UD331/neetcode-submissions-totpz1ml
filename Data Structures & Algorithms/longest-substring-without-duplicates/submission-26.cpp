class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 0)
            return 0;
        int l = 0, m = 1;
        unordered_set<char> hs;
        hs.insert(s[l]);
        for(int r = 1; r <s.size(); r++) {
            while(hs.count(s[r]) != 0) {
                hs.erase(s[l]);
                l++;
            }
            hs.insert(s[r]);
            m = max(r-l+1,m);
        }
        return m;
    }
};