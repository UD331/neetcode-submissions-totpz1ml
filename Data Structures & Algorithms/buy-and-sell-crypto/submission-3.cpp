class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int mp = 0, m = prices[0];
        for (int p: prices) {
            if (p < m) {
                m = p;
            }
            mp = max(mp,(p - m));
        }
        return mp;
    }
};
