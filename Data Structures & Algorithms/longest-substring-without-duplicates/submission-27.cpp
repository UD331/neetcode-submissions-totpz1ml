class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 0)
            return 0;
        int l = 0, m = 0;
        unordered_set<char> st;
        //st.insert(s[l]);
        for(int r = 0; r < s.size(); r++) {
            while(st.count(s[r]) == 1) {
                st.erase(s[l]);
                l++;
            }
            st.insert(s[r]);
            m = max(m, r-l+1);
        }
        return m;
    }
};