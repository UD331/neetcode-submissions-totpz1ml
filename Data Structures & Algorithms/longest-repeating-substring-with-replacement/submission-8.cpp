class Solution {
public:
    int characterReplacement(std::string s, int k) {
        int l = 0, res = 0, mf = 1;
        unordered_map<char,int> m;
        m[s[l]]++;
        for (int r =1; r<s.size(); r++) {
            m[s[r]]++;
            mf = max(mf, m[s[r]]);
            while(r-l+1-k>mf) {
                m[s[l]]--;
                l++;
            }
            res = max(res, r-l+1);
        }
        return res;
    }
};