class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 0)
            return 0;
        int l = 0, m = 0;
        unordered_set<char> st;
        for (int r = 0; r<s.size();r++) {
            while(st.count(s[r]))
                st.erase(s[l++]);
            m = max(m,r-l+1);
            st.insert(s[r]);
        }
        return m;
    }
};