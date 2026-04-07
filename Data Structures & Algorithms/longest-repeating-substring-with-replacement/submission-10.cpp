class Solution {
public:
    int characterReplacement(std::string s, int k) {
        unordered_map<char, int> m;;
        int mf = 0, l = 0, res = 0;
        for (int r =0; r < s.size(); r++) {
            m[s[r]]++;
            mf = max(mf, m[s[r]]);
            while(r-l-k+1>mf) {
                m[s[l++]]--;
            }
            res = max(res, r-l+1);
        }
        return res;
    }
};