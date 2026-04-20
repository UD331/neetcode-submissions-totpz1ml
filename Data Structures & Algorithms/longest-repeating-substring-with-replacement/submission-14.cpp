class Solution {
public:
    int characterReplacement(std::string s, int k) {
        unordered_map<char, int> m;;
        int res = 0, mf = 0, l = 0, r = 0;
        for (int r = 0; r < s.size(); r++) {
            m[s[r]]++;
            mf = max(mf, m[s[r]]);
            while (r-l+1-k >mf) {
                m[s[l]]--;
                l++;
            }
            res = max(res, r-l+1);
        }
        return res;
    }
};